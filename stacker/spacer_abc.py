import abc


class SpacerABC(abc.ABC):
    @property
    @abc.abstractmethod
    def adjustment(self) -> int:
        pass
