"""
    피자 클래스

    Description:
        피자 기본 정보를 담고 있는 클래스

    Author:
        Name: Junhyeok Yang
        Email: surfing2003@naver.com
"""
from abc import ABCMeta, abstractmethod
from typing import List


class Pizza:
    """
    Description:
        다양한 피자를 구현하는데 활용하기 위한 클래스
    """

    __metaclass__ = ABCMeta

    _name: str = ""
    _toppings: List[str] = []

    @abstractmethod
    def __init__(self) -> None:
        """
        상속받는 클래스에 따라 행동 선택 구현

        Args:
            None
        Returns:
            None
        """

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


class BasePizza(Pizza):
    """
    Description:
        Pizza를 상속받아 생성한 기본피자 서브클래스
    """

    def __init__(self) -> None:
        super().__init__()
        self._name = "기본피자"
        self._toppings = ["1번기본", "2번기본", "3번기본"]


class CheesePizza(Pizza):
    """
    Description:
        Pizza를 상속받아 생성한 치즈피자 서브클래스
    """

    def __init__(self) -> None:
        super().__init__()
        self._name = "치즈피자"
        self._toppings = ["1번치즈", "2번치즈", "3번치즈"]


class PepperoniPizza(Pizza):
    """
    Description:
        Pizza를 상속받아 생성한 페퍼로니피자 서브클래스
    """

    def __init__(self) -> None:
        super().__init__()
        self._name = "페퍼로니피자"
        self._toppings = ["1번페퍼로니", "2번페퍼로니", "3번페퍼로니"]


class ClamPizza(Pizza):
    """
    Description:
        Pizza를 상속받아 생성한 조개피자 서브클래스
    """

    def __init__(self) -> None:
        super().__init__()
        self._name = "조개피자"
        self._toppings = ["1번조개", "2번조개", "3번조개"]


class VeggiePizza(Pizza):
    """
    Description:
        Pizza를 상속받아 생성한 채소피자 서브클래스
    """

    def __init__(self) -> None:
        super().__init__()
        self._name = "채소피자"
        self._toppings = ["1번채소", "2번채소", "3번채소"]
