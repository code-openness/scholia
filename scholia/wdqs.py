"""Wikidata Query Service."""

import requests


class WDQS():
    """
    Wikidata Query Service.

    the main purpose of this class is allowing the possiblility of using
    another end-point of the wikidata query service, for example, if you are
    running a local instance of the query service, you can set the link to
    localhost.
    """

    queryServiceURL = 'https://query.wikidata.org'

    @staticmethod
    def initFlaskApp(app):
        """
        Initilizes a Flask apps with the queryServiceURL.

        All {{ queryServiceURL }} variables that appear in the html
        templates will be replaced with the link to the query

        Parameters
        ----------
        app : flask.app.Flask
            Flask app object.

        """
        @app.context_processor
        def inject_url():
            return dict(queryServiceURL=WDQS.queryServiceURL)

    @staticmethod
    def setURL(url='https://query.wikidata.org'):
        """
        Set the url to the Wikidata Query Service.

        Parameters
        ----------
        url : string
             query service url

        """
        WDQS.queryServiceURL = url

    @staticmethod
    def sparql_get(query, dataFormat='json', **requestProps):
        """
        Do a GET request to the 'WikidataQueryService/sparql' address.

        Parameters
        ----------
        query : string
             SPARQL query to send

        dataFormat: string
             the data format to be requested from the server

        **requestProps: dict
            any additional request parameters, will be given to requests.get

        Returns
        -------
        response: requests.Response

        """
        url = WDQS.queryServiceURL + '/sparql'
        params = {'query': query, 'format': dataFormat}
        response = requests.get(url, params=params, **requestProps)
        return response

    @staticmethod
    def bigdata_sparql_get(query, dataFormat='json', **requestProps):
        """
        Do GET request to 'WikidataQueryService/bigdata/namespace/wdq/sparql'.

        Parameters
        ----------
        query : string
             SPARQL query to send

        dataFormat: string
             the data format to be requested from the server

        **requestProps: dict
            any additional request parameters, will be given to requests.get

        Returns
        -------
        response: requests.Response

        """
        url = WDQS.queryServiceURL + '/bigdata/namespace/wdq/sparql'
        params = {'query': query, 'format': dataFormat}
        response = requests.get(url, params=params, **requestProps)
        return response
