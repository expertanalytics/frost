"""
Copyright 2018 Expert Analytics AS

This file is licensed under the terms of the MIT license.
See <https://github.com/expertanalytics/Frost/LICENSE.txt>
"""

import requests
import inspect

class Frost:
    def __init__(self) -> None:
        self.base_url = 'https://frost.met.no/'
        self.headers = {}
        with open('secrets/credentials.txt', 'r') as secrets:
            client_id, client_secret  = secrets.readlines()
            client_id = client_id.split(' # ')[0].strip()
            client_secret = client_secret.split(' # ')[0].strip()
        self.auth = requests.auth.HTTPBasicAuth(client_id,'')

    def get_elements_code_tables(self,
                                 *,
                                 ids: str = None,
                                 fields: str = None,
                                 lang: str = 'en-US') -> 'response json':
        """
        Description:
            /elements/codeTables/v0.{format}
            Get metadata about the code tables available in the Frost API. A 
            code table defines a small number of 
            discrete values for an element. Use the query parameters to filter 
            which code tables to return and what 
            fields to include for each one. Leave the query parameters blank to 
            select all code tables.
        Args:
            ids:    The code table IDs to get metadata for as a comma-separated 
                    list of search filters.
            fields: The fields to include in the output in addition to the code 
                    table name as a comma-separated list of header and values. 
                    Leave the parameter empty to include both header and 
                    values.
            lang:   ISO language/locale to be used for search filters and 
                    return values.
        """

        input_vars = inspect.getargvalues(inspect.currentframe()).locals
        del input_vars['self']
        query_parameters = self.query_parameters(input_vars)
        url = self.base_url + 'elements/codeTables/v0.jsonld?'

        response = self.get_response(url + query_parameters)
        return response.status_code, response.json() 

    def get_elements(self,
                     *,
                     ids: str = None,
                     names: str = None,
                     descriptions: str = None,
                     units: str = None,
                     code_tables: str = None,
                     statuses: str = None,
                     calculation_method: str = None,
                     categories: str = None,
                     time_offsets: str = None,
                     sensor_levels: str = None,
                     old_element_codes: str = None,
                     old_units: str = None,
                     cf_standard_names: str = None,
                     cf_cell_methods: str = None,
                     cf_units: str = None,
                     cf_statuses: str = None,
                     fields: str = None,
                     lang: str = 'en-US') -> 'response json':
        """
        Description:
            /elements/v0.{format}
            Get metadata about the weather and climate elements that are 
            defined for use in the Frost API. Use the query parameters to 
            filter which elements to return and what fields to include for each 
            element. Leave the 
            query parameters blank to select all elements.
        Args:
            ids:                The element IDs to get metadata for as a 
                                comma-separated list of search filters. An 
                                element ID is structured as a calculation 
                                method.
            names:              The element names to get metadata for as a 
                                comma-separated list of search filters.
            descriptions:	The descriptions to get metadata for as a 
                                comma-separated list of search filters.
            units:              The units to get metadata for as a 
                                comma-separated list of search filters. Note: 
                                when the unit is 'code', a codetable is in use.
            code_tables:        The code tables to get metadata for as a 
                                comma-separated list of search filters. 
                                Note: When a codetable is in use, the unit is 
                                'code'.
            statuses:           The statuses to get metadata for as a 
                                comma-separated list of search filters.
            calculation_method: The calculation method filter as a JSON filter 
                                that supports the following keys: 
                                baseNames, methods, innerMethods, periods, 
                                innerPeriods, thresholds, methodDescriptions, 
                                innerMethodDescriptions, methodUnits, and 
                                innerMethodUnits
            categories:         The categories to get metadata for as a 
                                comma-separated list of search filters.
            time_offsets:       The time offsets to get metadata for as a 
                                comma-separated list of search filters.
            sensor_levels:      The sensor levels filter as a JSON filter that 
                                supports the following keys: levelTypes, units, 
                                defaultValues, and values.
            old_element_codes:  The old MET Norway element codes to get 
                                metadata for as a comma-separated list of 
                                search filters.
            old_units:          The old MET Norway units to get metadata for as 
                                a comma-separated list of search 
                                filters.
            cf_standard_names:  The CF standard names to get metadata for as a 
                                comma-separated list of search filters.
            cf_cell_methods:    The CF cell methods to get metadata for as a 
                                comma-separated list of search filters.
            cf_units:           The CF units to get metadata for as a 
                                comma-separated list of search filters.
            cf_statuses:        The CF statuses to get metadata for as a 
                                comma-separated list of search filters.
            fields:             The information to return as a comma-separated 
                                list of id, name, description, unit, 
                                codeTable, status, cmBaseName, cmMethod, 
                                cmInnerMethod, cmPeriod, cmInnerPeriod, 
                                cmThreshold, cmMethodDescription, 
                                cmInnerMethodDescription, cmMethodUnit, 
                                cmInnerMethodUnit, category, sensorLevelType, 
                                sensorLevelUnit, sensorLevelDefaultValue, 
                                sensorLevelValues, oldElementCodes, oldUnit, 
                                cfStandardName, cfCellMethod, cfUnit, or 
                                cfStatus. For example 'id,unit,oldElementCodes,
                                oldUnit'. 
                                If omitted, all fields are returned.
            lang:               ISO language/locale to be used for search 
                                filters and return values.
        """
        input_vars = inspect.getargvalues(inspect.currentframe()).locals
        del input_vars['self']
        query_parameters = self.query_parameters(input_vars)
        url = self.base_url + 'elements/v0.jsonld?'

        response = self.get_response(url + query_parameters)
        return response.status_code, response.json() 

    def get_sources(self,
                    *,
                    ids: str = None,
                    types: str = None,
                    geometry: str = None,
                    valid_time: str = None,
                    name: str = None,
                    country: str = None,
                    county: str = None,
                    municipality: str = None,
                    wmo_id: str = None,
                    station_holder: str = None,
                    external_id: str = None,
                    icao_code: str = None,
                    ship_code: str = None,
                    wigos_id: str = None,
                    fields: str = None) -> 'response json':
        """
        Description:
            /sources/v0.{format}
            Get metadata for the source entitites defined in the Frost API. Use 
            the query parameters to filter the set of sources returned. Leave 
            the query parameters blank to select all sources.
        Args:
            ids:            The Frost API source ID(s) that you want metadata 
                            for. Enter a comma-separated list to select 
                            multiple sources. For sources of type SensorSystem 
                            or RegionDataset, the source ID must be of the form 
                            <prefix><int> where <prefix> is SN for SensorSystem 
                            and TR, NR, or GR for RegionDataset. The integer 
                            following the prefix may contain wildcards, e.g. 
                            SN18*7* matches both SN18700 and SN18007.
            types:          The type of Frost API source that you want metadata 
                            for.
            geometry:       Get Frost API sources defined by a specified 
                            geometry. Geometries are specified as either a 
                            POINT or POLYGON using WKT; see the reference 
                            section on the Geometry Specification for 
                            documentation and examples.
            valid_time:     If specified, only sources that have been, or still 
                            are, valid/applicable during some part of this 
                            interval may be included in the result. Specify 
                            <date>/<date>, <date>/now, <date>, or now, where 
                            <date> is of the form YYYY-MM-DD, e.g. 2017-03-06. 
                            The default is 'now', i.e. only currently 
                            valid/applicable sources are included.
            name:           If specified, only sources whose 'name' attribute 
                            matches this search filter may be included in the 
                            result.
            country:        If specified, only sources whose 'country' or 
                            'countryCode' attribute matches this search filter 
                            may be included in the result.
            county:         If specified, only sources whose 'county' or 
                            'countyId' attribute matches this search filter may 
                            be included in the result.
            municipality:   If specified, only sources whose 'municipality' or 
                            'municipalityId' attribute matches this search 
                            filter may be included in the result.
            wmo_id:         If specified, only sources whose 'wmoId' attribute 
                            matches this search filter may be included in the 
                            result.
            station_holder: If specified, only sources whose 'stationHolders' 
                            attribute contains at least one name that matches 
                            this search filter may be included in the result.
            external_id:    If specified, only sources whose 'externalIds' 
                            attribute contains at least one name that matches 
                            this search filter may be included in the result.
            icao_code:      If specified, only sources whose 'icaoCodes' 
                            attribute contains at least one name that matches 
                            this search filter may be included in the result.
            ship_code:      If specified, only sources whose 'shipCodes' 
                            attribute contains at least one name that matches 
                            this search filter may be included in the result.
            wigos_id:       If specified, only sources whose 'wigosId' 
                            attribute matches this search filter may be 
                            included in the result.
            fields:         A comma-separated list of the fields that should be 
                            present in the response. If set, only those 
                            properties listed here will be visible in the 
                            result set; e.g.: name,country will show only those 
                            two entries in the result in addition to the id 
                            which is always shown.
        """
        input_vars = inspect.getargvalues(inspect.currentframe()).locals
        del input_vars['self']
        query_parameters = self.query_parameters(input_vars)
        url = self.base_url + 'sources/v0.jsonld?'

        response = self.get_response(url + query_parameters)
        return response.status_code, response.json() 
     
    def get_locations(self,
                      *,
                      names: str = None,
                      geometry: str = None,
                      fields: str = None) -> 'response json':
        """
        Description:
            /locations/v0.{format} 
            Get metadata for the location names defined in the Frost API. Use 
            the query parameters to filter the set of location names returned. 
            Leave the query parameters blank to select all location names.
        Args:
            names:      The Frost API location names that you want metadata 
                        for. Enter a comma-separated list to select multiple 
                        location names. Leave blank to get all names.
            geometry:   Get Frost API location names by geometry. Geometries 
                        are specified as either a POINT or POLYGON using WKT; 
                        see the reference section on the Geometry Specification 
                        for documentation and examples.
            fields:     A comma-separated list of the fields that should be 
                        present in the response. If set, only those properties 
                        listed here will be visible in the result set; e.g.: 
                        name,geometry will show only those two entries in the 
                        data set.
        """
        input_vars = inspect.getargvalues(inspect.currentframe()).locals
        del input_vars['self']
        query_parameters = self.query_parameters(input_vars)
        url = self.base_url + 'locations/v0.jsonld?'

        response = self.get_response(url + query_parameters)
        return response.status_code, response.json() 

    def get_records(self,
                    *,
                    sources: str = None,
                    source_names: str = None,
                    counties: str = None,
                    municipalities: str = None,
                    elements: str = None,
                    months: str = None,
                    fields: str = None) -> 'response json':
        """
        Description:
            /records/countyExtremes/v0.{format}
            Get records. To be expanded.
        Args:
            sources:        The sources to get records for as a comma-separated 
                            list of search filters. If left out, the output is 
                            not filtered on source.
            source_names:   The source names to get records for as a 
                            comma-separated list of search filters. If left 
                            out, the output is not filtered on source name.
            counties:       The counties to get records for as a 
                            comma-separated list of search filters. If left 
                            out, the output is not filtered on county.
            municipalities: The municipalities to get records for as a 
                            comma-separated list of search filters. If left 
                            out, the output is not filtered on municipality.
            elements:       The elements to get records for as a 
                            comma-separated list of search filters. If left 
                            out, the output is not filtered on element.
            months:         The months to get records for as a comma-separated 
                            list of integers or integer ranges 
                            between 1 and 12, e.g. '1,5,8-12'. If left out, 
                            the output is not filtered on month.
            fields:         The information to return as a comma-separated list 
                            of 'sourceid', 'sourcename', 'county', 
                            'municipality', 'elementid', 'month', 
                            'referencetime', or 'value'. For example 
                            'county,month,referencetime1,elementid,value'. If 
                            omitted, all fields are returned.
        """
        input_vars = inspect.getargvalues(inspect.currentframe()).locals
        del input_vars['self']
        query_parameters = self.query_parameters(input_vars)
        url = self.base_url + 'records/countyExtremes/v0.jsonld?'

        response = self.get_response(url + query_parameters)
        return response.status_code, response.json() 

    def get_observations_available_time_series(self,
                                               *,
                                               sources: str = None,
                                               reference_time: str = None,
                                               elements: str = None,
                                               time_offsets: str = None,
                                               time_resolutions: str = None,
                                               time_series_id: str = None,
                                               performance_categories: str = None,
                                               exposure_categories: str = None,
                                               levels: str = None,
                                               level_types: str = None,
                                               fields: str = None) -> (int, 'response json'):
        """
        Description:
            /observations/availableTimeSeries/v0.{format} 
            Find timeseries metadata by source and/or element
        Args:
            sources:                The ID(s) of the data sources to get time 
                                    series for as a comma-separated list of 
                                    Frost API station IDs: SN<int>[:<int>|all] 
                                    (e.g. SN18700, SN18700:0, or SN18700:all). 
                                    0 is the main sensor and x>=1 is a parallel 
                                    sensor. Retrieve the complete station lists 
                                    using the sources resource. If left out, 
                                    time series for all available stations are 
                                    retrieved.
            reference_time:         The time range to get time series for as 
                                    extended ISO-8601 format. See Time 
                                    Specifications for documentation and 
                                    examples. If left out, time series for all 
                                    available periods are retrieved.
            elements:               The elements to get time series for as a 
                                    comma-separated list of search filters. 
                                    Elements follow the Frost API naming 
                                    convention. Available element names can be 
                                    found here. If left out, time series for 
                                    all available elements are retrieved.
            time_offsets:           The time offsets to get time series for as 
                                    a comma-separated list of ISO-8601 periods, 
                                    e.g. 'PT6H,PT18H'. If left out, the output 
                                    is not filtered on time offset.
            time_resolutions:       The time resolutions to get time series for 
                                    as a comma-separated list of ISO-8601 
                                    periods, e.g. 'PT6H,PT18H'. If left out, 
                                    the output is not filtered on time 
                                    resolution.
            time_series_ids:        The internal time series IDs to get time 
                                    series for as a comma-separated list of 
                                    integers, e.g. '0,1'. If left out, the 
                                    output is not filtered on internal time 
                                    series ID.
            performance_categories: The performance categories to get time 
                                    series for as a comma-separated list of 
                                    letters, e.g. 'A,C'. If left out, the 
                                    output is not filtered on performance 
                                    category.
            exposure_categories:    The exposure categories to get time series 
                                    for as a comma-separated list of integers, 
                                    e.g. '1,2'. If left out, the output is not 
                                    filtered on exposure category.
            levels:                 The sensor levels to get observations for 
                                    as a comma-separated list of numbers, e.g. 
                                    '0.1,2,10,20'. If left out, the output is 
                                    not filtered on sensor level.
            level_types:            The sensor level types to get records for 
                                    as a comma-separated list of search 
                                    filters. If left out, the output is not 
                                    filtered on sensor level type.
            level_units:            The sensor level units to get records for 
                                    as a comma-separated list of search 
                                    filters. If left out, the output is not 
                                    filtered on sensor level unit.
            fields:                 Fields to include in the output as a 
                                    comma-separated list. If specified, only 
                                    these fields are included in the output. If 
                                    left out, all fields are included.
        """
        input_vars = inspect.getargvalues(inspect.currentframe()).locals
        del input_vars['self']
        query_parameters = self.query_parameters(input_vars)
        url = self.base_url + 'observations/availableTimeSeries/v0.jsonld?'

        response = self.get_response(url + query_parameters)
        return response.status_code, response.json() 

    def get_observations_quality(self,
                                 flags: str,
                                 *,
                                 fields: str = None,
                                 lang: str = 'en-US') -> (int, 'response json'):
        """
        Description:
            /observations/quality/v0.{format} 
            Get detailed information about the quality of an observation. This 
            provides detailed information about an observation's parameter's 
            quality.
        Args:
            flags:  The quality flag combination you want information about. 
                    Normally, you should get this from an observations call.
            fields: Fields to access
            lang:   ISO language/locale of return values.
        """
        input_vars = inspect.getargvalues(inspect.currentframe()).locals
        print(input_vars)
        del input_vars['self']
        query_parameters = self.query_parameters(input_vars)
        url = self.base_url + 'observations/quality/v0.jsonld?'


        response = self.get_response(url + query_parameters)
        return response.status_code, response.json() 

    def get_observations_available_quality_codes(self,
                                                 *,
                                                 lang: str = 'en-US',
                                                 fields: str = None) -> (int, 'response json'):
        """
        Descripton:
            /observations/availableQualityCodes/v0.{format} 
            Get information about the existing quality flags. This provides a 
            list of all possible detail values given in the quality service.
        Args:
            lang: ISO language/locale of return values.
            fields: Fields to access
        """
        input_vars = inspect.getargvalues(inspect.currentframe()).locals
        del input_vars['self']
        query_parameters = self.query_parameters(input_vars)
        url = self.base_url + 'observations/availableQualityCodes/v0.jsonld?'
        
        response = self.get_response(url + query_parameters)
        return response.status_code, response.json() 

    def get_observations(self,
                         sources: str,
                         reference_time: str,
                         elements: str,
                         *,
                         time_offsets: str = None,
                         time_resolutions: str = None,
                         performance_categories: str = None,
                         exposure_categories: str = None,
                         levels: str = None,
                         fields: str = None) -> (int, 'response json'):
        """
        Description:
            /observations/v0.{format} 
            Get observation data from the Frost API. This is the core resource 
            for retrieving the actual observation data from MET Norway's data 
            storage systems. The query parameters act as a filter; if all were 
            left blank (not allowed in practice), one would retrieve all of the 
            observation data in the system. Restrict the data using the query 
            parameters. For possible input parameters see /sources, /elements, 
            and /observations/timeseries.
        Args:
            sources:                The ID(s) of the data sources to get 
                                    observations for as a comma-separated list 
                                    of Frost API station IDs, e.g. SN18700 for 
                                    Blindern. Retrieve the complete station 
                                    lists using the sources resource.
            reference_time:         The time range to get observations for in 
                                    either extended ISO-8601 format or the 
                                    single word 'latest'. See Time 
                                    Specifications for documentation and 
                                    examples.
            elements:               The elements to get observations for as a 
                                    comma-separated list of names that follow 
                                    the Frost API naming convention. Available 
                                    element names can be found here.
            time_offsets:           The time offsets to get observations for as 
                                    a comma-separated list of ISO-8601 
                                    periods, e.g. 'PT6H,PT18H'. If left out, 
                                    the output is not filtered on time offset.
            time_resolutions:       The time resolutions to get observations 
                                    for as a comma-separated list of ISO-8601 
                                    periods, e.g. 'PT6H,PT18H'. If left out, 
                                    the output is not filtered on time 
                                    resolution.
            time_series_ids:        The internal time series IDs to get 
                                    observations for as a comma-separated list 
                                    of integers, e.g. '0,1'. If left out, the 
                                    output is not filtered on internal time 
                                    series ID.
            performance_categories: The performance categories to get 
                                    observations for as a comma-separated list 
                                    of letters, e.g. 'A,C'. Enter a 
                                    comma-separated list to specify multiple 
                                    performance categories. If left out, the 
                                    output is not filtered on performance 
                                    category.
            exposure_categories:    The exposure categories to get observations 
                                    for as a comma-separated list of integers, 
                                    e.g. '1,2'. If left out, the output is not 
                                    filtered on exposure category.
            levels:                 The sensor levels to get observations for 
                                    as a comma-separated list of numbers, 
                                    e.g. '0.1,2,10,20'. If left out, the output 
                                    is not filtered on sensor level.
            fields:                 Fields to include in the output as a 
                                    comma-separated list. If specified, only 
                                    these fields are included in the output. If 
                                    left out, all fields are included.
        """
        input_vars = inspect.getargvalues(inspect.currentframe()).locals
        del input_vars['self']
        query_parameters = self.query_parameters(input_vars)
        url = self.base_url + 'observations/v0.jsonld?'

        response = self.get_response(url + query_parameters)
        return response.status_code, response.json() 

    def get_response(self,
                     url: str) -> 'GET response':
        with requests.get(url, headers=self.headers, auth=self.auth) as response:
            if not response.status_code == 200:
                print(f'Response code {response.status_code}, from url {url}')
                print(f'Error: {response.json()["error"]}')
                raise AssertionError()
            else:
                print(f'Response code: {response.status_code}, GET {url}')
                return response

    def query_parameters(self, input_vars) -> str:
        query_parameters = ''
        for key, value in input_vars.items():
            if not value == None:
                key = key.replace('_','')
                if not query_parameters:
                    query_parameters+= f'{key}={value}'
                else:
                    query_parameters+= f'&{key}={value}'
        return query_parameters

    def test_gets(self) -> None: 
        status_code, response_json = self.get_elements_code_tables()
        status_code, response_json = self.get_elements() 
        status_code, response_json = self.get_sources() 
        status_code, response_json = self.get_locations()
        status_code, response_json = self.get_records() 
        status_code, response_json = self.get_observations_available_time_series() 
        status_code, response_json = self.get_observations_available_quality_codes() 
        status_code, response_json = self.get_observations(sources = 'SN18700',
                                                           reference_time = 'latest',
                                                           elements='air_pressure_at_sea_level') 
        status_code, response_json = self.get_observations_quality(flags=70000)

if __name__=='__main__':
    test = Frost()
    test.test_gets()
