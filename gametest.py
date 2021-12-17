from unittest import TestCase, main as testmain
from game import Game


C_TITLE = 'Diablo III'
C_WEBSITE = 'blizzard.com/diablo'
C_GENRE_TYPE = 2
C_SCORE = 9.0
C_GENRE = 

class GameTest(TestCase):

    def setUp(self):
        g = Game()
        g.title = C_TITLE
        g.website = C_WEBSITE
        g.genre = C_GENRE
        g.score = C_SCORE
        self.game = g


    def test_title(self):
        self.assertEqual(self.game.title, C_TITLE)
        new = 'test game'
        self.game.title = new
        self.assertEqual(self.game.title, new)
    

    def test_title(self):
        self.assertEqual(self.game.website, C_WEBSITE)
        new = 'newsite'
        self.game.website = new
        self.assertEqual(self.game.website, new)

    def test_genre_type(self):
        self.assertEqual(self.game.genre_type, C_GENRE_TYPE)
        new = 0
        self.game.genre_type = new
        self.assertEqual(self.game.website, 0)

    def test_genre(self):
        self.assertEqual(self.game.genre, 'RPG')
        self.game.genre_type = 0
        self.assertEqual(self.game.genre, 'Unknown')
        self.game.genre_type = 5
        self.assertEqual(self.game.genre, 'Racing')


    def test_score(self):
        self.assertEqual(self.game.score, C_SCORE)

    def test_score_new(self):
        new = 8.2
        self.game.score = new
        self.assertEqual(self.game.score, new)

    def test_score_undervalue(self):
        with self.assertRaises(ValueError) as context:
            self.game.score = -1.0

    def test_score_uppervalue(self):
        with self.assertRaises(ValueError) as context:
            self.game.score = 10.1




if __name__ == '__main__':
    testmain()



    