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
    """summary
    Description:
        다양한 Beverage들을 구현하기 위한 Abstractive class
    """

    def get_description(self) -> str:
        """상속받는 클래스에 따라 Beverage의 이름 출력 구현

        Args:
            None

        Returns:
            None
        """

    @abstractmethod
    def cost(self) -> float:
        """상속받는 클래스에 따라 Beverage의 가격 출력 구현

        Args:
            None

        Returns:
            None
        """


class Espresso(Beverage):
    """summary
    Description:
        Beverage 중 Espresso 클래스
    """

    def get_description(self) -> str:
        """Espresso 이름 출력 구현

        Args:
            None

        Returns:
            None
        """
        return "Espresso"

    def cost(self) -> float:
        """Espresso 가격 출력 구현

        Args:
            None

        Returns:
            None
        """
        return 1.99


class HouseBlend(Beverage):
    """summary
    Description:
        Beverage 중 Espresso 클래스
    """

    def get_description(self) -> str:
        """Espresso 이름 출력 구현

        Args:
            None

        Returns:
            description
        """
        return "HouseBlend"

    def cost(self) -> float:
        """Espresso 가격 출력 구현

        Args:
            None

        Returns:
            cost
        """
        return 0.89
