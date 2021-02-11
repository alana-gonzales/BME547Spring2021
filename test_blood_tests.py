def test_check_HDL():
    from blood_tests import check_HDL
    norm_result = check_HDL(65)
    norm_expected = "Normal"
    assert norm_result == norm_expected

    bord_result = check_HDL(45)
    bord_expected = "Borderline Low"
    assert bord_result == bord_expected

    low_result = check_HDL(35)
    low_expected = "Low"
    assert low_result == low_expected
