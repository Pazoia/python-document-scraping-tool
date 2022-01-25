from src.sentence_filter import SentenceFinder

import pytest

def test_find_sentences_in_data_returns_list_of_sentences():
    sentence_finder = SentenceFinder()
    string_with_sentences = "We all made this journey for a reason. It's humbling, but in my heart I know you didn't come here just for me, you came here because you believe in what this country can be. In the face of war, you believe there can be peace. In the face of despair, you believe there can be hope."
    assert sentence_finder.find_sentences_in_data(string_with_sentences) == ["We all made this journey for a reason.", "It's humbling, but in my heart I know you didn't come here just for me, you came here because you believe in what this country can be.", "In the face of war, you believe there can be peace.", "In the face of despair, you believe there can be hope."]

def test_find_sentences_in_data_returns_error_if_data_is_not_of_type_string():
    with pytest.raises(Exception, match="Invalid data type!"):
        sentence_finder = SentenceFinder()
        invalid_data_type = []
        sentence_finder.find_sentences_in_data(invalid_data_type)