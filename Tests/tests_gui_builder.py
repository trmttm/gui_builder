import unittest
from typing import Tuple
from typing import Union

from view_tkinter import tk_interface


class Widget:
    def __init__(self, widget_id: str):
        self._id = widget_id
        self._pad_xy = (0, 0)
        self._options = {}

    @property
    def id(self):
        return self._id

    @property
    def widget_type(self) -> str:
        return widget_dictionary.get(self.__class__)

    @property
    def options(self) -> dict:
        return self._options

    @property
    def pad_xy(self) -> Tuple[int, int]:
        return self._pad_xy

    def padding(self, x, y):
        self._pad_xy = x, y
        return self

    def width(self, width: int):
        self._options['width'] = width
        return self

    def height(self, height: int):
        self._options['height'] = height
        return self


class Spacer(Widget):
    def __init__(self):
        Widget.__init__(self, 'spacer')
        self._options['text'] = ''
        self.width(0)


class WidgetWithText(Widget):
    def text(self, text: str) -> 'WidgetWithText':
        self._options['text'] = text
        return self


class Label(WidgetWithText):
    pass


class Button(WidgetWithText):
    def command(self, command) -> 'Button':
        self._options['command'] = command
        return self


class Entry(Widget):
    def default_value(self, value) -> 'Entry':
        self._options['default_value'] = value
        return self


def vstacker(*widgets: Union[Widget, Spacer]) -> list:
    view_model = []
    parent_id = 'frame_p'
    col = 0
    sticky = 'nsew'

    row_space = []
    for row, widget in enumerate(widgets):
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
    frame = tk_interface.widget_model('root', 'frame_p', 'frame', 0, 0, 0, 0, 'nsew',
                                      **tk_interface.frame_options(
                                          rows_and_weights,
                                          cols_and_weights,
                                      ))
    view_model.insert(0, frame)
    return view_model


def hstacker(*widgets: Union[Widget, Spacer]) -> list:
    view_model = []
    parent_id = 'frame_p'
    row = 0
    sticky = 'nsew'

    columns_space = []
    for col, widget in enumerate(widgets):
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
    frame = tk_interface.widget_model('root', 'frame_p', 'frame', 0, 0, 0, 0, 'nsew',
                                      **tk_interface.frame_options(
                                          rows_and_weights,
                                          cols_and_weights,
                                      ))
    view_model.insert(0, frame)
    return view_model


widget_dictionary = {
    Label: 'label',
    Button: 'button',
    Entry: 'entry',
    Spacer: 'label',
}


class MyTestCase(unittest.TestCase):
    def test_something(self):
        view_model = vstacker(
            Label('label_1').text('Name:').width(10),
            Entry('entry_1').default_value('Name').width(20),
            Button('button_1').text('Name').command(lambda: print('button pushed!')).width(15),
            Spacer(),
        )

        from view_tkinter import View
        app = View()
        app.add_widgets(view_model)

        app.launch_app()


if __name__ == '__main__':
    unittest.main()
