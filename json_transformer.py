# =================================================================
# ========== SCRIPT TO TRANSFORM LOCATION CSV TO JSON =============
# =================================================================

import os
import csv
import sys
import json
from pathlib import Path
from typing import Dict, List, Union, Iterable


class JsonTransformer(object):
    def __init__(self, regions_path: Union[str, Path]):
        if not isinstance(regions_path, str) and not isinstance(regions_path, Path):
            raise TypeError(f"{regions_path} should be of type string or Path")

        if not os.path.isdir(regions_path):
            raise FileNotFoundError(f"The path {regions_path} does not exists")

        self.regions_path = regions_path

    # ===================================================
    # =========== LOAD ALL LOCATION CSV FILES ===========
    # ===================================================

    def load_csv_names(self) -> Iterable:
        return (
            csv_file
            for csv_file in os.listdir(self.regions_path)
            if csv_file.endswith(".csv")
        )

    # ===================================================
    # ========= TRANSFORM LIST OF LOCATION ==============
    # =========       TO JSON              ===============
    # ====================================================

    def csv_to_json(self, csv_reader) -> Dict:
        try:
            payload = {}
            for index, record_row in enumerate(csv_reader):
                change_district = False
                change_ward = False
                change_street = False
                (
                    region,
                    r_pcode,
                    district,
                    d_pcode,
                    ward,
                    w_pcode,
                    street,
                    place,
                ) = record_row

                region, district, ward, street, place, = (
                    region.capitalize(),
                    district.capitalize(),
                    ward.capitalize(),
                    street.capitalize(),
                    place.capitalize(),
                )

                if index == 0:
                    payload = {
                        region: {
                            "post_code": r_pcode,
                            "districts": {
                                district: {
                                    "district_post_code": d_pcode,
                                    "wards": {
                                        ward: {
                                            "ward_post_code": w_pcode,
                                            "streets": {street: [place]},
                                        }
                                    },
                                }
                            },
                        }
                    }

                if not district in payload[region]["districts"].keys():
                    payload[region]["districts"][district] = {
                        "district_post_code": d_pcode,
                        "wards": {
                            "ward_post_code": w_pcode,
                            ward: {"streets": {street: [place]}},
                        },
                    }

                elif not ward in payload[region]["districts"][district]["wards"].keys():
                    payload[region]["districts"][district]["wards"][ward] = {
                        "ward_post_code": w_pcode,
                        "streets": {street: [place]},
                    }

                elif (
                    not street
                    in payload[region]["districts"][district]["wards"][ward][
                        "streets"
                    ].keys()
                ):
                    payload[region]["districts"][district]["wards"][ward]["streets"][
                        street
                    ] = [place]

                elif (
                    not place
                    in payload[region]["districts"][district]["wards"][ward]["streets"][
                        street
                    ]
                ):
                    payload[region]["districts"][district]["wards"][ward]["streets"][
                        street
                    ].append(place)
            return payload
        except Exception as error:
            print(error)
            sys.exit()

    # ================================================================
    # ================  LOAD A REGION CSV AS JSON ====================
    # ================================================================

    def region_as_json(self, region_name: Union[str, Path]) -> Dict:
        try:
            if isinstance(region_name, str) or isinstance(region_name, Path):
                full_region_path = f"{self.regions_path}/{region_name}"
                with open(full_region_path, "r") as region:
                    reader = csv.reader(region, delimiter=",")
                    header = next(reader)
                    processed_json = self.csv_to_json(reader)
                    return processed_json
        except TypeError as bug:
            print(bug)
            sys.exit()

    # ==========================================================
    # ========== METHODS FOR LOADING TANZANIA ==================
    # ==========    LOCATIONS AS JSON ==========================
    # ==========================================================

    def tanzania_as_json(self) -> Dict:
        try:
            regions = self.load_csv_names()
            tanzania = {}
            for region in regions:
                region_name = region[:-4].capitalize()
                tanzania[region_name] = self.region_as_json(region)[region_name]
            return tanzania
        except TypeError as error:
            print(error)
            sys.exit()


if __name__ == "__main__":
    transformer = JsonTransformer("locations")
    with open("tanzania.json", "w") as nchi:
        country_json = transformer.tanzania_as_json()
        json.dump(country_json, nchi)