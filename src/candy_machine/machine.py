"""
Candy machine  정의

Description:
    Candy machine 기능을 구현합니다.

Author:
    Name: KyungHyun Lim
    Email: lkh1075@gmail.com
"""

from candy_machine.interface import State
from candy_machine.states import (
    HasQuarterState,
    NoQuarterState,
    SoldOutState,
    SoldState,
)


class CandyMachine:
    """summary
    Description:
        Candy machine action 정의
    """

    def __init__(self, number_candy: int) -> None:
        self.soldout_state = SoldOutState(self)
        self.sold_state = SoldState(self)
        self.hasquarter_state = HasQuarterState(self)
        self.noquarter_state = NoQuarterState(self)

        self.state = State()
        self.count = number_candy

        if self.count > 0:
            self.state = self.noquarter_state
        else:
            self.state = self.soldout_state

    def insert_quarter(self) -> None:
        """동전 삽입에 따른 상태 변화"""
        self.state.insert_quarter()

    def eject_quarter(self) -> None:
        """동전 반환에 따른 상태 변화"""
        self.state.eject_quarter()

    def turn_crank(self) -> None:
        """다이얼 회전에 따른 상태 변화"""
        self.state.turn_crank()

    def dispense(self) -> None:
        """Candy 제공에 따른 상태 변화"""
        self.state.dispense()

    def release_candy(self) -> None:
        """Candy 제공에 따른 변화 정의"""
        if self.count > 0:
            self.count -= 1

    def set_state(self, state: State) -> None:
        """Candy machine 상태 설정

        Args:
            state: Candy machine에 셋팅할 상태

        Returns:
            None
        """
        self.state = state

    def get_state(self) -> State:
        """현재 Candy machine 상태 반환"""
        return self.state

    def get_count(self) -> int:
        """현재 Candy 개수 반환"""
        return self.count

    def get_noquarter_state(self) -> State:
        """동전없음 상태 반환"""
        return self.noquarter_state

    def get_hasquarter_state(self) -> State:
        """동전소유 상태 반환"""
        return self.hasquarter_state

    def get_soldout_state(self) -> State:
        """매진 상태 반환"""
        return self.soldout_state

    def get_sold_state(self) -> State:
        """판매중 상태 반환"""
        return self.sold_state
