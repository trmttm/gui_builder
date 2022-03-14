from typing import Dict
from typing import List

from view_tkinter import tk_interface

from .spacer_abc import SpacerABC
from .stacker_abc import StackerABC
from .widget_abc import WidgetABC


def register_elements(direction, elements, new_stacker: StackerABC, space: list):
    for n, element in enumerate(elements):
        row, col = get_widget_or_frame_row_col(direction, n, new_stacker)
        register_spacer(space, n, element)
        register_stacker(row, col, element, new_stacker)
        register_widgets(row, col, element, new_stacker)


def get_widget_or_frame_row_col(direction, n, new_stacker: StackerABC):
    return (n, 0) if (direction == new_stacker.v_direction) else (0, n)


def register_spacer(space: list, n: int, element:SpacerABC):
    if issubclass(element.__class__, SpacerABC):
        space.append(n + element.adjustment)


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


def configure_frame(new_stacker: StackerABC, direction, space: list):
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
