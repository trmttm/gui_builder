import abc
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
        return self.set_options('width', width)

    def height(self, height: int):
        return self.set_options('height', height)

    def set_options(self, option, value):
        self._options[option] = value
        return self


class Spacer(Widget, SpacerABC):
    def __init__(self):
        Widget.__init__(self, 'spacer')
        self._options['text'] = ''
        self.width(0)
        self._data = {'adjustment': 0}

    def adjust(self, n):
        self._data['adjustment'] = n
        return self

    @property
    def adjustment(self) -> int:
        return self._data['adjustment']


class WidgetWithText(Widget):
    def text(self, text: str) -> 'WidgetWithText':
        return self.set_options('text', text)


class Label(WidgetWithText):
    def align(self, nsew: str):
        return self.set_options('anchor', nsew)


class Button(WidgetWithText):
    def command(self, command) -> 'Button':
        return self.set_options('command', command)

    def wh_padding(self, w, n, s, e):
        return self.set_options('padding', (w, n, e, s))


class Entry(Widget):
    def default_value(self, default_value) -> 'Entry':
        return self.set_options('default_value', default_value)


class WidgetSpecialFrameHolder(Widget):
    @abc.abstractmethod
    def stackers(self, *stackers: StackerABC):
        pass


class PanedWindow(WidgetSpecialFrameHolder):
    _is_vertical = 'is_vertical'

    def __init__(self, widget_id: str, stacker: StackerABC):
        Widget.__init__(self, widget_id)
        self._options = {
            self._is_vertical: True,
            'frame_ids': (),
            'weights': (),
        }
        self._stacker = stacker

    def is_vertical(self):
        return self.set_options(self._is_vertical, True)

    def is_horizontal(self):
        self._options[self._is_vertical] = False
        return self

    def weights(self, weights: tuple):
        return self.set_options('weights', weights)

    def stackers(self, *stackers: StackerABC):
        for n, stacker in enumerate(stackers):
            if self._is_vertical:
                row, col = n, 0
            else:
                row, col = 0, n

            if not issubclass(stacker.__class__, StackerABC):
                # widget is directly passed. wrap the widget with stacker
                stacker = self._stacker.hstack(stacker)
            configure_child_stacker(stacker, self.id, row, col)

            self._options['frame_ids'] += (stacker.frame_id,)
            self._options['weights'] += (1,)  # default weight = 1
        return self


class NoteBook(WidgetSpecialFrameHolder):
    def __init__(self, widget_id: str, stacker):
        Widget.__init__(self, widget_id)
        self._options = {
            'frame_ids': (),
            'frame_names': (),
        }
        self._stacker = stacker

    def stackers(self, *stackers: StackerABC):
        for n, stacker in enumerate(stackers):
            if not issubclass(stacker.__class__, StackerABC):
                # widget is directly passed. wrap the widget with stacker
                stacker = self._stacker.hstack(stacker)
            configure_child_stacker(stacker, self.id, 0, 0)
            self._options['frame_ids'] += (stacker.frame_id,)
        return self

    def frame_names(self, frame_names: tuple):
        return self.set_options('frame_names', frame_names)


class FrameSwitcher(Widget):
    def __init__(self, widget_id: str, stacker, switchable_frames_pass_me_an_empty_frame: list):
        Widget.__init__(self, widget_id)
        self._options = {
            'frame options': {'rows_and_weights': ((0,), (1,)),
                              'cols_and_weights': ((0,), (1,)),
                              'propagate': True}}
        self._stacker = stacker
        self._switchable_frames = switchable_frames_pass_me_an_empty_frame

    def stackers(self, *stackers: StackerABC):
        for n, stacker in enumerate(stackers):
            if not issubclass(stacker.__class__, StackerABC):
                # widget is directly passed. wrap the widget with stacker
                stacker = self._stacker.hstack(stacker)

            self._switchable_frames.append(stacker.frame_id)
            configure_child_stacker(stacker, self.id, 0, 0)
            stacker.set_row(0)
            stacker.set_col(0)
        return self


class Canvas(Widget):
    def color(self, color: str):
        return self.set_options('bg', color)


class TreeView(Widget):
    pass


class TextBox(Widget):
    def back_ground_color(self, color):
        return self.set_options('bg', color)

    def text_color(self, color):
        return self.set_options('fg', color)

    def cursor_color(self, color):
        return self.set_options('insertbackground', color)

    def select_color(self, color):
        return self.set_options('selectbackground', color)

    def border_width(self, width):
        return self.set_options('bd', width)


class RadioButton(Widget):
    _is_vertical = 'is_vertical'

    def __init__(self, widget_id: str):
        Widget.__init__(self, widget_id)
        self._options = {
            self._is_vertical: True,
            'int_var_id': f'int_var_{self._id}',
            'frame_id': f'frame_{self._id}',
            'names': (),
        }

    def is_vertical(self):
        return self.set_options(self._is_vertical, True)

    def is_horizontal(self):
        self._options[self._is_vertical] = False
        return self

    def frame_id(self, frame_id: str):
        return self.set_options('frame_id', frame_id)

    def int_var_id(self, int_var_id: str):
        return self.set_options('int_var_id', int_var_id)

    def names(self, names: tuple):
        return self.set_options('names', names)


class CheckButton(Widget):
    def value(self, value: bool):
        return self.set_options('value', value)


class ComboBox(Widget):
    def values(self, values: tuple):
        return self.set_options('value', values)

    def widths(self, widths: tuple):
        return self.set_options('widths', widths)


widget_dictionary = {
    Label: 'label',
    Button: 'button',
    Entry: 'entry',
    Spacer: 'label',
    PanedWindow: 'paned_window',
    Canvas: 'canvas',
    NoteBook: 'notebook',
    TreeView: 'treeview',
    TextBox: 'text',
    RadioButton: 'radio_button',
    CheckButton: 'check_button',
    ComboBox: 'combo_box',
    FrameSwitcher: 'frame',
}
