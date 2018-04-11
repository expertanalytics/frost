"""
Copyright 2018 Expert Analytics AS

This file is licensed under the terms of the MIT license.
See <https://github.com/expertanalytics/frost/blob/master/LICENSE>
"""

from API import Frost
import math

class Stations(Frost):
    """
    Description:
        Finds all stations within a square of chosen size from a point with 
        WGS84 coordinates and collects available observational data from each
        station
    """
    def __init__(self,
                 latitude: float,
                 longitude: float,
                 *,
                 length_of_square: float = 10.0) -> None:
        """
        Description:
            Class instance initialization
        Args:
            latitude:           latitudal coordinate
            longitude:          longitudal coordinate
            length_of_square:   length of side of square in km
        """
        super().__init__()
        self.stations = {}
        self.latitude = latitude
        self.longitude = longitude
        self.length_of_square = length_of_square

    def has(self,
            *,
            data_type: str = None,
            show_all: bool = True) -> None:
        """
        Description:
            To be done
        Args:
            data_type:  which observational data type to look for
            show_all:   see all available data types from each station
        """
        station_ids = ','.join(i for i in self.stations)
        for station_id in self.stations:
            self.stations[station_id]['available'] = []
        sc, r_json = self.get_observations_available_time_series(sources=station_ids)
        for point in r_json['data']:
            self.stations[point['sourceId'][:7]]['available'].append(point)

        if data_type:
            for station_id, data in self.stations.items(): 
                print(f'Available data for station {station_id}:')
                print('{:25}{:63}{:20}'.format('Valid from','data type', 'time resolution'))
                for time_series in data['available']:
                    if data_type in time_series['elementId']:
                        print(f'{time_series["validFrom"]:25}{time_series["elementId"]:63}' +\
                                f'{time_series["timeResolution"]:20}')
                print('')

        elif show_all:
            for station_id, data in self.stations.items():
                print(f'Available data for station {station_id}:')
                print('{:25}{:63}{:20}'.format('Valid from','data type', 'time resolution'))
                for time_series in data['available']:
                    print(f'{time_series["validFrom"]:25}{time_series["elementId"]:63}' +\
                            f'{time_series["timeResolution"]:20}')
                print('')



    def nearest_stations(self) -> None:
        """
        Description:
            Finds all stations in the vicinity of the point given within a square
        Args:
            latitude:           latitude coordinate of wanted point in WGS84 
            longitude:          longitude coordinate of wanted point in WGS84 
            length_of_square:   length of side of square to search for stations
        """
        self.station_ids = {}
        polygon = self.calculate_polygon()
        status_code, response_json = self.get_sources(geometry = f'POLYGON(({polygon}))')
        for data in response_json['data']:
            self.stations[data['id']] = data
        self.distance() 

    def calculate_polygon(self) -> str:
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

        length_to_corner_lat = length_half_side/one_deg_lat
        length_to_corner_lon = length_half_side/one_deg_lon
       
        north = self.latitude + length_to_corner_lat
        south = self.latitude - length_to_corner_lat
        east = self.longitude + length_to_corner_lon
        west = self.longitude - length_to_corner_lon

        return f'{self.longitude} {north}, {self.longitude} {south},' +\
               f'{east} {self.latitude}, {west} {self.latitude},'+\
               f' {self.longitude} {north}'
    
    def distance(self) -> None:
        """
        Description:
            Calculates distance from original point to each station and adds it
            to the correspondng stations dictionary
        """
        point_lat_rad = math.radians(self.latitude)
        point_lon_rad = math.radians(self.longitude)
        for station, data in self.stations.items():
            lon, lat =  data['geometry']['coordinates']
            lat_rad = math.radians(lat)
            lon_rad = math.radians(lon)
            x = (lon_rad - point_lon_rad)*math.cos((point_lat_rad + lat_rad)/2)
            y = lat_rad - point_lat_rad
            self.stations[station]['distance'] = math.sqrt(x*x + y*y)
        

    def oslo_test(self) -> None:
        """
        Descripton:
            Function to test finding stations within a squar around Oslo center
        """
        self.nearest_stations()
        for key, value in self.stations.items():
            print(key, value)

if __name__=="__main__":
    test = Stations(latitude=59.9138688,longitude=10.752245399999993,length_of_square=11.0)
    test.nearest_stations()
    #for key, value in test.stations.items():
    #    print(value['distance'])
    test.has(data_type = 'precipitation')
    #test.oslo_test()
