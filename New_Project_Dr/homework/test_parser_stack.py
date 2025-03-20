from parser_stack import process_string

def test_parser_stack():
    subject = "(x<2 and y<4) <Or> (Z>5 <and> N>5)"
    actual = process_string(subject)
    expected = "(x<2 and y<4)  , Or ,  (Z>5  , and ,  N>5)"
    assert actual == expected
