from typing import Dict
from typing import List

from view_tkinter import tk_interface

from .spacer_abc import SpacerABC
from .stacker_abc import StackerABC
from .widget_abc import WidgetABC


def configure_frame_of_new_stacker_for_later_command_execution(new_stacker: StackerABC, direction, space: list):
    fr_options = tk_interface.frame_options
    if not space:
        space = [0]
    if direction == new_stacker.v_direction:
        row_space, col_space = space, [0]
    else:
        row_space, col_space = [0], space
    rows_and_weights = tuple(row_space), tuple(1 for _ in row_space)
    cols_and_weights = tuple(col_space), tuple(1 for _ in col_space)
    new_stacker.set_frame_options(fr_options(rows_and_weights, cols_and_weights, ))


def register_elements(direction, elements, new_stacker: StackerABC, space):
    for n, element in enumerate(elements):
        row, col = get_widget_or_frame_row_col(direction, n, new_stacker)
        register_spacer(space, n, element)
        register_stacker(row, col, element, new_stacker)
        register_widgets(row, col, element, new_stacker)


def get_widget_or_frame_row_col(direction, n, new_stacker: StackerABC):
    return (n, 0) if (direction == new_stacker.v_direction) else (0, n)


def register_spacer(space: list, n: int, element):
    if issubclass(element.__class__, SpacerABC):
        space.append(n)


def register_stacker(row: int, col: int, element: StackerABC, new_stacker: StackerABC):
    if issubclass(element.__class__, StackerABC):
        frame_id = new_stacker.frame_id
        child_stacker = element
        new_stacker.children_stackers.append(child_stacker)
        configure_child_stacker(child_stacker, frame_id, row, col)


def configure_child_stacker(child_stacker: StackerABC, frame_id, row: int, col: int):
    child_stacker.set_parent(frame_id)
    child_stacker.set_row(row)
    child_stacker.set_col(col)
    child_stacker.increment_level()


def register_widgets(row: int, col: int, element: WidgetABC, new_stacker: StackerABC):
    if issubclass(element.__class__, WidgetABC) and not issubclass(element.__class__, SpacerABC):
        w: WidgetABC = element
        f = tk_interface.widget_model
        frame_id = new_stacker.frame_id
        widget_model = f(frame_id, w.id, w.widget_type, row, row, col, col, 'nsew', w.pad_xy, **w.options)
        new_stacker.add_widget_model(widget_model)


def get_sorted_frames(children_stackers: List[StackerABC]) -> dict:
    sorted_frames: Dict[int, list] = {}
    for child_stacker in children_stackers:
        level = child_stacker.level
        frame_id = child_stacker.frame_id
        if level in sorted_frames:
            sorted_frames[level].insert(0, frame_id)
        else:
            sorted_frames[level] = [frame_id]
    return sorted_frames


def freeze_frame(frame_id, frame_to_stacker_dictionary: dict):
    child_stacker: StackerABC = frame_to_stacker_dictionary.get(frame_id)
    frame_id = child_stacker.frame_id
    frame_parent = child_stacker.parent
    frame_options_ = child_stacker.frame_options
    row1 = child_stacker.row
    row2 = child_stacker.row
    col1 = child_stacker.col
    col2 = child_stacker.col
    static_kwargs = child_stacker.static_kwargs

    kwargs = {}
    kwargs.update(static_kwargs)
    kwargs.update({'parent_id': frame_parent, 'widget_id': frame_id})
    kwargs.update({'row1': row1, 'row2': row2})
    kwargs.update({'col1': col1, 'col2': col2})
    kwargs.update(frame_options_)

    frame = tk_interface.widget_model(**kwargs)
    return frame


def sort_view_model_for_paned_window(view_model: list):
    """
    1) PanedWindow widget model must be placed right after its parent frame_id
    2) PanedWindow's children frames are automatically created,
    3) but we need to pass their frame_options in order to properly configure row and column.
    """
    paned_window_ids = []
    paned_window_parents = set()
    frame_id_to_frame_options = {}
    widget_id_to_widget_model = {}
    for widget_model in view_model:
        parent_id = widget_model[0]
        widget_id = widget_model[1]
        widget_type = widget_model[2]

        widget_id_to_widget_model[widget_id] = widget_model

        if widget_type == 'paned_window':
            paned_window_ids.append(widget_id)
            paned_window_parents.add(parent_id)

        if widget_type == 'frame':
            frame_options: dict = widget_model[-1]['frame options']  # this logic looks so easy to break...
            frame_id_to_frame_options[widget_id] = frame_options

    all_paned_window_children = []
    paned_window_parent_to_paned_window_id = {}
    paned_window_id_to_children_frames = {}
    for widget_model in view_model:
        parent_id = widget_model[0]
        widget_id = widget_model[1]
        if parent_id in paned_window_ids:
            paned_window_child_frame_id = widget_id
            paned_window_id = parent_id

            all_paned_window_children.append(paned_window_child_frame_id)

            if paned_window_id in paned_window_id_to_children_frames:
                paned_window_id_to_children_frames[paned_window_id].append(paned_window_child_frame_id)
            else:
                paned_window_id_to_children_frames[paned_window_id] = [paned_window_child_frame_id]
        if widget_id in paned_window_ids:
            paned_window_id = widget_id
            if parent_id in paned_window_parent_to_paned_window_id:
                paned_window_parent_to_paned_window_id[parent_id].append(paned_window_id)
            else:
                paned_window_parent_to_paned_window_id[parent_id] = [paned_window_id]

    if paned_window_ids:
        sorted_viewed_model = []

        for widget_model in view_model:
            widget_id = widget_model[1]
            if widget_id not in paned_window_ids + all_paned_window_children:  # Ignore PanedWindows and their children
                sorted_viewed_model.append(widget_model)
            if widget_id in paned_window_parents:
                parent_of_paned_window = widget_id

                children_paned_window_ids = paned_window_parent_to_paned_window_id[parent_of_paned_window]
                # Add children frame options
                for paned_window_id in children_paned_window_ids:
                    list_of_frame_options = []
                    for paned_window_child_frame in paned_window_id_to_children_frames[paned_window_id]:
                        list_of_frame_options.append(frame_id_to_frame_options[paned_window_child_frame])

                    paned_window_widget_model = widget_id_to_widget_model[paned_window_id]
                    options: dict = paned_window_widget_model[-1]
                    additional_options = {'frame_options': list_of_frame_options, }
                    options.update(additional_options)
                    pw_widget_model_frame_options_added = paned_window_widget_model[:-1] + (options,)

                    sorted_viewed_model.append(pw_widget_model_frame_options_added)
    else:
        sorted_viewed_model = view_model
    return sorted_viewed_model
