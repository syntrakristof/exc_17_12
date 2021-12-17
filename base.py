from json import dumps, loads
from files import read_json_file, create_json_file
from typing import Any, List,  Optional
from abc import ABC, abstractmethod, abstractclassmethod

class BaseObject(ABC):

    @abstractmethod
    def _get_dict(self) -> dict:
        pass # pragma: no cover

    @abstractmethod    
    def _set_dict(self, value):
        pass # pragma: no cover

    @abstractclassmethod
    def fromDict(cls, value: dict) -> Any:
        pass # pragma: no cover 

    @property
    def as_dict(self) -> dict:
        return self._get_dict()
    
    @as_dict.setter
    def as_dict(self, value: dict):
        self._set_dict(value)

    @property
    def as_json(self) -> str:
        return dumps(self.as_dict)

    @as_json.setter
    def as_json(self, value: str):
        ddict = loads(value)
        self.as_dict = ddict
        


class BaseList():  
    __filename = 'base.json'
    __classtype = None

    def __init__(self, classtype, filename: str =''):
        self.__items: List[Any] = []
        if filename != '':
            self.__filename = filename
        self.__classtype = classtype

    @property
    def items(self) -> List[Any]:
        return self.__items

    @property
    def filename(self) -> str:
        return self.__filename

    @filename.setter
    def filename(self, value):
        self.__filename = value

    @property
    def as_dict(self) -> dict:
        mylist: List[Any] = []
        for item in self.items:
            mylist.append(item.as_dict)

        output = {}
        output['data'] = mylist

        return output

    @as_dict.setter
    def as_dict(self, value: dict):
        mylist = value["data"]
        self.__items.clear()
        for item in mylist:
            obj: Optional[Any] = self.__classtype.fromDict(item)
            self.items.append(obj)

    @property
    def as_json(self) -> str:
        return dumps(self.as_dict)

    @as_json.setter
    def as_json(self, value: str):
        if value != '':
            d = loads(value)
            self.as_dict = d

    def save(self):
        """save the list
        """
        create_json_file(self.as_json, self.__filename)

    def load(self):
        """load the contents of this list
        """
        filecontents = read_json_file(self.__filename)
        if filecontents != '':
            # clear stuff first
            self.__items.clear()
            self.as_json = filecontents

    
    def add(self, obj):
        """add an object to the internal list

        Args:
            obj (Object): an object
        """
        if obj is not None:
            self.__items.append(obj)
            return obj
            
    def remove(self, nr: int):
        """remove an object by id

        Args:
            nr (int): index in the list
        """
        if (nr > -1)and (nr < len(self.__items)):
            del self.__items[nr]


