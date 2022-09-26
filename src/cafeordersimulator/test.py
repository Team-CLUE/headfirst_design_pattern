"""
cafe order test 코드

Description:
    cafe order 테스트를 위한 코드

Author:
    Name: Gangmin Kim
    Email: rlarkdals7@gmail.com
"""

from beverage import Espresso, HouseBlend
from condiment import Mocha


def main() -> None:
    """summary
    Description:
        Test 진행함수
    """
    bevarage = Espresso()
    print(bevarage.get_description() + " $" + str(bevarage.cost()))
    assert bevarage.get_description() == "Espresso"

    beverage2 = HouseBlend()
    beverage2 = Mocha(beverage2)
    print(beverage2.get_description() + " $" + str(beverage2.cost()))
    assert beverage2.get_description() == "HouseBlend, 모카"

    beverage3 = HouseBlend()
    beverage3.set_size("venti")
    beverage3 = Mocha(beverage3)
    print(beverage3.cost())
    assert beverage3.cost() == 1.09


if __name__ == "__main__":
    main()
