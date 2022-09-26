"""
각종 음료 관련 코드

Description:
    추상클래스 Beverage를 상속받아, Espresso, HouseBlend 구현

Author:
    Name: Gangmin Kim
    Email: rlarkdals7@gmail.com
"""
from abc import ABCMeta, abstractmethod


class Beverage(metaclass=ABCMeta):
    """
    Description:
        다양한 Beverage들을 구현하기 위한 Abstractive class
    """

    def __init__(self):
        self.size = "tall"

    def get_description(self) -> str:
        """
        Description:
            상속받는 클래스에 따라 Beverage의 이름 출력 구현
        """

    def set_size(self, size) -> str:
        """
        Description:
            Beverage의 사이즈 지정
        args :
            size : Beverage의 사이즈
        """
        self.size = size

    def get_size(self) -> str:
        """
        Description:
            Beverage의 사이즈 출력 구현
        """
        return self.size

    @abstractmethod
    def cost(self) -> float:
        """
        Description:
            상속받는 클래스에 따라 Beverage의 가격 출력 구현
        """


class Espresso(Beverage):
    """
    Description:
        Beverage 중 Espresso 클래스
    """

    def get_description(self) -> str:
        """Espresso 이름 출력 구현
        Returns: name of beverage
        """
        return "Espresso"

    def cost(self) -> float:
        """Espresso 가격 출력 구현
        Returns: cost of beverage
        """
        return 1.99


class HouseBlend(Beverage):
    """
    Description:
        Beverage 중 Espresso 클래스
    """

    def get_description(self) -> str:
        """Espresso 이름 출력 구현
        Returns: name of beverage
        """
        return "HouseBlend"

    def cost(self) -> float:
        """Espresso 가격 출력 구현
        Returns: cost of beverage
        """
        return 0.89
