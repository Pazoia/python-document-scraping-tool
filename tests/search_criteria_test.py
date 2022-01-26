from src.search_criteria import SearchCriteria

def test_is_long_isogram_returns_true_if_passed_a_valid_isogramic_word():
    isogram = SearchCriteria()

    not_isogramic_word_example_all_caps = "Doctorwho"
    too_short_isogramic_word_example_all_lower = "isogram"
    valid_isogramic_word_example_all_lower = "ambidextrously"

    assert isogram.is_long_isogramic_word(not_isogramic_word_example_all_caps) == False
    assert isogram.is_long_isogramic_word(too_short_isogramic_word_example_all_lower) == False
    assert isogram.is_long_isogramic_word(valid_isogramic_word_example_all_lower) == True

def test_is_long_isogram_returns_true_if_passed_a_valid_isogramic_word():
    isogram = SearchCriteria()

    not_isogramic_word_example_all_caps = "Doctorwho"
    too_short_isogramic_word_example_all_lower = "isogram"
    valid_isogramic_word_example_all_lower = "ambidextrously"

    assert isogram.is_long_isogramic_word(not_isogramic_word_example_all_caps) == False
    assert isogram.is_long_isogramic_word(too_short_isogramic_word_example_all_lower) == False
    assert isogram.is_long_isogramic_word(valid_isogramic_word_example_all_lower) == True

def test_is_long_isogram_returns_true_if_passed_a_valid_isogramic_word():
    isogram = SearchCriteria()

    not_isogramic_word_example_all_caps = "Doctorwho"
    too_short_isogramic_word_example_all_lower = "isogram"
    valid_isogramic_word_example_all_lower = "ambidextrously"

    assert isogram.is_long_isogramic_word(not_isogramic_word_example_all_caps) == False
    assert isogram.is_long_isogramic_word(too_short_isogramic_word_example_all_lower) == False
    assert isogram.is_long_isogramic_word(valid_isogramic_word_example_all_lower) == True
