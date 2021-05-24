import os
import json
from pathlib import Path
from typing import Dict, Union, Iterator


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

    # ====================================================
    # ======== METHOD TO BUILD A LOCATION ================
    # ========        TREE               =================
    # ====================================================

    def tree(self, json_object=None) -> Dict:
        json_object = json_object if json_object else self.__dict__
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


# ====================================================
# ======== FUNCTION TO GET POST CODE  ================
# ====================================================

def get_postcode(payload, l_level):
    return getattr(payload, l_level, "")


# ====================================================
# ======== FUNCTION TO GROUPED LOCATIONS  ============
# ====================================================

def get_all(country, level):
    all_districts = []
    all_wards = []
    all_streets = []

    if level == 'regions':
        return list(country)

    if level == 'districts':
        for region in country:
            for district in country.get(region).districts:
                l_level = country.get(region).districts.get(district)
                post_code = get_postcode(l_level, 'district_post_code')
                all_districts.append(
                    {'post_code': post_code, 'name': district})
        return all_districts

    if level == 'wards':
        for region in country:
            for district in country.get(region).districts:
                for ward in country.get(region).districts.get(district).wards:
                    if ward == 'ward_post_code':
                        continue
                    l_level = country.get(region).districts.get(
                        district).wards.get(ward)
                    post_code = get_postcode(l_level, 'ward_post_code')
                    all_wards.append({'post_code': post_code, 'name': ward})
        return all_wards

    if level == 'streets':
        for region in country:
            for district in country.get(region).districts:
                for ward in country.get(region).districts.get(district).wards:
                    if ward == 'ward_post_code':
                        continue
                    streets = country.get(region).districts.get(
                        district).wards.get(ward).streets
                    all_streets += streets
        return all_streets


if __name__ != '__main__':
    json_path = os.path.dirname(__file__) + "/tanzania_json.py"
    tanzania = create_mtaa(json_path)
    regions = get_all(tanzania, 'regions')
    districts = get_all(tanzania, 'districts')
    wards = get_all(tanzania, 'wards')
    streets = get_all(tanzania, 'streets')
