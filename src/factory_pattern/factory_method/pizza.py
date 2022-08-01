"""
    피자 클래스

    Description:
        피자 기본 정보를 담고 있는 클래스

    Author:
        Name: Junhyeok Yang
        Email: surfing2003@naver.com
"""
from abc import ABC, abstractmethod
from typing import List


class Pizza(ABC):
    """
    Description:
        다양한 피자를 구현하는데 활용하기 위한 클래스
    """

    @abstractmethod
    def __init__(self) -> None:
        """
        상속받는 클래스에 따라 행동 선택 구현

        Args:
            None
        Returns:
            None
        """
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
        print(f"토핑을 올리는 중: {' '.join(self._toppings)}")

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


class BasePizza(Pizza):
    """
    Description:
        Pizza 클래스를 활용해 만든 서브 클래스
    """

    def __init__(self) -> None:
        """
        서브 클래스에 따라 해당 값 입력

        Args:
            None
        Returns:
            None
        """
        super().__init__()
        self._name = "기본 피자"
        self._dough = "기본 도우"
        self._sauce = "기본 소스"
        self._toppings.append("기본 토핑")


class NYCheesePizza(Pizza):
    """
    Description:
        Pizza 클래스를 활용해 만든 서브 클래스
    """

    def __init__(self) -> None:
        """
        서브 클래스에 따라 해당 값 입력

        Args:
            None
        Returns:
            None
        """
        super().__init__()
        self._name = "뉴욕 스타일 소스와 치즈 피자"
        self._dough = "씬 크러스트 도우"
        self._sauce = "마리나라 소스"
        self._toppings.append("잘게 썬 레지아노 치즈")


class ChicagoCheesePizza(Pizza):
    """
    Description:
        Pizza 클래스를 활용해 만든 서브 클래스
    """

    def __init__(self) -> None:
        """
        서브 클래스에 따라 해당 값 입력

        Args:
            None
        Returns:
            None
        """
        super().__init__()
        self._name = "시카도 스타일 딥 디쉬 치즈 피자"
        self._dough = "아주 두꺼운 크러스트 도우"
        self._sauce = "플럼토마토 소스"
        self._toppings.append("잘게 조각낸 모짜렐라 치즈")

    @classmethod
    def cut(cls) -> None:
        """
        피자 자르기 과정 함수

        Args:
            None
        Returns:
            None
        """
        print("네모난 모양으로 피자 자르기")
