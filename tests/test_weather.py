"""Starter tests for the weather module.

These tests deliberately cover only ordinary examples. They show how pytest works,
but they are not a sufficient test suite for the specification in SPECIFICATION.md.
"""

import pytest

from weather import (
    average_temperature,
    filter_by_temperature,
    hottest_measurement,
    parse_measurement,
    parse_time,
)
import pytest


def test_parse_time_regular_time():
    assert parse_time("14:21") == 861


def test_parse_time_zeros():
    assert parse_time("9:9") == 549
    assert parse_time("09:09") == 549

    assert parse_time("00:00") == 0
    assert parse_time("0:0") == 0
    assert parse_time("23:59") == 1439


def test_parse_time_ValErr():

    with pytest.raises(ValueError):
        parse_time("24:00")

    with pytest.raises(ValueError):     
        parse_time("3:70")

    # -> failed test (mit value error): .split geht nicht bei none 
    with pytest.raises(AttributeError):     
        parse_time(None)


def test_parse_measurement_regular_line():
    assert parse_measurement("Köln;14:21;21.7") == ("Köln", 861, 21.7)

def test_parse_measurement_trim_city():
    assert parse_measurement("  Köln ;14:21;-21.7") == ("Köln", 861, -21.7)

def test_parse_measurement_empty_city():
    with pytest.raises(ValueError):
        parse_measurement(";14:21;21.7")

def test_parse_measurement_missing_part():
    with pytest.raises(ValueError):
        parse_measurement("Köln;14:21")

def test_parse_measurement_wrong_split_character():
    with pytest.raises(ValueError):
        parse_measurement("Köln,14:21,21.7")

def test_parse_measurement_invalid_temp_input():
    with pytest.raises(ValueError):
        parse_measurement("Köln;14:21;21,23")


def test_filter_by_temperature_regular_values():
    measurements = [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 18.5),
        ("Bonn", 900, 25.0),
    ]

    assert filter_by_temperature(measurements, 15.0, 20.0) == [
        ("Düsseldorf", 720, 18.5)
    ]


def test_filter_by_temperature_edge():
    measurements = [
            ("Köln", 600, 10.0),
            ("Düsseldorf", 720, 18.5),
            ("Bonn", 900, 25.0),
        ]
    
    assert filter_by_temperature(measurements, 10.0, 18.5) == [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 18.5)
    ]


def test_filter_by_temperature_order_double():
    measurements = [
                ("Köln", 600, 10.0),
                ("Düsseldorf", 720, 18.5),
                ("Düsseldorf", 720, 18.5),
                ("Bonn", 900, 25.0),
            ]
        
    assert filter_by_temperature(measurements, 15.0, 18.5) == [
        ("Düsseldorf", 720, 18.5),
        ("Düsseldorf", 720, 18.5)
    ]

def test_filter_by_temperature_list():
    measurements = [
            ("Köln", 600, 10.0),
            ("Düsseldorf", 720, 18.5),
            ("Bonn", 900, 25.0),
        ]
    
    assert type(filter_by_temperature(measurements, 15.0, 20.0)) == list


def test_filter_by_temperature_emptylist():
    measurements = []

    assert filter_by_temperature(measurements, 15.0, 18.5) == []


def test_filter_by_temperature_samelimit():
    measurements = [
                ("Köln", 600, 10.0),
                ("Düsseldorf", 720, 18.5),
                ("Bonn", 900, 25.0),
            ]
        
    assert filter_by_temperature(measurements, 15.0, 15.0) == []
    assert filter_by_temperature(measurements, 18.5, 18.5) == [("Düsseldorf", 720, 18.5)]


def test_average_temperature_regular_values():
    measurements = [
        ("Köln", 600, 10.0),
        ("Köln", 720, 20.0),
    ]

    assert average_temperature(measurements, "Köln") == 15.0

def test_average_temperature_city_upper_lowercase():
    measurements = [
            ("Köln", 600, 10.0),
            ("köln", 720, 20.0),
    ]

    assert average_temperature(measurements, "Köln") == 10.0

def test_average_temperature_empty_input():
    measurements = []

    with pytest.raises(ValueError):
        average_temperature(measurements, "Köln")

#def test_average_temperature_none_input():
    #measurements = None

    #with pytest.raises(ValueError):
        #average_temperature(measurements, "Köln")

def test_average_temperature_no_match():
    measurements = [
        ("Köln", 600, 10.0),
        ("Köln", 720, 20.0),
    ]

    with pytest.raises(ValueError):
        average_temperature(measurements, "Düsseldorf")




def test_hottest_measurement_with_unique_maximum():
    measurements = [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 25.0),
        ("Bonn", 900, 20.0),
    ]

    assert hottest_measurement(measurements) == ("Düsseldorf", 720, 25.0)

def test_hottest_measurement_with_multiple_maxima_unique_time():
    measurements = [
        ("Köln", 600, 25.0),
        ("Düsseldorf", 720, 25.0),
        ("Bonn", 900, 20.0),
    ]

    assert hottest_measurement(measurements) == ("Köln", 600, 25.0)

def test_hottest_measurement_with_multiple_maxima_multiple_times():
    measurements = [
        ("Köln", 600, 25.0),
        ("Düsseldorf", 600, 25.0),
        ("Bonn", 900, 20.0),
    ]

    assert hottest_measurement(measurements) == ("Köln", 600, 25.0)

def test_hottest_measurement_with_empty_measurements():
    measurements = []

    with pytest.raises(ValueError):
        hottest_measurement(measurements)

