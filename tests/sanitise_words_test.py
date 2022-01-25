from src.sanitise_words import SanitiseWord

def test_sanitise_word_returns_a_valid_word():
    sanitise_word = SanitiseWord()
    
    invalid_word_1 = "Capital,"
    invalid_word_2 = "\"Chicago's"
    invalid_word_3 = "today."
    invalid_word_4 = "capitalize"
    valid_word = "Valid"

    assert sanitise_word.sanitise_word(invalid_word_1) == "Capital"
    assert sanitise_word.sanitise_word(invalid_word_2) == "Chicago"
    assert sanitise_word.sanitise_word(invalid_word_3) == "Today"
    assert sanitise_word.sanitise_word(invalid_word_4) == "Capitalize"
    assert sanitise_word.sanitise_word(valid_word) == "Valid"
