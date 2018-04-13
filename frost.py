"""
Copyright 2018 Expert Analytics AS

This file is licensed under the terms of the MIT license.
See <https://github.com/expertanalytics/frost/blob/master/LICENSE>
"""

import sys
import inspect
import requests
import datetime
import math

class API:
    def __init__(self) -> None:
        self.base_url = 'https://frost.met.no/'
        self.headers = {}
        self.api_version = '0'
        try:
            with open('secrets/credentials.txt', 'r') as secrets:
                client_id, client_secret  = secrets.readlines()
                client_id = client_id.split(' # ')[0].strip()
                client_secret = client_secret.split(' # ')[0].strip()
            self.auth = requests.auth.HTTPBasicAuth(client_id,'')
        except FileNotFoundError as error:
            print('You need a secrets folder with a text file called credentials.txt with your ' +\
                  'credentials in it, see README.md for details')
            sys.exit(1)
        self.stations = {}

    def get_elements_code_tables(self,
                                 *,
                                 ids: str = None,
                                 fields: str = None,
                                 lang: str = 'en-US') -> (int, 'response json'):
        """
        Description:
            GET /elements/codeTables/v0.{format}
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
        url = self.base_url + f'elements/codeTables/v{self.api_version}.jsonld?'

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
                     lang: str = 'en-US') -> (int, 'response json'):
        """
        Description:
            GET /elements/v0.{format}
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
        url = self.base_url + f'elements/v{self.api_version}.jsonld?'

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
                    fields: str = None) -> (int, 'response json'):
        """
        Description:
            GET /sources/v0.{format}
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
        url = self.base_url + f'sources/v{self.api_version}.jsonld?'

        response = self.get_response(url + query_parameters)
        return response.status_code, response.json() 
     
    def get_locations(self,
                      *,
                      names: str = None,
                      geometry: str = None,
                      fields: str = None) -> (int, 'response json'):
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
        url = self.base_url + f'locations/v{self.api_version}.jsonld?'

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
                    fields: str = None) -> (int, 'response json'):
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
        url = self.base_url + f'records/countyExtremes/v{self.api_version}.jsonld?'

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
            GET /observations/availableTimeSeries/v0.{format} 
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
        url = self.base_url + f'observations/availableTimeSeries/v{self.api_version}.jsonld?'

        response = self.get_response(url + query_parameters)
        return response.status_code, response.json() 

    def get_observations_quality(self,
                                 flags: str,
                                 *,
                                 fields: str = None,
                                 lang: str = 'en-US') -> (int, 'response json'):
        """
        Description:
            GET /observations/quality/v0.{format} 
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
        del input_vars['self']
        query_parameters = self.query_parameters(input_vars)
        url = self.base_url + f'observations/quality/v{self.api_version}.jsonld?'


        response = self.get_response(url + query_parameters)
        return response.status_code, response.json() 

    def get_observations_available_quality_codes(self,
                                                 *,
                                                 lang: str = 'en-US',
                                                 fields: str = None) -> (int, 'response json'):
        """
        Descripton:
            GET /observations/availableQualityCodes/v0.{format} 
            Get information about the existing quality flags. This provides a 
            list of all possible detail values given in the quality service.
        Args:
            lang: ISO language/locale of return values.
            fields: Fields to access
        """
        input_vars = inspect.getargvalues(inspect.currentframe()).locals
        del input_vars['self']
        query_parameters = self.query_parameters(input_vars)
        url = self.base_url + f'observations/availableQualityCodes/v{self.api_version}.jsonld?'
        
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
            GET /observations/v0.{format} 
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
        url = self.base_url + f'observations/v{self.api_version}.jsonld?'

        response = self.get_response(url + query_parameters)
        return response.status_code, response.json() 

    def get_climate_normals(self,
                            sources: str,
                            *,
                            elements: str = None,
                            period: str = None) -> (int, 'response json'):
        """
        Description:
            GET /climatenormals/v0.{format}
            Get climate normals. To be expanded.
        Args:
            sources:    The sources to get climate normals for as a 
                        comma-separated list. Each source should be of the form 
                        SN<number>.
            elements:   The elements to get climate normals for as a 
                        comma-separated list of search filters.
            period:     The validity period, e.g. '1931/1960'. If specified, 
                        only climate normals for this period will be returned.
        """

        input_vars = inspect.getargvalues(inspect.currentframe()).locals
        del input_vars['self']
        query_parameters = self.query_parameters(input_vars)
        url = self.base_url + f'climatenormals/v{self.api_version}.jsonld?'

        response = self.get_response(url + query_parameters)
        return response.status_code, response.json() 

    def get_climate_normals_available(self,
                                      *,
                                      sources: str = None,
                                      elements: str = None,
                                      periods: str = None,
                                      fields: str = None) -> (int, 'response json'):
        """
        Description:
            GET /climatenormals/available/v0.{format}
            Get available combinations of sources, elements, and periods for 
            climate normals. To be expanded.
        Args:
            sources:    If specified, only combinations matching these sources 
                        may be included in the output. Enter a comma-separated 
                        list of sources of the form SN<number>. If omitted, any 
                        source will match.
            elements:   If specified, only combinations matching these elements 
                        may be included in the output. Enter a comma-separated 
                        list of element names in the form of search filters. If 
                        omitted, any element will match.
            periods:    If specified, only combinations matching these validity 
                        periods may be included in the output. Enter a 
                        comma-separated list of validity period of the form 
                        '<from year>/<to year>', e.g. '1931/1960'. If omitted, 
                        any period will match.
            fields:     Specifies what information to return as a 
                        comma-separated list of 'sourceid', 'elementid', or 
                        'period'. For example, 'sourceid,period' specifies that 
                        only source IDs and periods will appear in the output. 
                        If omitted, all fields are returned.
        """

        input_vars = inspect.getargvalues(inspect.currentframe()).locals
        del input_vars['self']
        query_parameters = self.query_parameters(input_vars)
        url = self.base_url + f'climatenormals/available/v{self.api_version}.jsonld?'

        response = self.get_response(url + query_parameters)
        return response.status_code, response.json() 

    def get_frequencies_rainfall(self,
                                 *,
                                 sources: str = None,
                                 location: str = None,
                                 duration: str = None,
                                 frequencies: str = None,
                                 unit: str = None,
                                 fields: str = None) -> (int, 'response json'):
        """
        Description:
            GET /frequencies/rainfall/v0.{format}
            Get rainfall IDF data. To be expanded.
        Args:
            sources:        The Frost API source ID(s) that you want IDF data 
                            for. Enter either a comma-separated list of one or 
                            more stations (each of the form 
                            SN<number>[:<number>|all]), or the name of a 
                            gridded dataset. If left out, IDF data for all 
                            available station sources is returned.
            location:       The geographic position from which to get IDF data 
                            in case of a gridded dataset. Format: 
                            POINT(<longitude degrees> <latitude degrees>). Data 
                            from the nearest grid point is returned.
            durations:      The Frost API IDF duration(s), in minutes, that you 
                            want IDF data for. Enter a comma-separated list to 
                            select multiple durations.
            frequencies:    The Frost API IDF frequencies (return periods), in 
                            years, that you want IDF data for. Enter a 
                            comma-separated list to select multiple 
                            frequencies.
            unit:           The unit of measure for the intensity. Specify 'mm' 
                            for millimetres per minute multiplied by the 
                            duration, or 'l/sHa' for litres per second per 
                            hectar. The default unit is 'l/sHa'
            fields:         A comma-separated list of the fields that should be 
                            present in the response. The sourceId and values 
                            attributes will always be returned in the query 
                            result. Leaving this parameter empty returns all 
                            attributes; otherwise only those properties listed 
                            will be visible in the result set (in addition to 
                            the sourceId and values); e.g.: 
                            unit,numberOfSeasons will show only sourceId, unit, 
                            numberOfSeasons, and values in the response.
        """

        input_vars = inspect.getargvalues(inspect.currentframe()).locals
        del input_vars['self']
        query_parameters = self.query_parameters(input_vars)
        url = self.base_url + f'frequencies/rainfall/v{self.api_version}.jsonld?'

        response = self.get_response(url + query_parameters)
        return response.status_code, response.json() 
        
    def get_frequencies_rainfall_available_sources(self,
                                                   *,
                                                   sources: str = None,
                                                   types: str = None,
                                                   fields: str = None) -> (int, 'response json'):
        """
        Description:
            GET /frequencies/rainfall/availableSources/v0.{format} 
            Get available sources for rainfall IDF data.
        Args:
            sources:    The Frost API source ID(s) that you want information 
                        for. Enter either a comma-separated list of one or more 
                        stations (each of the form SN<number>[:<number>|all]), 
                        or the name of a gridded dataset. If left out, 
                        information for all available sources is returned.
            types:      The type(s) of Frost API source that you want 
                        information for. Enter a comma-separated list to select 
                        multiple types.
            fields:     A comma-separated list of the fields that should be 
                        present in the response. The sourceId attribute will 
                        always be returned in the query result. Leaving this 
                        parameter empty returns all attributes; otherwise only 
                        those properties listed will be visible in the result 
                        set (in addition to the sourceId); e.g.: 
                        validFrom,numberOfSeasons will show only sourceId, 
                        validFrom, and numberOfSeasons in the response.
        """

        input_vars = inspect.getargvalues(inspect.currentframe()).locals
        del input_vars['self']
        query_parameters = self.query_parameters(input_vars)
        url = self.base_url + f'frequencies/rainfall/availableSources/v{self.api_version}.jsonld?'

        response = self.get_response(url + query_parameters)
        return response.status_code, response.json() 

    def get_response(self,
                     url: str) -> 'GET response':
        """
        Description:
            Calls the API and checks if the response was successfull
        Args:
            url:    The url which is to be used in the GET request
        """
        with requests.get(url, headers=self.headers, auth=self.auth) as response:
            if not response.status_code == 200:
                print(f'Response code {response.status_code}, from url {url}')
                print(f'Error: {response.json()["error"]}')
                raise AssertionError()
            else:
                print(f'Response code: {response.status_code}, GET {url}')
                return response

    def query_parameters(self, input_vars) -> str:
        """
        Description:
            Creates the query parameters to add into the request url
        Args:
            input_vars: array of parameters to add to the url, come from the 
                        input to the get_* functions
        """
        query_parameters = ''
        for key, value in input_vars.items():
            if not value == None:
                key = key.replace('_','')
                if not query_parameters:
                    query_parameters+= f'{key}={value}'
                else:
                    query_parameters+= f'&{key}={value}'
        return query_parameters

    def convert_datetime(self,
                         *,
                         repeat: int = 0,
                         seperation: str = None,
                         start_time: 'datetime.datetime' = None,
                         end_time: 'datetime.datetime' = None) -> str:
        """
        Description:
            Converts datetime object to time string needed for referenceTime in
            API. If no start or end time is given the latest observed data will
            be retrieved. If no end time is given observations from start up 
            until now will be retrieved. 
        Args:
            repeat:     how many times to repeat interval
            seperation: between observation, ex. 1D is 1 day duration between
                        each interval
            start_time: starting time of observational data wanted
            end_time:   end time of observational data wanted
        """
        time_string = ''
        if repeat:
            time_string += f'R{repeat}/'

        if not start_time:
            time_string += 'latest'
        elif not end_time:
            time_string += start_time.strftime('%Y-%m-%dT%H:%M:%S.000Z') + '/' +\
                           datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.000Z')
        else:
            time_string += start_time.strftime('%Y-%m-%dT%H:%M:%S.000Z') + '/' +\
                           end_time.strftime('%Y-%m-%dT%H:%M:%S.000Z')

        if seperation:
            time_string += '/P{seperation}'

        return time_string

    def test_gets(self) -> None: 
        """
        Function to test all GET requests in API
        """
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
        status_code, response_json = self.get_climate_normals(sources = 'SN18700')
        status_code, response_json = self.get_climate_normals_available()
        status_code, response_json = self.get_frequencies_rainfall()
        status_code, response_json = self.get_frequencies_rainfall_available_sources()


class Stations(API):
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


if __name__=='__main__':
    api = False
    if api:
        test = API()
        test.test_gets()
        #test.test_gets()
        #test.nearest_stations(latitude=59.9138688,longitude=10.752245399999993)
        #stations = ','.join(test.station_ids)
        #status_code, response_json = test.get_observations_available_time_series(sources=stations)

        #for point in response_json['data']:
        #    test.stations[point['sourceId'][:7]].append(point)

        #for key, value in test.station_ids.items():
        #    for v in value:
        #        print(v)
    
    else:
        test = Stations(latitude=59.9138688,longitude=10.752245399999993,length_of_square=20.0)
        test.oslo_test()
        #closest = ''
        #for station, data in test.stations.items():
        #    available_data_types = [avail['elementId'] for avail in data['available']]
        #    if closest:
        #        close = test.stations[closest]
        #        if data['distance'] < close['distance']:
        #            if any('precipitation_amount' == data_type for data_type in available_data_types):
        #                closest = station
        #    elif any('precipitation_amount' == data_type for data_type in available_data_types):
        #        closest = station
        #    print(closest)
