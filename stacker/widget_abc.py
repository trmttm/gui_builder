import abc


class WidgetABC(abc.ABC):
    @property
    @abc.abstractmethod
    def id(self):
        pass

    @property
    @abc.abstractmethod
    def widget_type(self):
        pass

    @property
    @abc.abstractmethod
    def pad_xy(self):
        pass

    @property
    @abc.abstractmethod
    def options(self):
        pass
