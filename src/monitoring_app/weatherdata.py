"""
날씨 모니터링 앱의 날씨 데이터 관리자(subject) 구현 모듈

Description:
    날씨 모니터링 앱의 날씨 데이터 관리자(subject) 구현

Author:
    Name: KyungHyun Lim
    Email: lkh1075@gmail.com
"""

from typing import List

from monitoring_app.interfaces import Observer, Subject


class WeatherData(Subject):
    """summary
    Description:
        날씨 데이터 및 observer 리스트를 관리하는 Subject 클래스
    """

    def __init__(self) -> None:
        super().__init__()
        self.observer_list: List[Observer] = []
        self.temperature: float = 0.0
        self.humidity: float = 0.0
        self.pressure: float = 0.0

    def register_observer(self, any_observer: Observer) -> None:
        """관리할 observer를 추가적으로 등록

        Args:
            any_observer: 등록할 Observer

        Returns:
            None
        """
        self.observer_list.append(any_observer)

    def remove_observer(self, any_observer: Observer) -> None:
        """입력 받은 observer를 관리 observer 리스트에서 제거

        Args:
            any_observer: 제거할 Observer

        Returns:
            None
        """
        self.observer_list.remove(any_observer)

    def noitfy(self) -> None:
        """관리 중인 observer들에게 날씨 데이터 변경을 전파

        Args:
            None

        Returns:
            None
        """
        for observer in self.observer_list:
            observer.update()

    def set_measurements(self, temp: float, humidity: float, pressure: float) -> None:
        """새로운 관측값을 업데이트 및 observer들에게 전파

        Args:
            temp: 온도
            humidity: 습도
            pressure: 기압

        Returns:
            None
        """

        self.temperature = temp
        self.humidity = humidity
        self.pressure = pressure
        self.noitfy()
