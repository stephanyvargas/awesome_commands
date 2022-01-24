# tests/test_lib.py
from awesome_commands.lib import change_toarray, city_weather
import numpy

def test_change_tolist():
    assert type(change_toarray([48.8, 2.3, 48.2, 2.3])) == numpy.ndarray
    assert type(change_toarray('abc')) == str
    assert city_weather() == None
