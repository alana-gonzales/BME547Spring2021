import pytest

@pytest.mark.parametrize("hdl, exp", [(65, "Normal"), (45, "Borderline Low"), (35, "Low")])

def test_check_HDL(hdl, exp):
    from blood_tests import check_HDL
    result = check_HDL(hdl)
    expected = exp
    assert result == expected