from typing import Tuple

from .. import StackerABC
from ..implementation import configure_child_stacker
from ..spacer_abc import SpacerABC
from ..widget_abc import WidgetABC


class Widget(WidgetABC):
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


class Spacer(Widget, SpacerABC):
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


class PanedWindow(Widget):
    _is_vertical = 'is_vertical'

    def __init__(self, widget_id: str):
        Widget.__init__(self, widget_id)
        self._options = {
            self._is_vertical: True,
            'frame_ids': (),
            'weights': (),
        }

    def is_vertical(self):
        self._options[self._is_vertical] = True
        return self

    def is_horizontal(self):
        self._options[self._is_vertical] = False
        return self

    def weights(self, weights: tuple):
        self._options['weights'] = weights
        return self

    def stackers(self, *stackers: StackerABC):
        for n, stacker in enumerate(stackers):
            if self._is_vertical:
                row, col = n, 0
            else:
                row, col = 0, n
            configure_child_stacker(stacker, self.id, row, col)

            self._options['frame_ids'] += (stacker.frame_id,)
            self._options['weights'] += (1,)  # default weight = 1
        return self


widget_dictionary = {
    Label: 'label',
    Button: 'button',
    Entry: 'entry',
    Spacer: 'label',
    PanedWindow: 'paned_window',
}
