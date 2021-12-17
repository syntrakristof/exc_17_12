import os
from unittest import TestCase, main as testmain
from game import Game, GameList, genre_types
from files import read_json_file

C_TITLE = 'Diablo III'
C_WEBSITE = 'blizzard.com/diablo'
C_GENRE_TYPE = 2
C_SCORE = 9.0
C_GENRE = 'RPG'
C_JSON_FILE = 'test_games.json'

class GameTest(TestCase):

    def setUp(self):
        g = Game()
        g.title = C_TITLE
        g.website = C_WEBSITE
        g.genre_type = C_GENRE_TYPE
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
        self.assertEqual(self.game.genre_type, new)

    def test_genre_type_lower(self):
        with self.assertRaises(ValueError) as context:
            self.game.genre_type = -1

    def test_genre_type_upper(self):
        with self.assertRaises(ValueError) as context:
            self.game.genre_type = len(genre_types) + 1
            

    def test_genre(self):
        self.assertEqual(self.game.genre, C_GENRE)
        self.game.genre_type = 0
        self.assertEqual(self.game.genre, 'Unknown')
        self.game.genre_type = 1
        self.assertEqual(self.game.genre, 'FPS')
        self.game.genre_type = 2
        self.assertEqual(self.game.genre, 'RPG')
        self.game.genre_type = 3
        self.assertEqual(self.game.genre, 'MMO')
        self.game.genre_type = 4
        self.assertEqual(self.game.genre, 'Arcade')
        self.game.genre_type = 5
        self.assertEqual(self.game.genre, 'Racing')
        self.game.genre_type = len(genre_types) - 1
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

    def test_str_repr(self):
        self.assertIn(str(C_SCORE), str(self.game))
        self.assertIn(C_TITLE, str(self.game))
        self.assertIn(' - ', str(self.game))
        

    def test_json(self):
        json = self.game.as_json
        self.assertIn(str(C_SCORE), json)
        self.assertIn(str(C_TITLE), json)
        self.assertIn(str(C_WEBSITE), json)
        self.assertIn(str(C_GENRE_TYPE), json)
        self.assertIn('website', json)
        self.assertIn('genre_type', json)
        self.assertIn('score', json)
        self.assertIn('title', json)


        self.game.score = 5.0
        self.game.title = 'new game'
        self.game.website = 'newurl'
        self.game.genre_type = 0

        self.game.as_json = json
        self.assertEqual(self.game.title, C_TITLE)
        self.assertEqual(self.game.score, C_SCORE)
        self.assertEqual(self.game.genre_type, C_GENRE_TYPE)
        self.assertEqual(self.game.website, C_WEBSITE)
        self.assertEqual(self.game.genre, C_GENRE)

    def test_fromDict(self):
        g = Game.fromDict(self.game.as_dict)
        self.assertEqual(self.game.title, g.title)
        self.assertEqual(self.game.score, g.score)
        self.assertEqual(self.game.genre_type, g.genre_type)
        self.assertEqual(self.game.website, g.website)
        self.assertEqual(self.game.genre, g.genre)

        

class TestGameList(TestCase):
        

    def create_game(self) -> Game:
        g = Game()
        g.title = C_TITLE
        g.genre_type = C_GENRE_TYPE
        g.website = C_WEBSITE
        g.score = C_SCORE

        return g


    def setUp(self):
        super().setUp()

        try:
            if os.path.exists(C_JSON_FILE):
                os.remove(C_JSON_FILE)
        except: # pragma: no cover
            pass

        games = GameList()
        games.add(self.create_game())
        self.games = games


    def test_length(self):
        self.assertEqual(len(self.games.items), 1)
        games = GameList()
        self.assertEqual(len(games.items), 0)
    


    def test_additem(self):
        g = self.games.add(Game())
        g.score = 2.0
        g.title = 'new game'
        g.website = 'new url'
        g.genre_type = 0

        self.assertEqual(len(self.games.items), 2)
        self.assertEqual(type(self.games.items[1]), Game)
        self.assertEqual(self.games.items[1].title, 'new game')
        
    def test_removeitem(self):
        self.games.remove(0)
        self.assertEqual(len(self.games.items), 0)


    def test_save_and_load(self):
        glist = GameList()
        glist.filename = C_JSON_FILE
        glist.add(self.create_game())
        glist.save()        
    
        self.assertTrue(os.path.exists(C_JSON_FILE))
        content = read_json_file(C_JSON_FILE)
        self.assertIn(str(C_SCORE), content)
        self.assertIn(str(C_GENRE_TYPE), content)
        self.assertIn(str(C_TITLE), content)
        self.assertIn(str(C_WEBSITE), content)
        self.assertIn('data', content)
        

        glist = GameList()
        glist.filename = C_JSON_FILE
        glist.load()        

        self.assertEqual(len(glist.items), 1)
        self.assertEqual(glist.items[0].score, C_SCORE)
        self.assertEqual(glist.items[0].genre_type, C_GENRE_TYPE)
        self.assertEqual(glist.items[0].title, C_TITLE)
        self.assertEqual(glist.items[0].website, C_WEBSITE)



if __name__ == '__main__':
    testmain()



    