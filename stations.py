"""
Copyright 2018 Expert Analytics AS

This file is licensed under the terms of the MIT license.
See <https://github.com/expertanalytics/frost/blob/master/LICENSE>
"""

from API import Frost
import math
import datetime

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
        self.find_stations()
        self.has()

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

        title_head = 'Available data for station {}, {}, distance {}:'
        if data_type:
            for station_id, data in self.stations.items():
                try:
                    print(title_head.format(station_id, data["shortName"], data["distance"]))
                except KeyError as error:
                    print(title_head.format(station_id, data["name"], data["distance"]))
                print('{:25}{:63}{:20}'.format('Valid from','data type', 'time resolution'))
                for time_series in data['available']:
                    if data_type in time_series['elementId']:
                        print(f'{time_series["validFrom"]:25}{time_series["elementId"]:63}' +\
                                f'{time_series["timeResolution"]:20}')
                print('')

        elif show_all:
            for station_id, data in self.stations.items():
                try:
                    print(title_head.format(station_id, data["shortName"], data["distance"]))
                except KeyError as error:
                    print(title_head.format(station_id, data["name"], data["distance"]))
                print('{:25}{:63}{:20}'.format('Valid from','data type', 'time resolution'))
                for time_series in data['available']:
                    print(f'{time_series["validFrom"]:25}{time_series["elementId"]:63}' +\
                            f'{time_series["timeResolution"]:20}')
                print('')

    def find_stations(self) -> None:
        """
        Description:
            Finds all stations in the vicinity of the point given within a
            square
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
               f' {east} {self.latitude}, {west} {self.latitude},'+\
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

    def observational_data(self,
                           source: str,
                           *,
                           elements: list = ['air_temperature'],
                           repeat: int = 0,
                           seperation: str = None,
                           start_time: 'datetime.datetime' = None,
                           end_time: 'datetime.datetime' = None) -> None:
        """
        Description:
            A simplified observations call for one station. For a fully
            customizable call, see documentation in API.get_observations()
        Args:
            elements:   list of which data type to access
            source:     station ID
            repeat:     how many times to repeat interval
            seperation: seperation between observations, ex 1D is 1 day 
                        duration between each interval
            start_time: starting time of observational data wanted
            end_time:   end time of observational data wanted
        """
        #if not sources:
        #    sources = ','.join(source for source in self.stations)
        #else:
        #    sources = ','.join(source for source in sources)
        elements = ','.join(element for element in elements)
        time_string = self.convert_datetime(repeat = repeat,
                                            seperation = seperation,
                                            start_time = start_time,
                                            end_time = end_time)
        return self.get_observations(sources = source,
                                     reference_time = time_string,
                                     elements = elements)
                                     
    def observation_air_temperature(self,
                                    source: str,
                                    *,
                                    repeat: int = 0,
                                    seperation: str = None,
                                    start_time: 'datetime.datetime' = None,
                                    end_time: 'datetime.datetime' = None) -> None:
        """
        Description:
            A simplified observations call for air temperature for  one station 
        Args:
            source:     station ID
            repeat:     how many times to repeat interval
            seperation: seperation between observations, ex 1D is 1 day 
                        duration between each interval
            start_time: starting time of observational data wanted
            end_time:   end time of observational data wanted
        """
        return self.observational_data(source = source,
                                       elements = ['air_temperature'],
                                       repeat = repeat,
                                       seperation = seperation,
                                       start_time = start_time,
                                       end_time = end_time)

    def observation_precipitation_amount(self,
                                         source: str,
                                         *,
                                         repeat: int = 0,
                                         seperation: str = None,
                                         start_time: 'datetime.datetime' = None,
                                         end_time: 'datetime.datetime' = None) -> None:
        """
        Description:
            A simplified observations call for percepitation amount for one 
            station 
        Args:
            source:     station ID
            repeat:     how many times to repeat interval
            seperation: seperation between observations, ex 1D is 1 day 
                        duration between each interval
            start_time: starting time of observational data wanted
            end_time:   end time of observational data wanted
        """
        return self.observational_data(source = source,
                                       elements = ['precipitation_amount'],
                                       repeat = repeat,
                                       seperation = seperation,
                                       start_time = start_time,
                                       end_time = end_time)

    def oslo_test(self) -> None:
        """
        Descripton:
            Function to test finding stations within a square around Oslo 
            center
        """
        self.find_stations()
        for key, value in self.stations.items():
            print(key, value)

if __name__=="__main__":
    test = Stations(latitude=59.9138688,longitude=10.752245399999993,length_of_square=20.0)
    closest = ''
    for station, data in test.stations.items():
        available_data_types = [avail['elementId'] for avail in data['available']]
        if closest:
            close = test.stations[closest]
            if data['distance'] < close['distance']:
                if any('precipitation_amount' == data_type for data_type in available_data_types):
                    closest = station
        elif any('precipitation_amount' == data_type for data_type in available_data_types):
            closest = station
        print(closest)
    #sc, r_json = test.observational_data(source = closest,
    #                                     elements = ['air_temperature'],
    #                                     start_time = datetime.datetime(2018, 1, 1))
    #sc, r_json = test.observation_precipitation_amount(source = closest)
    #for data in r_json['data']:
    #    print(data['referenceTime'])
    #    for obs in data['observations']:
    #        print(obs)
    #test.has(data_type = 'precipitation')
    #test.has()
    #test.oslo_test()