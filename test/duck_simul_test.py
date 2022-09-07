"""
Duck Simulator Test 모듈

Description:
    Duck의 종류에 따라, Quack 및 Fly이 기능이 의도한대로 동작하는지 간단한 Test 수행

Author:
    Name: KyungHyun Lim
    Email: lkh1075@gmail.com
"""


from ducksimulator.base import RealDuck, RubberDuck


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
