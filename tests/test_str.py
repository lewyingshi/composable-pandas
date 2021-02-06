from composable_pandas.str import capitalize, islower, isnumeric, istitle, isupper, isspace
from datetime import datetime

import numpy as np
import pytest

from pandas import Series, _testing as tm

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

def test_islower():
    values = ["A", "b", "Xy", "4", "3A", "", "TT", "55", "-", "  "]
    str_s = Series(values)

    lower_e = [False, True, False, False, False, False, False, False, False, False]

    tm.assert_series_equal((str_s >> islower()), Series(lower_e))

    assert (str_s >> islower()).tolist() == [v.islower() for v in values]

def test_isnumeric():
    # 0x00bc: ¼ VULGAR FRACTION ONE QUARTER
    # 0x2605: ★ not number
    # 0x1378: ፸ ETHIOPIC NUMBER SEVENTY
    # 0xFF13: ３ Em 3
    values = ["A", "3", "¼", "★", "፸", "３", "four"]
    s = Series(values)
    numeric_e = [False, True, True, False, True, True, False]
    tm.assert_series_equal((s >> isnumeric()), Series(numeric_e))

    unicodes = ["A", "3", "¼", "★", "፸", "３", "four"]
    assert (s >> isnumeric()).tolist() == [v.isnumeric() for v in unicodes]

    values = ["A", np.nan, "¼", "★", np.nan, "３", "four"]
    s = Series(values)
    numeric_e = [False, np.nan, True, False, np.nan, True, False]
    tm.assert_series_equal((s >> isnumeric()), Series(numeric_e))

def test_istitle():
    values = ["A", "b", "Xy", "4", "3A", "", "TT", "55", "-", "  "]
    str_s = Series(values)

    title_e = [True, False, True, False, True, False, False, False, False, False]

    tm.assert_series_equal((str_s >> istitle()), Series(title_e))

    assert (str_s >> istitle()).tolist() == [v.istitle() for v in values]

def test_isupper():
    values = ["A", "b", "Xy", "4", "3A", "", "TT", "55", "-", "  "]
    str_s = Series(values)

    upper_e = [True, False, False, False, True, False, True, False, False, False]

    tm.assert_series_equal((str_s >> isupper()), Series(upper_e))

    assert (str_s >> isupper()).tolist() == [v.isupper() for v in values]

def test_isspace():
    values = ["A", "b", "Xy", "4", "3A", "", "TT", "55", "-", "  "]
    str_s = Series(values)

    space_e = [False, False, False, False, False, False, False, False, False, True]

    tm.assert_series_equal((str_s >> isspace()), Series(space_e))

    assert (str_s >> isspace()).tolist() == [v.isspace() for v in values]

