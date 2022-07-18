"""
    피자 팩토리 클래스

    Description:
        피자 생성에 필요한 함수를 정의해둔 클래스

    Author:
        Name: Junhyeok Yang
        Email: surfing2003@naver.com
"""
from pizza import BasePizza, CheesePizza, ClamPizza, PepperoniPizza, Pizza, VeggiePizza


class SimplePizzaFactory:  # pylint: disable=too-few-public-methods
    """
    Description:
        피자 생성을 담당하는 factory 클래스
    """

    def __init__(self) -> None:
        pass

    @classmethod
    def create_pizza(cls, category: str) -> Pizza:
        """
        입력된 카테고리에 해당하는 피자를 생성하는 함수

        Args:
            category (str): 생성하길 원하는 카테고리
        Returns:
            pizza (Pizza): 입력된 카테고리에 해당하는 피자
        """
        if category == "cheese":
            return CheesePizza()
        if category == "pepperoni":
            return PepperoniPizza()
        if category == "clam":
            return ClamPizza()
        if category == "veggie":
            return VeggiePizza()

        return BasePizza()
