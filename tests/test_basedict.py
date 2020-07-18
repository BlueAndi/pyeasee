import pytest
import datetime
from easee import BaseDict


def test_parse_iso_date_without_millis():
    bd = BaseDict({"date": "2020-07-18T07:02:45Z"})
    date = bd.get("date")
    assert type(date) == datetime.datetime


def test_parse_iso_date_with_millis():
    bd = BaseDict({"date": "2020-04-06T11:59:53.135015"})
    date = bd.get("date")
    assert type(date) == datetime.datetime
