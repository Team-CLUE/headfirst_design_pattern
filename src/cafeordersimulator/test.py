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
    Args :
        None
    Returns :
        None
    """
    bevarage = Espresso()
    print(bevarage.getdescription() + " $" + str(bevarage.cost()))

    beverage2 = HouseBlend()
    beverage2 = Mocha(beverage2)
    print(beverage2.getdescription() + " $" + str(beverage2.cost()))


if __name__ == "__main__":
    main()
