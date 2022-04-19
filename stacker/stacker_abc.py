import abc
from typing import List


class StackerABC(abc.ABC):
    @abc.abstractmethod
    def set_frame_id(self, frame_id):
        pass

    @abc.abstractmethod
    def hstack(self, *elements):
        pass

    @abc.abstractmethod
    def vstack(self, *elements):
        pass

    @abc.abstractmethod
    def hstack_scrollable(self, *elements):
        pass

    @abc.abstractmethod
    def vstack_scrollable(self, *elements):
        pass

    @property
    @abc.abstractmethod
    def v_direction(self):
        pass

    @abc.abstractmethod
    def add_widget_model(self, widget_model):
        pass

    @property
    @abc.abstractmethod
    def frame_options(self):
        pass

    @property
    @abc.abstractmethod
    def children_stackers(self) -> List['StackerABC']:
        pass

    @property
    @abc.abstractmethod
    def frame_id(self):
        pass

    @abc.abstractmethod
    def set_parent(self, prent_id):
        pass

    @abc.abstractmethod
    def set_row(self, row):
        pass

    @abc.abstractmethod
    def set_col(self, col):
        pass

    @property
    @abc.abstractmethod
    def increment_level(self):
        pass

    @property
    @abc.abstractmethod
    def level(self):
        pass

    @property
    @abc.abstractmethod
    def parent(self):
        pass

    @property
    @abc.abstractmethod
    def row(self):
        pass

    @property
    @abc.abstractmethod
    def col(self):
        pass

    @property
    @abc.abstractmethod
    def static_kwargs(self):
        pass

    @abc.abstractmethod
    def set_frame_options(self, frame_options):
        pass
