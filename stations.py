"""
Copyright 2018 Expert Analytics AS

This file is licensed under the terms of the MIT license.
See <https://github.com/expertanalytics/frost/blob/master/LICENSE>
"""

from API import Frost
import math

class Stations(Frost):
    def __init__(self,
                 latitude: float,
                 longitude: float,
                 *,
                 length_of_square: float = 10.0) -> None:
        super().__init__()
        self.stations = {}
        self.latitude = latitude
        self.longitude = longitude
        self.length_of_square = length_of_square

    def nearest_stations(self) -> None:
                        #latitude: float,
                        #longitude: float,
                        #*,
                        #length_of_square: float = 10.0) -> None:
        """
        Description:
            Finds all stations in the vicinity of the point given within a square
        Args:
            latitude:           latitude coordinate of wanted point in WGS84 
            longitude:          longitude coordinate of wanted point in WGS84 
            length_of_square:   length of side of square to search for stations
        """
        self.station_ids = {}
        #polygon = self.calculate_polygon(
        #        self.latitude, self.longitude, length_of_square=length_of_square)
        polygon = self.calculate_polygon()
        status_code, response_json = self.get_sources(geometry = f'POLYGON(({polygon}))')
        for data in response_json['data']:
            self.stations[data['id']] = data

    def calculate_polygon(self) -> str:
                          #latitude: float,
                          #longitude: float,
                          #length_of_square: float) -> str:
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
        one_deg_lon = 111.320*math.cos(math.radians(self.latitude)) # km

        length_half_side = self.length_of_square/2

        length_to_corner_lat = length_half_side/one_deg_lat # deg
        length_to_corner_lon = length_half_side/one_deg_lon # deg
       
        north = self.latitude + length_to_corner_lat
        south = self.latitude - length_to_corner_lat
        east = self.longitude + length_to_corner_lon
        west = self.longitude - length_to_corner_lon
        
        return f'{self.longitude} {north}, {self.longitude} {south},' +\
               f'{east} {self.latitude}, {west} {self.latitude},'+\
               f' {self.longitude} {north}'
    
    def oslo_test(self):
        """
        Function to test finding stations in a square of 100 km^2 around Oslo 
        center
        """
        self.nearest_stations()
        for key, value in self.stations.items():
            print(key, value)

if __name__=="__main__":
    test = Stations(latitude=59.9138688,longitude=10.752245399999993,length_of_square=11.0)
    test.oslo_test()
