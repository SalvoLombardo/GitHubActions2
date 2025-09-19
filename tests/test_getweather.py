import pytest

from services.weather_api import get_weather

def test_service(city):
    data=get_weather('Palermo')

    

    assert data["city"]=="Palermo"
    assert "temp" in data
    assert "description" in data

#