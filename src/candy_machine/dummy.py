"""
Dummy class 정의

Description:
    Circular import 방지를 위한 Dummy class

Author:
    Name: KyungHyun Lim
    Email: lkh1075@gmail.com
"""

from abc import abstractmethod


class CandyMachine:
    """Dummy class : machine.CandyMachine"""

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def insert_quarter(self) -> None:
        """동전 삽입에 따른 상태 변화"""

    @abstractmethod
    def eject_quarter(self) -> None:
        """동전 반환에 따른 상태 변화"""

    @abstractmethod
    def turn_crank(self) -> None:
        """다이얼 회전에 따른 상태 변화"""

    @abstractmethod
    def dispense(self) -> None:
        """Candy 제공에 따른 상태 변화"""

    @abstractmethod
    def release_candy(self) -> None:
        """Candy 제공에 따른 변화 정의"""

    @abstractmethod
    def set_state(self) -> None:
        """Candy machine 상태 설정"""

    @abstractmethod
    def get_state(self) -> None:
        """현재 Candy machine 상태 반환"""

    @abstractmethod
    def get_count(self) -> None:
        """현재 Candy 개수 반환"""

    @abstractmethod
    def get_noquarter_state(self) -> None:
        """동전없음 상태 반환"""

    @abstractmethod
    def get_hasquarter_state(self) -> None:
        """동전소유 상태 반환"""

    @abstractmethod
    def get_soldout_state(self) -> None:
        """매진 상태 반환"""

    @abstractmethod
    def get_sold_state(self) -> None:
        """판매중 상태 반환"""

    @abstractmethod
    def get_winner_state(self) -> None:
        """당첨 상태 반환"""
