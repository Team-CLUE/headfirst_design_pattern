"""
    피자 가게 클래스

    Description:
        피자 가게에 필요한 함수를 정의해둔 클래스

    Author:
        Name: Junhyeok Yang
        Email: surfing2003@naver.com
"""
from abc import ABC, abstractmethod

from pizza import BasePizza, ChicagoCheesePizza, NYCheesePizza, Pizza


class PizzaStore(ABC):  # pylint: disable=too-few-public-methods
    """
    Description:
        피자 가게를 구현하기 위한 클래스
    """

    def __init__(self) -> None:
        """
        pizza store init

        Args:
            None
        Returns:
            None
        """

    def order_pizza(self, category: str) -> Pizza:
        """
        원하는 피자를 주문하는 함수

        Args:
            category (str): 주문을 원하는 카테고리
        Returns:
            pizza (Pizza): 입력된 카테고리에 해당하는 피자
        """
        pizza = self.create_pizza(category)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    @abstractmethod
    def create_pizza(self, category: str) -> Pizza:
        """
        pizzastore class를 상속받는 클래스 별로 정의하여 사용

        Args:
            category (str): 원하는 종류를 입력받는 변수
        Returns:
            None
        """


class NYPizzaStore(PizzaStore):
    """
    Description:
        PizzaStore를 상속받아 만든 클래스
    """

    def create_pizza(self, category: str) -> Pizza:
        """
        pizzastore class를 상속받는 클래스로 해당 지점에 Pizza를 리턴

        Args:
            category (str): 원하는 종류를 입력받는 변수
        Returns:
            None
        """
        if category == "cheese":
            return NYCheesePizza()
        return BasePizza()


class ChicagoPizzaStore(PizzaStore):
    """
    Description:
        PizzaStore를 상속받아 만든 클래스
    """

    def create_pizza(self, category: str) -> Pizza:
        """
        pizzastore class를 상속받는 클래스로 해당 지점에 Pizza를 리턴

        Args:
            category (str): 원하는 종류를 입력받는 변수
        Returns:
            None
        """
        if category == "cheese":
            return ChicagoCheesePizza()
        return BasePizza()
