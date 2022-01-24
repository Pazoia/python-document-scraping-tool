from src.data_extraction import DataExtraction

from unittest.mock import mock_open, patch

def test_get_data_from_file_returns_data():
    data_extraction = DataExtraction()

    m = mock_open(read_data="Some data returned")

    with patch("builtins.open", m) as mocked_open:
        assert data_extraction.get_data_from_file("fake/file/path") == "Some data returned"
        mocked_open.assert_called_once_with("fake/file/path", "r")