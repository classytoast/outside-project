from weather_api.weather_main import run_getweather


def test_return_2_elements():
    res = run_getweather('Moscow')
    assert len(res) == 2
