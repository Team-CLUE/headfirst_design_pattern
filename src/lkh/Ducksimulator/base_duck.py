"""
각종 오리에 대한 정의 모듈

Description:
    추상클래스 BaseDuck 상속받아, 각각의 알맞은 Quack, Fly 행동을 하는 Duck 클래스 구현

Author:
    Name: KyungHyun Lim
    Email: lkh1075@gmail.com
"""

from abc import abstractmethod

from lkh.Ducksimulator.fly_behavior import Fly, FlyBehavior, NoFly
from lkh.Ducksimulator.quack_behavior import Quack, QuackBehavior, Squeak


class BaseDuck:
    """
    다양한 Duck들을 구현하기 위한 Abstractive class
    """

    quackbehavior = QuackBehavior()
    flybehavior = FlyBehavior()

    @abstractmethod
    def __init__(self) -> None:
        """
        상속받는 클래스에 따라 행동 선택 구현
        """

    @abstractmethod
    def display(self) -> None:
        """
        상속받는 클래스에 따라 오리의 정보 출력 구현
        """

    def perform_quack(self) -> None:
        """
        상속받는 클래스에 따라 오리가 소리를 내는 행동 수행
        """
        self.quackbehavior.quack()

    def perform_fly(self) -> None:
        """
        상속받는 클래스에 따라 오리가 소리를 내는 행동 수행
        """
        self.flybehavior.fly()


class RealDuck(BaseDuck):
    """
    진짜 오리에 대한 행동을 정의한 클래스
    """

    def __init__(self) -> None:
        """
        오리의 행동 정의
        """
        super().__init__()
        self.quackbehavior = Quack()
        self.flybehavior = Fly()

    def display(self) -> None:
        """
        오리의 정보 출력
        """
        print("저는 진짜 오리입니다.")


class RubberDuck(BaseDuck):
    """
    고무 오리에 대한 행동을 정의한 클래스
    """

    def __init__(self) -> None:
        """
        오리의 행동 정의
        """
        super().__init__()
        self.quackbehavior = Squeak()
        self.flybehavior = NoFly()

    def display(self) -> None:
        """
        오리의 정보 출력
        """
        print("저는 고무 오리입니다.")
