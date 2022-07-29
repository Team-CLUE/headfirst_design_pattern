"""
    카페인 음료 클래스
    Description:
        카페인 음료 생성 템플릿을 가지고 있는 클래스
    Author:
        Name: Junhyeok Yang
        Email: surfing2003@naver.com
"""
from abc import ABC, abstractmethod
from typing import final


class CaffeineBeverage(ABC):
    """
    Description:
        카페인 생성의 기본이 되는 추상 클래스
    """

    @final
    def prepare_recipe(self) -> None:
        """
        템플릿 역할을 하는 함수로 해당 클래스에 정의된 함수 외에
        서브 클래스에서 선언될 함수의 순서를 가지고 있는 함수

        Args:
            None
        Returns:
            None
        """
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    @classmethod
    def boil_water(cls) -> None:
        """
        카페인 음료에 필요한 물을 끓이는 함수

        Args:
            None
        Returns:
            None
        """
        print("물을 끓인다.")

    @classmethod
    def pour_in_cup(cls) -> None:
        """
        카페인 음료를 컵에 따르는 함수

        Args:
            None
        Returns:
            None
        """
        print("음료를 컵에 따른다.")

    @abstractmethod
    def brew(self) -> None:
        """
        서브 클래스에 따라 바뀌는 함수

        Args:
            None
        Returns:
            None
        """

    @abstractmethod
    def add_condiments(self) -> None:
        """
        서브 클래스에 따라 바뀌는 함수

        Args:
            None
        Returns:
            None
        """
