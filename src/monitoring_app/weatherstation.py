"""
날씨 모니터링 앱

Description:
    날씨 모니터링 앱 기능 테스트

Author:
    Name: KyungHyun Lim
    Email: lkh1075@gmail.com
"""

from monitoring_app.displays import (
    CurrentConditionDisplay,
    ForecastDisplay,
    StatisticsDisplay,
)
from monitoring_app.weatherdata import WeatherData

if __name__ == "__main__":
    weather_data = WeatherData()

    current_display = CurrentConditionDisplay(weather_data)
    static_display = StatisticsDisplay(weather_data)
    forecast_display = ForecastDisplay(weather_data)

    print("-" * 100)
    weather_data.set_measurements(80, 65, 59)
    print("기상변화", "-" * 90)
    weather_data.set_measurements(45, 61, 87)
    print("기상변화", "-" * 90)
    weather_data.set_measurements(111, 65, 92)
