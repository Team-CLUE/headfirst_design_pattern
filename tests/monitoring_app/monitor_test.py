"""
날씨 모니터링 앱 기능을 테스트 하기 위한 모듈

Description:
    날씨 모니터링 앱 기능을 테스트

Author:
    Name: KyungHyun Lim
    Email: lkh1075@gmail.com
"""

import random

from monitoring_app.displays import (
    CurrentConditionDisplay,
    ForecastDisplay,
    StatisticsDisplay,
)
from monitoring_app.weatherdata import WeatherData


def test_info_update() -> None:
    """새로운 관측값이 observer 들에게 제대로 전파되는지 테스트"""
    weather_data = WeatherData()

    current_display = CurrentConditionDisplay(weather_data)
    static_display = StatisticsDisplay(weather_data)
    forecast_display = ForecastDisplay(weather_data)

    temperature = random.randrange(-20, 120)
    humidity = random.randrange(0, 100)
    pressure = random.randrange(0, 100)

    weather_data.set_measurements(temp=temperature, humidity=humidity, pressure=pressure)

    assert (
        current_display.temperature == temperature
    ), "current display's temperature has not been updated"
    assert current_display.humidity == humidity, "current display's humidity has not been updated"
    assert static_display.temperature == temperature, "static's temperature has not been updated"
    assert (
        forecast_display.temperature == temperature
    ), "forecast display's temperature has not been updated"


def remove_and_register_test() -> None:
    """데이터 객체에 등록되어 있는 observer들을 정상적으로 제거, 등록할 수 있는지 테스트"""
    weather_data = WeatherData()

    current_display = CurrentConditionDisplay(weather_data)
    static_display = StatisticsDisplay(weather_data)
    forecast_display = ForecastDisplay(weather_data)

    assert current_display in weather_data.observer_list, "Observer has not been registered"
    assert static_display in weather_data.observer_list, "Observer has not been registered"
    assert forecast_display in weather_data.observer_list, "Observer has not been registered"

    weather_data.remove_observer(current_display)

    assert len(weather_data.observer_list) == 2, "Observer list has not been removed"
    assert current_display not in weather_data.observer_list, "Other objects are removed"

    weather_data.register_observer(current_display)

    assert len(weather_data.observer_list) == 3, "Observer list has not been registered"
    assert current_display in weather_data.observer_list, "Other objects are registered"
