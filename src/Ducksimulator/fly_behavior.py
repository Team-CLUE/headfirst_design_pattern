"""
하늘을 나는 행동들에 대한 클래스를 정의한 모듈

Description:
    추상클래스 FlyBehavior 상속받아, 각각의 Fly 행동들을 클래스로 구현

Author:
    Name: KyungHyun Lim
    Email: lkh1075@gmail.com
"""

from abc import abstractmethod


class FlyBehavior:
    """summary
    Description:
        나는 행동의 종류에 따라 클래스를 정의하기 위한 Abstractive class
    """

    @abstractmethod
    def fly(self) -> None:
        """
        상속받는 클래스에서 정의되는 함수
        """

    def dummy(self) -> None:
        """
        프리커밋 진행을 위한 dummy 함수
        """


class Fly(FlyBehavior):
    """summary
    Description:
        FlyBehavior 중 날 수 있는 행동 클래스
    """

    def fly(self) -> None:
        """나는 행동에 대한 정의

        Args:
            None

        Returns:
            None
        """
        print("무한한 공간 저 너머로!")


class NoFly(FlyBehavior):
    """summary
    Description:
        FlyBehavior 중 날지 못하는 행동 클래스
    """

    def fly(self) -> None:
        """날지 못하는 행동에 대한 정의

        Args:
            None

        Returns:
            None
        """
        print("<< 날지 못함 >>")
