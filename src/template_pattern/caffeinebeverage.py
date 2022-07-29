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
        카페인 음료 생성의 기본이 되는 추상 클래스
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
        if self.customer_wants_condiments():
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

    @classmethod
    def customer_wants_condiments(cls) -> bool:
        """
        hook 역할 함수

        Args:
            None
        Returns:
            (bool): True or False
        """
        return True

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


class Tea(CaffeineBeverage):
    """
    Description:
        추상 클래스를 바탕으로 생성한 서브 클래스
    """

    def brew(self) -> None:
        """
        홍차(서브클래스)에 맞는 함수 생성

        Args:
            None
        Returns:
            None
        """
        print("찻잎을 우려낸다.")

    def add_condiments(self) -> None:
        """
        홍차(서브클래스)에 맞는 함수 생성

        Args:
            None
        Returns:
            None
        """
        print("레몬을 추가한다.")

    @classmethod
    def customer_wants_condiments(cls) -> bool:
        """
        사용자의 입력을 바탕으로 참 또는 거짓을 반환하는 함수

        Args:
            None
        Returns:
            (bool): True or False
        """
        answer = input("차에 레몬을 넣을까요? (y/n)")

        if answer == "y":
            return True

        return False


class Coffee(CaffeineBeverage):
    """
    Description:
        추상 클래스를 바탕으로 생성한 서브 클래스
    """

    def brew(self) -> None:
        """
        커피(서브 클래스)에 맞는 함수 생성

        Args:
            None
        Returns:
            None
        """
        print("커피를 우려낸다.")

    def add_condiments(self) -> None:
        """
        커피(서브 클래스)에 맞는 함수 생성

        Args:
            None
        Returns:
            None
        """
        print("설탕과 우유를 추가한다.")

    @classmethod
    def customer_wants_condiments(cls) -> bool:
        """
        사용자의 입력을 바탕으로 참 또는 거짓을 반환하는 함수

        Args:
            None
        Returns:
            (bool): True or False
        """
        answer = input("커피에 우유와 설탕을 넣을까요? (y/n)")

        if answer == "y":
            return True

        return False
