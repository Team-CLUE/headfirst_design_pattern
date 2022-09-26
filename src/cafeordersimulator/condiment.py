"""
각종 음료 관련 코드

Description:
    추상클래스 Beverage를 상속받아, Espresso, HouseBlend 구현

Author:
    Name: Gangmin Kim
    Email: rlarkdals7@gmail.com
"""
from typing import Any

from beverage import Beverage


class CondimentDecorator(Beverage):
    """
    Description:
        첨가물을 나타내는 추상클래스
    """

    def __init__(self, bevarage: Beverage) -> None:
        super().__init__()
        self._beverage = bevarage

    @property
    def beverage(self) -> Beverage:
        """
        Description:
            상속받는 클래스에 따라 구현

        Returns:
            beverage
        """
        return self._beverage

    def get_description(self) -> Any:
        """
        Description:
            상속받는 클래스에 따라 Beverage의 이름 출력 구현

        Returns:
            beverage.get_description
        """
        return self._beverage.get_description()

    def get_size(self) -> Any:
        """
        Description:
            상속받는 클래스에 따라 Beverage의 사이즈 출력 구현

        Returns:
            beverage.get_size
        """
        return self._beverage.get_size()

    def cost(self) -> Any:
        """
        Description:
            상속받는 클래스에 따라 Beverage의 가격 출력 구현

            Args:
                None

            Returns:
                beverage.cost
        """
        return self._beverage.cost()


class Mocha(CondimentDecorator):
    """
    Description:
        Mocha를 나타내는 클래스
    """

    # def __init__(self, bevarage: Beverage) -> None:
    #     super().__init__()
    #     self._beverage = bevarage

    def get_description(self) -> Any:
        """
        Description:
            설명을 덧붙이는 함수

        Returns:
            beverage의 이름 + ", 모카"
        """
        return self._beverage.get_description() + ", 모카"

    def cost(self) -> Any:
        """
        Description:
            cost 계산시 size에 따라서 cost를 계산해준다.
        Returns:
            beverage cost + size depends cost
        """
        beverage_cost = self._beverage.cost()

        if self._beverage.get_size() == "tall":
            beverage_cost += 0.10
        elif self._beverage.get_size() == "grande":
            beverage_cost += 0.15
        elif self._beverage.get_size() == "venti":
            beverage_cost += 0.20
        return beverage_cost
