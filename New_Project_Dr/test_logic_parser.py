from logic_parser import parse_condition_string


def test_parse_condition_string():
    subject = "x=3 <and> y= 4"
    actual = parse_condition_string(subject)
    expected = ['x=3', 'and', 'y= 4']
    assert actual == expected
    subject = "x=3 <or> y=4"
    actual = parse_condition_string(subject)
    expected = ['x=3', 'or', 'y=4']
    assert actual == expected
    subject = "x=3 <not> y=4"
    actual = parse_condition_string(subject)
    expected = ['x=3', 'not', 'y=4']
    assert actual == expected
        
