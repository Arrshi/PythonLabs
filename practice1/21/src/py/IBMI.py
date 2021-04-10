from abc import abstractmethod, ABC


class IBMI(ABC):

    @abstractmethod
    def bmi(self, weight: float, height: float) -> float:
        pass

    @abstractmethod
    def print_bmi(self, bmi: float):
        pass
