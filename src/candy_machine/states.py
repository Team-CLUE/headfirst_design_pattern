"""
Candy machine 상태 추상클래스(인터페이스) 정의

Description:
    Candy machine 가질 수 있는 상태 클래스들을 정의합니다.

Author:
    Name: KyungHyun Lim
    Email: lkh1075@gmail.com
"""

import random
from typing import TYPE_CHECKING

from candy_machine.interface import State

if TYPE_CHECKING:
    from candy_machine.machine import CandyMachine


class SoldState(State):
    """summary
    Description:
        판매 상태에 대한 변화 정의
    """

    def __init__(self, candy_machine: "CandyMachine") -> None:
        super().__init__()
        self.candy_machine = candy_machine

    def insert_quarter(self) -> None:
        """동전 삽입시 상태변화 정의"""
        print("이미 Candy가 나오고 있습니다.")

    def eject_quarter(self) -> None:
        """동전 제거시 상태변화 정의"""
        print("이미 Candy가 나오고 있습니다.")

    def turn_crank(self) -> None:
        """다이얼 회전시 상태변화 정의"""
        print("다이얼은 한번만 돌려주세요!")

    def dispense(self) -> None:
        """알 제공시 상태변화 정의"""
        self.candy_machine.release_candy()
        if self.candy_machine.get_count() > 0:
            self.candy_machine.set_state(self.candy_machine.get_noquarter_state())
        else:
            self.candy_machine.set_state(self.candy_machine.get_soldout_state())


class SoldOutState(State):
    """summary
    Description:
        매진 상태에 대한 변화 정의
    """

    def __init__(self, candy_machine: "CandyMachine") -> None:
        super().__init__()
        self.candy_machine = candy_machine

    def insert_quarter(self) -> None:
        """동전 삽입시 상태변화 정의"""
        print("Candy가 매진되었습니다.")

    def eject_quarter(self) -> None:
        """동전 제거시 상태변화 정의"""
        print("동전이 들어있지 않습니다. Candy가 매진되었습니다.")

    def turn_crank(self) -> None:
        """다이얼 회전시 상태변화 정의"""
        print("동전이 들어있지 않습니다. Candy가 매진되었습니다.")

    def dispense(self) -> None:
        """알 제공시 상태변화 정의"""
        print("현재 상태에서는 실행이 불가능한 행동입니다.")


class HasQuarterState(State):
    """summary
    Description:
        동전 소유 상태에 대한 변화 정의
    """

    def __init__(self, candy_machine: "CandyMachine") -> None:
        super().__init__()
        self.candy_machine = candy_machine

    def insert_quarter(self) -> None:
        """동전 삽입시 상태변화 정의"""
        print("이미 동전이 들어있습니다!")

    def eject_quarter(self) -> None:
        """동전 제거시 상태변화 정의"""
        print("동전이 반환되었습니다.")
        self.candy_machine.set_state(self.candy_machine.get_noquarter_state())

    def turn_crank(self) -> None:
        """다이얼 회전시 상태변화 정의"""
        print("Candy가 나오고있습니다.")
        winner = random.randint(0, 10)
        if winner == 0 and self.candy_machine.get_count() > 1:
            self.candy_machine.set_state(self.candy_machine.get_winner_state())
        else:
            self.candy_machine.set_state(self.candy_machine.get_sold_state())

    def dispense(self) -> None:
        """알 제공시 상태변화 정의"""
        print("이 상태에서는 필요 없습니다.")


class NoQuarterState(State):
    """summary
    Description:
        동전 없음 상태에 대한 변화 정의
    """

    def __init__(self, candy_machine: "CandyMachine") -> None:
        super().__init__()
        self.candy_machine = candy_machine

    def insert_quarter(self) -> None:
        """동전 삽입시 상태변화 정의"""
        print("동전을 넣으셨습니다.")
        self.candy_machine.set_state(self.candy_machine.get_hasquarter_state())

    def eject_quarter(self) -> None:
        """동전 제거시 상태변화 정의"""
        print("동전을 넣어주세요")

    def turn_crank(self) -> None:
        """다이얼 회전시 상태변화 정의"""
        print("동전을 넣어주세요")

    def dispense(self) -> None:
        """알 제공시 상태변화 정의"""
        print("동전을 넣어주세요")


class WinnerState(State):
    """summary
    Description:
        이벤트 당첨에 대한 변화 정의
    """

    def __init__(self, candy_machine: "CandyMachine") -> None:
        super().__init__()
        self.candy_machine = candy_machine

    def insert_quarter(self) -> None:
        """동전 삽입시 상태변화 정의"""
        print("이미 동전을 넣으셨습니다.")

    def eject_quarter(self) -> None:
        """동전 제거시 상태변화 정의"""
        print("이미 Candy가 나오고 있습니다.")

    def turn_crank(self) -> None:
        """다이얼 회전시 상태변화 정의"""
        print("손잡이는 한번만 돌려주세요. 이미 Candy가 나오고 있습니다.")

    def dispense(self) -> None:
        """알 제공시 상태변화 정의"""
        self.candy_machine.release_candy()
        if self.candy_machine.get_count() > 0:
            self.candy_machine.set_state(self.candy_machine.get_soldout_state())
        else:
            self.candy_machine.release_candy()
            print("축하합니다. 당첨되셨습니다.")
            if self.candy_machine.get_count() > 0:
                self.candy_machine.set_state(self.candy_machine.get_noquarter_state())
            else:
                print("Candy가 매진되었습니다.")
                self.candy_machine.set_state(self.candy_machine.get_soldout_state())
