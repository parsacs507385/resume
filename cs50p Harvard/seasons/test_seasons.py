from seasons import convert


def test_convert():
    assert convert("365") == "Five hundred and twenty-five thousand, six hundred"
    assert convert(365) == "Five hundred and twenty-five thousand, six hundred"
    assert convert("731") == "One million, fifty-two thousand, six hundred and forty"
    assert convert(731) == "One million, fifty-two thousand, six hundred and forty"
