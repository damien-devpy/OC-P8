from pytest import mark
from search_app.views import ResultsView

input_and_expect_return = [
    ('Compote de pommes.',
     'compote pommes',
     ),
    ('Pot de nutella',
     'pot nutella',
     ),
    ('Confiture aux pruneaux',
     'confiture pruneaux',
     ),
    ('Sauce au pesto',
     'sauce pesto',
     ),
]


@mark.parametrize("input, expected", input_and_expect_return)
def test_parse_method_remove_stop_word_and_special_char(input, expected):
    search_result = ResultsView()
    assert search_result._parse_input_user(input) == expected
