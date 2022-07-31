"""
각종 음료 관련 코드

Description:
    추상클래스 Beverage를 상속받아, Espresso, HouseBlend 구현

Author:
    Name: Gangmin Kim
    Email: rlarkdals7@gmail.com
"""
from abc import abstractmethod
from typing import Any


class Beverage:
    """summary
    Description:
        다양한 Beverage들을 구현하기 위한 Abstractive class
    """

    @abstractmethod
    def __init__(self) -> None:
        """상속받는 클래스에 따라 Description 구현

        Args:
            None

        Returns:
            None
        """
        self.description = "제목 없음"

    @abstractmethod
    def getdescription(self) -> str:
        """상속받는 클래스에 따라 Beverage의 이름 출력 구현

        Args:
            None

        Returns:
            None
        """
        return self.description

    @abstractmethod
    def cost(self) -> Any:
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

    def __init__(self) -> None:
        """상속받는 클래스에 따라 Description 구현

        Args:
            None

        Returns:
            None
        """
        super().__init__()
        self.description = "Espresso"

    def getdescription(self) -> str:
        """Espresso 이름 출력 구현

        Args:
            None

        Returns:
            None
        """
        return self.description

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

    def __init__(self) -> None:
        """상속받는 클래스에 따라 Description 구현

        Args:
            None

        Returns:
            None
        """
        super().__init__()
        self.description = "HouseBlend"

    def getdescription(self) -> str:
        """Espresso 이름 출력 구현

        Args:
            None

        Returns:
            description
        """
        return self.description

    def cost(self) -> float:
        """Espresso 가격 출력 구현

        Args:
            None

        Returns:
            cost
        """
        return 0.89
