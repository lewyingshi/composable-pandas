from composable_pandas.str import capitalize, is_month_start, is_quarter_start, is_quarter_end, is_year_start, is_year_end
from datetime import datetime

import numpy as np
import pytest

from pandas import Series, _testing as tm
import calendar
from datetime import datetime, timedelta
import locale
import unicodedata
from dateutil.tz import tzutc
import numpy as np
import pytest
import pytz
from pytz import timezone, utc
from pandas import NaT, Timedelta, Timestamp
from pandas.tseries import offsets

def test_capitalize():
    values = Series(["FOO", "BAR", np.nan, "Blah", "blurg"])
    result = values >> capitalize()
    exp = Series(["Foo", "Bar", np.nan, "Blah", "Blurg"])
    tm.assert_series_equal(result, exp)

    # mixed
    mixed = Series(["FOO", np.nan, "bar", True, datetime.today(), "blah", None, 1, 2.0])
    mixed = mixed >> capitalize()
    exp = Series(["Foo", np.nan, "Bar", np.nan, np.nan, "Blah", np.nan, np.nan, np.nan])
    tm.assert_almost_equal(mixed, exp)



def test_is_month_startend():
    ts = Timestamp("2014-01-01 00:00:00+01:00")
    starts = ["is_month_start"]
    for start in starts:
        assert getattr(ts, start)
    ts = Timestamp("2014-12-31 23:59:59+01:00")
    ends = ["is_month_end"]
    for end in ends:
        assert getattr(ts, end)

def test_is_quarter_startend():
    ts = Timestamp("2014-01-01 00:00:00+01:00")
    starts = ["is_quarter_start"]
    for start in starts:
        assert getattr(ts, start)
    ts = Timestamp("2014-12-31 23:59:59+01:00")
    ends = ["is_quarter_end"]
    for end in ends:
        assert getattr(ts, end)

def test_is_year_startend():
    ts = Timestamp("2014-01-01 00:00:00+01:00")
    starts = ["is_year_start"]
    for start in starts:
        assert getattr(ts, start)
    ts = Timestamp("2014-12-31 23:59:59+01:00")
    ends = ["is_year_end"]
    for end in ends:
        assert getattr(ts, end)

def test_properties_business():
    ts = Timestamp("2017-10-01", freq="B")
    control = Timestamp("2017-10-01")
    assert not ts.is_month_start  # not a weekday
    assert not ts.is_quarter_start  # not a weekday
     # Control case: non-business is month/qtr start
    assert control.is_month_start
    assert control.is_quarter_start

    ts = Timestamp("2017-09-30", freq="B")
    control = Timestamp("2017-09-30")
    assert not ts.is_month_end  # not a weekday
    assert not ts.is_quarter_end  # not a weekday
    # Control case: non-business is month/qtr start
    assert control.is_month_end
    assert control.is_quarter_end

