"""
Dummy class 정의

Description:
    Circular import 방지를 위한 Dummy class

Author:
    Name: KyungHyun Lim
    Email: lkh1075@gmail.com
"""

from abc import abstractmethod


class CandyMachine:
    """Dummy class : machine.CandyMachine"""

    def __init__(self) -> None:
        pass

    @abstractmethod
    def dummy1(self) -> None:
        """dummy1"""

    @abstractmethod
    def dummy2(self) -> None:
        """dummy2"""
