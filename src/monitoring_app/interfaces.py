"""
날씨 모니터링 앱을 구현하기 위한 추상클래스(인터페이스)들을 정의한 모듈

Description:
    Observer 패턴을 구현하기 위해 Subject 인터페이스와 Observer 인터페이스 정의

Author:
    Name: KyungHyun Lim
    Email: lkh1075@gmail.com
"""

from abc import abstractmethod


class Observer:
    """summary
    Description:
        다양한 Observer들을 구현하기 위한 Abstractive class
    """

    def __init__(self) -> None:
        pass

    @abstractmethod
    def update(self, temp: float, humidity: float, pressure: float) -> None:
        """상속받는 클래스에 따라 행동 선택 구현

        Args:
            temp: 온도
            humidity: 습도
            pressure: 기압

        Returns:
            None
        """

    def dummy(self) -> None:
        """dummy"""


class Display:
    """summary
    Description:
        다양한 Display 장치들을 구현하기 위한 Abstractive class
    """

    def __init__(self) -> None:
        pass

    @abstractmethod
    def display(self) -> None:
        """상속받는 클래스에 따라 행동 선택 구현

        Args:
            None

        Returns:
            None
        """

    def dummy(self) -> None:
        """dummy"""


class Subject:
    """summary
    Description:
        observer들을 관리하는 주체를 구현하기 위한 Abstractive class
    """

    def __init__(self) -> None:
        pass

    @abstractmethod
    def register_observer(self, any_observer: Observer) -> None:
        """상속받는 클래스에 따라 행동 선택 구현

        Args:
            any_observer: 등록할 Observer

        Returns:
            None
        """

    @abstractmethod
    def remove_observer(self, any_observer: Observer) -> None:
        """상속받는 클래스에 따라 행동 선택 구현

        Args:
            any_observer: 제거할 Observer

        Returns:
            None
        """

    @abstractmethod
    def noitfy(self) -> None:
        """상속받는 클래스에 따라 행동 선택 구현

        Args:
            None

        Returns:
            None
        """
