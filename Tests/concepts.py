from typing import Union

from view_tkinter import tk_interface

from stacker.widgets import Spacer
from stacker.widgets import Widget


def vstacker(*widgets: Union[Widget, Spacer, list]) -> list:
    view_model = []
    parent_id = f'frame_p'
    frame_row = 0
    frame_col = 0
    col = 0
    sticky = 'nsew'

    row_space = []
    for row, widget in enumerate(widgets):
        if type(widget) == list:
            view_model += widget
        else:
            w = widget
            if widget.__class__ == Spacer:
                row_space.append(row)
            view_model.append(tk_interface.widget_model(parent_id,
                                                        w.id,
                                                        w.widget_type,
                                                        row,
                                                        row,
                                                        col,
                                                        col,
                                                        sticky,
                                                        w.pad_xy,
                                                        **w.options))

    rows_and_weights = tuple(row_space), tuple(1 for _ in row_space)
    cols_and_weights = ((), ())
    frame = tk_interface.widget_model('root', parent_id, 'frame', frame_row, frame_row, frame_col, frame_col, 'nsew',
                                      **tk_interface.frame_options(
                                          rows_and_weights,
                                          cols_and_weights,
                                      ))
    view_model.insert(0, frame)
    return view_model


def hstacker(*widgets: Union[Widget, Spacer, list]) -> list:
    view_model = []
    parent_id = f'frame_p'
    frame_row = 0
    frame_col = 0
    row = 0
    sticky = 'nsew'

    columns_space = []
    for col, widget in enumerate(widgets):
        if type(widget) == list:
            view_model += widget
        else:
            w = widget
            if widget.__class__ == Spacer:
                columns_space.append(col)
            view_model.append(tk_interface.widget_model(parent_id,
                                                        w.id,
                                                        w.widget_type,
                                                        row,
                                                        row,
                                                        col,
                                                        col,
                                                        sticky,
                                                        w.pad_xy,
                                                        **w.options))

    rows_and_weights = ((), ())
    cols_and_weights = tuple(columns_space), tuple(1 for _ in columns_space)
    frame = tk_interface.widget_model('root', parent_id, 'frame', frame_row, frame_row, frame_col, frame_col, 'nsew',
                                      **tk_interface.frame_options(
                                          rows_and_weights,
                                          cols_and_weights,
                                      ))
    view_model.insert(0, frame)
    return view_model
