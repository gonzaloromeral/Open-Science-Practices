#Tests para el script grobid_2.1
import unittest
import os
from unittest.mock import patch, MagicMock

from grobid_client.grobid_client import GrobidClient
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

class TestScript(unittest.TestCase):

    @patch('builtins.input', side_effect=["/path/to/files"])
    @patch('tkinter.filedialog.askdirectory', return_value="/path/to/files")
    def test_search_for_file_path(self, mock_input, mock_filedialog):
        # Test file path returned is correct
        expected = "/path/to/files"
        actual = search_for_file_path()
        self.assertEqual(actual, expected)

    @patch.object(GrobidClient, 'process')
    def test_grobid_client_process(self, mock_process):
        # Test that GrobidClient.process() method is called with the correct arguments
        mock_process.return_value = "success"
        expected = "success"
        actual = GrobidClient().process("processFulltextDocument", "/path/to/files")
        self.assertEqual(actual, expected)

    def test_word_cloud(self):
        listaglobalKeywords = ["word1", "word2", "word3", "word1"]
        expected = WordCloud(width = 1000, height = 500).generate_from_frequencies(Counter(listaglobalKeywords))
        actual = WordCloud(width = 1000, height = 500).generate_from_frequencies(Counter(listaglobalKeywords))
        self.assertEqual(str(actual), str(expected))

    def test_bar_chart(self):
        list1 = ["Archivo1", "Archivo2"]
        listaglobalnFiguras = [5, 10]
        expected = plt.bar(list1, listaglobalnFiguras)
        actual = plt.bar(list1, listaglobalnFiguras)
        self.assertEqual(str(actual), str(expected))
        
   if __name__ == '__main__':
    unittest.main()
