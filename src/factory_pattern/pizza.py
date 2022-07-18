"""
피자 추상 클래스

Description:
    피자 기본 정보를 담고 있는 추상 클래스

Author:
    Name: Junhyeok Yang
    Email: surfing2003@naver.com
"""

from abc import abstractmethod
from typing import List


class Pizza:
    """
    Description:
        다양한 Pizza를 구현하는데 활용하기 위한 추상 클래스
    """

    @abstractmethod
    def __init__(self) -> None:
        self._name: str = ""
        self._dough: str = ""
        self._sauce: str = ""
        self._toppings: List[str] = []

    def get_name(self) -> str:
        """
        실제로 생성된 클래스의 피자 이름을 출력하는 함수

        Args:
            None
        Returns:
            _name (str): 생성된 클래스의 피자 이름
        """
        return self._name

    def get_toppings(self) -> str:
        """
        실제로 생성된 클래스의 피자 토핑을 출력하는 함수

        Args:
            None
        Returns:
            _toppings (str): 생성된 클래스의 피자 토핑
        """
        return " ".join(self._toppings)

    def prepare(self) -> None:
        """
        피자 준비 과정 함수

        Args:
            None
        Returns:
            None
        """
        print(f"피자 준비중: {self.get_name()}")
        print("도우를 돌리는 중")
        print("소스를 뿌리는 중")
        print(f"토핑을 올리는 중: {self.get_toppings()}")

    @classmethod
    def bake(cls) -> None:
        """
        피자 굽기 과정 함수

        Args:
            None
        Returns:
            None
        """
        print("175도에서 25분간 굽기")

    @classmethod
    def cut(cls) -> None:
        """
        피자 자르기 과정 함수

        Args:
            None
        Returns:
            None
        """
        print("피자를 사선으로 자르기")

    @classmethod
    def box(cls) -> None:
        """
        피자 포장 과정 함수

        Args:
            None
        Returns:
            None
        """
        print("상자에 피자 담기")
