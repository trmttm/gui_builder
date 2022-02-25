from typing import Dict
from typing import List
from typing import Union

from view_tkinter import tk_interface

from .widgets import Spacer
from .widgets import Widget


class Stacker:
    _id = 0
    _v_direction = 'vertical'
    _h_direction = 'horizontal'

    def __init__(self):
        self._parent = 'root'  # Default Parent

        self._id = Stacker._id
        self._frame_id = f'frame_{self._id}'
        Stacker._id += 1

        self._row = 0
        self._col = 0
        self._frame_options = {}
        self._static_kwargs = {'widget_type': 'frame', 'sticky': 'nsew'}
        self._children_stackers: List[Stacker] = []
        self._view_model = []

        self._flag_already_inserted_frame = False

        self._level = 0
        self._frame_to_stacker_dictionary = {}

    def set_row(self, row):
        self._row = row

    def set_col(self, col):
        self._col = col

    def set_parent(self, parent_id):
        self._parent = parent_id

    def hstack(self, *widgets: Union[Widget, Spacer, 'Stacker']):
        new_stacker = self.register_widgets(self._h_direction, widgets)
        return new_stacker

    def vstack(self, *widgets: Union[Widget, Spacer, 'Stacker']):
        new_stacker = self.register_widgets(self._v_direction, widgets)
        return new_stacker

    def register_widgets(self, direction, widgets):
        f = tk_interface.widget_model
        fr_options = tk_interface.frame_options

        new_stacker = Stacker()
        self._frame_to_stacker_dictionary[new_stacker._frame_id] = new_stacker
        self._children_stackers.append(new_stacker)
        frame_id = new_stacker._frame_id

        sticky = 'nsew'
        space = []
        for n, widget in enumerate(widgets):
            w = widget
            if widget.__class__ == Spacer:
                if direction == new_stacker._v_direction:
                    space.append(n)
                else:
                    space.append(n)

            if direction == new_stacker._v_direction:
                row, col = n, 0
            else:
                row, col = 0, n

            if widget.__class__ == Stacker:
                # "I am your father"
                child_stacker: Stacker = widget
                new_stacker._children_stackers.append(child_stacker)
                child_stacker.set_parent(frame_id)
                child_stacker.set_row(row)
                child_stacker.set_col(col)
                child_stacker.increment_level()
            else:
                w: Widget = w
                widget_model = f(frame_id, w.id, w.widget_type, row, row, col, col, sticky, w.pad_xy, **w.options)
                new_stacker._view_model.append(widget_model)

        # Insert Frame
        if not space:
            space = [0]
        if direction == new_stacker._v_direction:
            row_space, col_space = space, [0]
        else:
            row_space, col_space = [0], space
        rows_and_weights = tuple(row_space), tuple(1 for _ in row_space)
        cols_and_weights = tuple(col_space), tuple(1 for _ in col_space)
        new_stacker._frame_options = fr_options(rows_and_weights, cols_and_weights, )
        return new_stacker

    def increment_level(self):
        self._level += 1
        for child_stacker in self._children_stackers:
            child_stacker.increment_level()

    def _combine_view_models(self):
        combined_view_model = []
        for stacker in self._children_stackers:
            combined_view_model += stacker._view_model
        self._view_model = combined_view_model

    def insert_frames(self):
        if self._flag_already_inserted_frame:
            return

        # Sort Stackers cleverly to make sure tab order is as intended.
        sorted_frames: Dict[int, list] = {}
        for child_stacker in self._children_stackers:
            level = child_stacker._level
            frame_id = child_stacker._frame_id
            if level in sorted_frames:
                sorted_frames[level].insert(0, frame_id)
            else:
                sorted_frames[level] = [frame_id]

        # for child_stacker in reversed(self._children_stackers):
        for level in sorted_frames.keys():
            frame_ids = sorted_frames.get(level)
            for frame_id in frame_ids:
                child_stacker: Stacker = self._frame_to_stacker_dictionary.get(frame_id)
                frame_id = child_stacker._frame_id
                frame_parent = child_stacker._parent
                frame_options_ = child_stacker._frame_options
                row1 = child_stacker._row
                row2 = child_stacker._row
                col1 = child_stacker._col
                col2 = child_stacker._col
                static_kwargs = child_stacker._static_kwargs

                kwargs = {}
                kwargs.update(static_kwargs)
                kwargs.update({'parent_id': frame_parent, 'widget_id': frame_id})
                kwargs.update({'row1': row1, 'row2': row2})
                kwargs.update({'col1': col1, 'col2': col2})
                kwargs.update(frame_options_)

                frame = tk_interface.widget_model(**kwargs)
                self._view_model.insert(0, frame)

        self._flag_already_inserted_frame = True

    @property
    def view_model(self) -> list:
        self._combine_view_models()
        self.insert_frames()
        return self._view_model
