import unittest

from BeautifulSoup import BeautifulSoup
import urllib2


class MarvelComicsScraper(object):

    def get_comic_header(self):
        content = open('marvelsource.txt', 'r')
        soup = BeautifulSoup(content)
        headers = soup.findAll("h4")
        return headers


class TestMarvelComicsScraper(unittest.TestCase):

    def test_get_comics_headers(self):
        sut = MarvelComicsScraper()
        headers = sut.get_comic_header()
        self.assertEquals(headers[0], "<h4>Comics</h4>")


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMarvelComicsScraper)
    unittest.TextTestRunner(verbosity=2).run(suite)