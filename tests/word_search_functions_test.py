from src.word_search_functions import IsIsogramicWord

def test_is_long_isogram_returns_a_long_isogramic_word():
    isogram = IsIsogramicWord()

    
    not_isogramic_word_example_all_caps = "Doctorwho"
    too_short_isogramic_word_example_all_lower = "isogram"
    valid_isogramic_word_example_all_lower = "ambidextrously"

    assert isogram.is_long_isogramic_word(not_isogramic_word_example_all_caps) == False
    assert isogram.is_long_isogramic_word(too_short_isogramic_word_example_all_lower) == False
    assert isogram.is_long_isogramic_word(valid_isogramic_word_example_all_lower) == True



