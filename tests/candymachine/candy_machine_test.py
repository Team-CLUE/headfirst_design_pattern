"""
Candy machine 앱 기능을 테스트 하기 위한 모듈

Description:
    Candy machine 앱 기능을 테스트

Author:
    Name: KyungHyun Lim
    Email: lkh1075@gmail.com
"""

from candy_machine.machine import CandyMachine


def basic_function_test() -> None:
    """기본적인 상태 변화 및 Candy 개수 변화에 대한 테스트"""
    candy_machine = CandyMachine(2)

    candy_machine.insert_quarter()
    assert (
        candy_machine.get_state() == candy_machine.get_hasquarter_state()
    ), f"Incorrect state, {candy_machine.get_state()}"

    candy_machine.turn_crank()
    assert (
        candy_machine.get_state() == candy_machine.get_noquarter_state()
    ), f"Incorrect state, {candy_machine.get_state()}"

    assert (
        candy_machine.get_count() == 1
    ), f"There is no change on Candy count, {candy_machine.get_count()}"

    candy_machine.insert_quarter()
    candy_machine.turn_crank()
    assert (
        candy_machine.get_state() == candy_machine.get_soldout_state()
    ), f"Incorrect state, {candy_machine.get_state()}"

    assert (
        candy_machine.get_count() == 0
    ), f"There is no change on Candy count, {candy_machine.get_count()}"

    candy_machine.refill_candy(10)

    assert candy_machine.get_count() == 10, f"Incorrect Candy count, {candy_machine.get_count()}"
