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
        self._id = Stacker._id
        Stacker._id += 1
        self._parent = 'root'
        self._frame_id = ''
        self._row = 0
        self._col = 0
        self._frame_options = {}
        self._static_kwargs = {'widget_type': 'frame', 'sticky': 'nsew'}
        self._children_stackers: List[Stacker] = []
        self._view_model = []

        self._flag_already_inserted_frame = False

    @property
    def parent(self):
        return self._parent

    @property
    def frame_id(self):
        return self._frame_id

    @property
    def row(self, ):
        return self._row

    @property
    def col(self, ):
        return self._col

    @property
    def static_kwargs(self) -> dict:
        return self._static_kwargs

    @property
    def frame_options(self):
        return self._frame_options

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
        self._children_stackers.append(new_stacker)
        new_stacker._frame_id = frame_id = f'frame_{new_stacker._id}'
        new_stacker._id += 1

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
            else:
                widget_model = f(frame_id, w.id, w.widget_type, row, row, col, col, sticky, w.pad_xy, **w.options)
                new_stacker._view_model.append(widget_model)

        # Insert Frame
        if direction == new_stacker._v_direction:
            row_space, col_space = space, []
        else:
            row_space, col_space = [], space
        rows_and_weights = tuple(row_space), tuple(1 for _ in row_space)
        cols_and_weights = tuple(col_space), tuple(1 for _ in col_space)
        new_stacker._frame_options = fr_options(rows_and_weights, cols_and_weights, )
        return new_stacker

    def insert_frames(self):
        if self._flag_already_inserted_frame:
            return

        for child_stacker in self._children_stackers:
            frame_id = child_stacker.frame_id
            frame_parent = child_stacker.parent
            frame_options_ = child_stacker._frame_options
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
            self._view_model.insert(0, frame)

        self._flag_already_inserted_frame = True

    @property
    def view_model(self) -> list:
        self._combine_view_models()
        self.insert_frames()
        return self._view_model

    def _combine_view_models(self):
        combined_view_model = []
        for stacker in self._children_stackers:
            combined_view_model += stacker._view_model
        self._view_model = combined_view_model
