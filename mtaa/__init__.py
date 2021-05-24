import os
import json
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, Union, Iterator


@dataclass
class Tanzania(object):

    # ========================================================
    # ======== RECURSIVE CONSTRUCTOR TO CREATE ===============
    # ========    LOCATION OBJECTS WE NEED     ===============
    # ========================================================

    def __init__(self, **raw_data: Dict) -> None:
        for key, value in raw_data.items():
            if isinstance(value, dict):
                self.__dict__[key] = Tanzania(**value)
            else:
                self.__dict__[key] = value

    # =====================================================
    # ========= METHOD TO BUILD REPRENTATION ==============
    # =========       STRING                 ==============
    # =====================================================

    def __repr__(self) -> str:
        items = list(self.__dict__.keys())
        return f"{items}"

    # =====================================================
    # ======       METHOD THAN RETURNS A ==================
    # ======            ITERATOR       ====================
    # =====================================================

    def __iter__(self) -> Iterator:
        return iter(self.__dict__.keys())

    # ====================================================
    # =========== METHOD TO GET A LOCATION ===============
    # ===========         LEVEL           ================
    # ====================================================

    def get(self, location_level: str):
        if not isinstance(location_level, str):
            raise TypeError(
                f'{location_level} must be of type<str> not {type(location_level)}')
        return self.__dict__.get(location_level, None)

    def get_dict(self):
        return self.__dict__

    # ====================================================
    # ======== METHOD TO BUILD A LOCATION ================
    # ========        TREE               =================
    # ====================================================

    def tree(self, json_object=None) -> Dict:
        json_object = json_object if json_object else self.get_dict()
        data_tree = {}
        for key, value in json_object.items():
            if isinstance(value, Tanzania):
                data_tree[key] = self.tree(value.__dict__)
            else:
                data_tree[key] = value
        return data_tree


# ========================================================
# =========== FUNCTION TO CREATE TZ OBJECT ===============
# ========================================================


def create_mtaa(json_path: Union[str, Path]) -> Tanzania:
    tanzania_as_json = json.load(open(json_path))
    return Tanzania(**tanzania_as_json)


if __name__ != "__main__":
    json_path = os.path.dirname(__file__) + "/tanzania.py"
    tanzania = create_mtaa(json_path)
