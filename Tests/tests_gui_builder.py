import unittest
from typing import Union

from view_tkinter import tk_interface

from stacker import Spacer
from stacker import Stacker
from stacker import Widget
from stacker.widgets import Button
from stacker.widgets import Entry
from stacker.widgets import Label


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


def launch_app(view_model):
    from view_tkinter import View
    app = View()
    app.add_widgets(view_model)
    app.launch_app()


class MyTestCase(unittest.TestCase):
    def test_vstacker(self):
        view_model = vstacker(
            Label('label_1').text('Name:').width(10),
            Entry('entry_1').default_value('Name').width(20),
            Button('button_1').text('Name').command(lambda: print('button pushed!')).width(15),
            Spacer(),
        )

        launch_app(view_model)

    def test_hstacker(self):
        view_model = hstacker(
            Label('label_1').text('Name:').width(10),
            Entry('entry_1').default_value('Name').width(20),
            Button('button_1').text('Name').command(lambda: print('button pushed!')).width(15),
            Spacer(),
        )

        launch_app(view_model)

    def test_combination_of_vstacker_and_hstacker(self):
        stacker = Stacker()

        stacker.hstack(
            stacker.vstack(
                stacker.hstack(
                    Label('label_0').text('Name1').width(10),
                    Entry('entry_0').default_value('First Last1').width(15),
                    Button('button_0').text('Add1').width(10).command(lambda: print('Pushed1'))
                ),
                stacker.hstack(
                    Label('label_1').text('Name2').width(10),
                    Entry('entry_1').default_value('First Last2').width(15),
                    Button('button_1').text('Add2').width(10).command(lambda: print('Pushed2'))
                ),
                stacker.hstack(
                    Label('label_2').text('Name3').width(10),
                    Entry('entry_2').default_value('First Last3').width(15),
                    Button('button_2').text('Add3').width(10).command(lambda: print('Pushed3'))
                ),
            ),
            stacker.vstack(
                stacker.hstack(
                    Label('label_3').text('Name a').width(10),
                    Entry('entry_3').default_value('First Last a').width(15),
                    Button('button_3').text('Add a').width(10).command(lambda: print('pushed a'))
                ),
                stacker.hstack(
                    Label('label_4').text('Name b').width(10),
                    Entry('entry_4').default_value('First Last b').width(15),
                    Button('button_4').text('Add b').width(10).command(lambda: print('pushed b'))
                ),
                stacker.hstack(
                    Label('label_5').text('Name c').width(10),
                    Entry('entry_5').default_value('First Last c').width(15),
                    Button('button_5').text('Add c').width(10).command(lambda: print('pushed c'))
                ),
            ),
        )

        launch_app(stacker.view_model)


if __name__ == '__main__':
    unittest.main()
