from typing import List
from typing import Union

from stacker.spacer_abc import SpacerABC
from stacker.widget_abc import WidgetABC

from . import handle_other_frame_holders
from . import implementation
from .stacker_abc import StackerABC


class Stacker(StackerABC):
    _id = 0
    _v_direction = 'vertical'
    _h_direction = 'horizontal'

    def __init__(self, specified_parent=None, scrollable=False):
        self._parent = specified_parent or 'root'  # Default Parent

        self._id = Stacker._id
        self._frame_id = f'frame_{self._id}'
        Stacker._id += 1

        self._row = 0
        self._col = 0
        self._frame_options = {}
        frame_type = 'frame' if not scrollable else 'scrollable_frame'
        self._static_kwargs = {'widget_type': frame_type, 'sticky': 'nsew'}
        self._children_stackers: List[Stacker] = []
        self._view_model = []

        self._flag_already_inserted_frame = False

        self._level = 0
        self._frame_to_stacker_dictionary = {}

    def set_frame_id(self, frame_id):
        self._frame_id = frame_id

    @property
    def v_direction(self):
        return self._v_direction

    @property
    def frame_options(self):
        return self._frame_options

    @property
    def children_stackers(self) -> List['Stacker']:
        return self._children_stackers

    @property
    def frame_id(self):
        return self._frame_id

    @property
    def increment_level(self):
        return self._increment_level

    @property
    def level(self):
        return self._level

    @property
    def parent(self):
        return self._parent

    @property
    def row(self):
        return self._row

    @property
    def col(self):
        return self._col

    @property
    def static_kwargs(self):
        return self._static_kwargs

    def add_widget_model(self, widget_model):
        self._view_model.append(widget_model)

    def set_frame_options(self, frame_options):
        self._frame_options = frame_options

    def set_row(self, row):
        self._row = row

    def set_col(self, col):
        self._col = col

    def set_parent(self, parent_id):
        self._parent = parent_id

    def hstack(self, *elements: Union[WidgetABC, SpacerABC, 'Stacker']) -> StackerABC:
        new_stacker = self._register_spacer_widget_or_stacker(self._h_direction, elements)
        return new_stacker

    def vstack(self, *elements: Union[WidgetABC, SpacerABC, 'Stacker']) -> StackerABC:
        new_stacker = self._register_spacer_widget_or_stacker(self._v_direction, elements)
        return new_stacker

    def hstack_scrollable(self, *elements: Union[WidgetABC, SpacerABC, 'Stacker']) -> StackerABC:
        new_stacker = self._register_spacer_widget_or_stacker_scrollable(self._h_direction, elements)
        return new_stacker

    def vstack_scrollable(self, *elements: Union[WidgetABC, SpacerABC, 'Stacker']) -> StackerABC:
        new_stacker = self._register_spacer_widget_or_stacker_scrollable(self._v_direction, elements)
        return new_stacker

    def _register_spacer_widget_or_stacker(self, direction, elements) -> StackerABC:
        new_stacker = self._instantiate_and_link_new_stacker()
        return implementation.register_spacer_widget_or_stacker(direction, elements, new_stacker)

    def _register_spacer_widget_or_stacker_scrollable(self, direction, elements) -> StackerABC:
        new_stacker = self._instantiate_and_link_new_stacker_scrollable()
        return implementation.register_spacer_widget_or_stacker(direction, elements, new_stacker)

    def _instantiate_and_link_new_stacker(self) -> 'Stacker':
        new_stacker = Stacker(self._parent)
        return self._link_new_stacker(new_stacker)

    def _instantiate_and_link_new_stacker_scrollable(self) -> 'Stacker':
        new_stacker = Stacker(self._parent, True)
        return self._link_new_stacker(new_stacker)

    def _link_new_stacker(self, new_stacker):
        self._frame_to_stacker_dictionary[new_stacker._frame_id] = new_stacker
        self._children_stackers.append(new_stacker)
        return new_stacker

    def _increment_level(self):
        self._level += 1
        for child_stacker in self._children_stackers:
            child_stacker._increment_level()

    def _combine_view_models(self):
        combined_view_model = []
        for stacker in self._children_stackers:
            combined_view_model += stacker._view_model
        self._view_model = combined_view_model

    def _insert_frames(self):
        sorted_frames = implementation.get_sorted_frames(self._children_stackers)
        self._insert_frames_to_view_model(sorted_frames)

    def _insert_frames_to_view_model(self, sorted_frames: dict):
        for level in tuple(reversed(sorted(sorted_frames.keys()))):
            frame_ids = sorted_frames.get(level)
            for frame_id in frame_ids:
                frozen_frame = implementation.freeze_frame(frame_id, self._frame_to_stacker_dictionary)
                self._view_model.insert(0, frozen_frame)

    @property
    def view_model(self) -> list:
        if not self._flag_already_inserted_frame:
            self._combine_view_models()
            self._insert_frames()
            self._view_model = handle_other_frame_holders.sort_view_model_for_paned_window(self._view_model)
            self._flag_already_inserted_frame = True
        return self._view_model
