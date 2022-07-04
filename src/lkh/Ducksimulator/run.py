"""
Duck Simulator Test 모듈
"""

from lkh.Ducksimulator.base_duck import RealDuck, RubberDuck


def main() -> None:
    """
    Test 진행 함수
    """
    real_duck = RealDuck()
    rubber_duck = RubberDuck()

    real_duck.display()
    real_duck.perform_quack()
    real_duck.perform_fly()

    print("-" * 100)

    rubber_duck.display()
    rubber_duck.perform_quack()
    rubber_duck.perform_fly()


if __name__ == "__main__":
    main()
