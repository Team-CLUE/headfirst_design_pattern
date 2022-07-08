"""
Quack 소리를 내는 행동들에 대한 클래스를 정의한 모듈

Description:
    추상클래스 QuackBehavior를 상속받아, 각각의 Quack 행동들을 클래스로 구현

Author:
    Name: KyungHyun Lim
    Email: lkh1075@gmail.com
"""

from abc import abstractmethod


class QuackBehavior:
    """
    꽥 행동의 종류에 따라 클래스를 정의하기 위한 부모 클래스
    """

    @abstractmethod
    def quack(self) -> None:
        """
        상속받는 클래스에서 정의되는 함수
        """

    def dummy(self) -> None:
        """
        프리커밋 진행을 위한 dummy 함수
        """


class Quack(QuackBehavior):
    """
    QuackBehavior 중 "꽥" 소리를 나타내는 행동 클래스
    """

    def quack(self) -> None:
        """
        꽥 소리를 내는 기능
        """
        print("꽥")


class MuteQuack(QuackBehavior):
    """
    QuackBehavior 중 소리를 나타내지 못하는 행동 클래스
    """

    def quack(self) -> None:
        """
        아무 소리도 내지 못하는 것을 표현하는 기능
        """
        print("<< --- >>")


class Squeak(QuackBehavior):
    """
    QuackBehavior 중 "삑" 소리를 나타내는 행동 클래스
    """

    def quack(self) -> None:
        """
        삑 소리를 내는 기능
        """
        print("삑")
