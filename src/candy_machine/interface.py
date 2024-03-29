"""
Candy machine 상태 추상클래스(인터페이스) 정의

Description:
    상태 추상 클래스 정의합니다.

Author:
    Name: KyungHyun Lim
    Email: lkh1075@gmail.com
"""


from abc import abstractmethod


class State:
    """Candy machine 상태 인터페이스"""

    @abstractmethod
    def __init__(self) -> None:
        """클래스 초기화"""

    @abstractmethod
    def insert_quarter(self) -> None:
        """동전 삽입시 상태변화 정의"""

    @abstractmethod
    def eject_quarter(self) -> None:
        """동전 제거시 상태변화 정의"""

    @abstractmethod
    def turn_crank(self) -> None:
        """다이얼 회전시 상태변화 정의"""

    @abstractmethod
    def dispense(self) -> None:
        """알 제공시 상태변화 정의"""
