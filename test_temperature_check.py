def test_fever_check():
    from temperature_check import fever_check
    data = [98, 99, 102, 100.5, 87]
    answer = fever_check(data)
    expected = True
    assert answer == expected
