"""
날씨 모니터링 앱에서 사용되는 display 기능들을 정의한 모듈

Description:
    display 기능 정의 및 구현

Author:
    Name: KyungHyun Lim
    Email: lkh1075@gmail.com
"""

from monitoring_app.interfaces import Display, Observer
from monitoring_app.weatherdata import WeatherData


class CurrentConditionDisplay(Observer, Display):
    """summary
    Description:
        현재 날씨 상황을 display 해주는 기능 담당
    """

    def __init__(self, weather_data: WeatherData) -> None:
        super().__init__()
        self.temperature: float = 0.0
        self.humidity: float = 0.0
        self.weather_data: WeatherData = weather_data
        self.weather_data.register_observer(self)

    def update(self, temp: float, humidity: float, pressure: float) -> None:
        """새로운 관측값을 업데이트

        Args:
            temp: 온도
            humidity: 습도
            pressure: 기압

        Returns:
            None
        """
        self.temperature = temp
        self.humidity = humidity
        self.display()

    def display(self) -> None:
        """관측값을 화면에 출력

        Args:
            temp: 온도
            humidity: 습도

        Returns:
            None
        """
        print(f"현재 상태: 온도 {self.temperature:.3f}F, 습도 {self.humidity:.3f}%")
