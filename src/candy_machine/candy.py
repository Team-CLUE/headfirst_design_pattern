"""
Candy 클래스 정의

Description:
    기계에 들어갈 Candy를 나타내는 Class 정의

Author:
    Name: KyungHyun Lim
    Email: lkh1075@gmail.com
"""

import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from candy_machine.machine import CandyMachine


class Candy:
    """기계가 반환하는 Candy"""

    def __init__(self, candy_machine: "CandyMachine") -> None:
        """클래스 초기화"""
        self.candy_machine = candy_machine
        # 0: choco, 1: strawberry, 2: vanila, 3: Mint, 4: coffee
        self.flavor = random.randint(0, 5)

    def show_activity(self) -> None:
        """캔디를 소유하고 있는 Candy machine의 상태 표시"""
        curr_state = self.candy_machine.get_state()
        curr_state.show_state()

    def get_flavor(self) -> None:
        """캔디의 맛을 반환"""
        return self.flavor
