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
    """summary
    Description:
        첨가물을 나타내는 추상클래스
    """

    def __init__(self, bevarage: Beverage) -> None:
        """상속받는 클래스에 따라 구현

        Args:
            None

        Returns:
            None
        """
        super().__init__()
        self._beverage = bevarage

    @property
    def beverage(self) -> Beverage:
        """summary
        Description:
            상속받는 클래스에 따라 구현

            Args:
                None

            Returns:
                None
        """
        return self._beverage

    def get_description(self) -> Any:
        """summary
        Description:
            상속받는 클래스에 따라 Beverage의 이름 출력 구현

            Args:
                None

            Returns:
                None
        """
        return self._beverage.getdescription()

    def cost(self) -> Any:
        """summary
        Description:
            상속받는 클래스에 따라 Beverage의 가격 출력 구현

            Args:
                None

            Returns:
                None
        """
        return self._beverage.cost()


class Mocha(CondimentDecorator):
    """summary
    Description:
        Mocha를 나타내는 클래스
    """

    def get_description(self) -> Any:
        """summary
        Description:
            설명을 덧붙이는 함수
        """
        return self.beverage.getdescription() + ", 모카"

    def cost(self) -> Any:
        """summary
        Description:
            cost 계산시 0.2를 더해준다.
        """
        return self.beverage.cost() + 0.20
