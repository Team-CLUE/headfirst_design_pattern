"""
    피자 가게 클래스

    Description:
        피자 가게에 필요한 함수를 정의해둔 클래스

    Author:
        Name: Junhyeok Yang
        Email: surfing2003@naver.com
"""
from pizza import Pizza
from simplepizzafactory import SimplePizzaFactory


class PizzaStore:  # pylint: disable=too-few-public-methods
    """
    Description:
        피자 가게를 구현하기 위한 클래스
    """

    def __init__(self, factory: SimplePizzaFactory) -> None:
        """
        피자 가게 생성 시에 simple pizza factory를 지정한다.

        Args:
            factory (SimplePizzaFactory): 사용할 피자 팩토리
        Returns:
            None
        """
        self._simple_pizza_factory = factory

    def order_pizza(self, category: str) -> Pizza:
        """
        원하는 피자를 주문하는 함수

        Args:
            category (str): 주문을 원하는 카테고리
        Returns:
            pizza (Pizza): 입력된 카테고리에 해당하는 피자
        """
        pizza = self._simple_pizza_factory.create_pizza(category)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza
