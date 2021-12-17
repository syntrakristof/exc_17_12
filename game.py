from base import BaseObject, BaseList
from typing import Optional, Any

genre_types = set(['Unknown', 'FPS', 'RPG', 'MMO', 'Arcade', 'Racing'])


class Game(BaseObject):

    def __init__(self):
        self.__title = ''
        self.__score = 0.0
        self.__genre_type = 0
        self.__website = ''

    
    @property
    def title(self) -> str:
        return self.__title
    
    @title.setter
    def title(self, value: str):
        self.title = value
    

    @property
    def score(self) -> float:
        return self.__score

    @score.setter
    def score(self, value: float):
        if value >= 0.0 and value <= 10.0:
            self.__score = value
        else:
            raise ValueError('score must be from 0 to 10')
    
    @property
    def genre_type(self) -> int:
        return self.__genre_type
    
    @genre_type.setter
    def genre_type(self, value: int):
        if value >=0 and value < len(genre_types):
            self.__genre_type = value
        else:
            raise ValueError('must be in range of genre_types')

    @property
    def genre(self) -> str:
        return genre_types[self.__genre_type]


    @property
    def website(self) -> str:
        return self.__website


    @property
    def website(self, value: str):
        self.__website = value


    def _get_dict(self) -> dict:
        return dict(
            website=self.website,
            genre_types=self.genre_type,
            title=self.title,
            score=self.score
        )

    def _set_dict(self, value):
        pass

    def fromDict(cls, value: dict) -> Any:
        return None




        
