"""
Copyright 2018 Expert Analytics AS

This file is licensed under the terms of the MIT license.
See <https://github.com/expertanalytics/frost/blob/master/LICENSE>
"""

from API import Frost
import math

class Station():
    def __init__(self) -> None:
        self.api = Frost()
        self.stations = {}

    def nearest_stations(self,
                        latitude: float,
                        longitude: float,
                        *,
                        length_of_square: float = 10) -> None:
        """
        Description:
            Finds all stations in the vicinity of the point given within a square
        Args:
            latitude:           latitude coordinate of wanted point in WGS84 
            longitude:          longitude coordinate of wanted point in WGS84 
            length_of_square:   length of side of square to search for stations
        """
        self.station_ids = {}
        polygon = self.calculate_polygon(latitude, longitude, length_of_square=length_of_square)
        status_code, response_json = self.api.get_sources(geometry = f'POLYGON(({polygon}))')
        for data in response_json['data']:
            self.stations[data['id']] = data

    def calculate_polygon(self,
                          latitude: float,
                          longitude: float,
                          *,
                          length_of_square: float = 10) -> str:
        """
        Description:
            Creates the latitude/longitude coordinates of corners of a square
            around the point given
        Args:
            latitude:           latitude coordinate of wanted point in WGS84 
            longitude:          longitude coordinate of wanted point in WGS84 
            length_of_square:   length of side of square to search for stations
        """

        one_deg_lat = 110.574 # km
        one_deg_lon = 111.320*math.cos(math.radians(latitude)) # km

        length_half_side = length_of_square/2

        length_to_corner_lat = length_half_side/one_deg_lat # deg
        length_to_corner_lon = length_half_side/one_deg_lon # deg
       
        north = latitude + length_to_corner_lat
        south = latitude - length_to_corner_lat
        east = longitude + length_to_corner_lon
        west = longitude - length_to_corner_lon
        
        return f'{longitude} {north}, {longitude} {south}, {east} {latitude}, {west} {latitude},'+\
                f' {longitude} {north}'

if __name__=="__main__":
    test = Station()
    test.nearest_stations(latitude=59.9138688,longitude=10.752245399999993)
    for key,value in test.stations.items():
        print(key,value)
