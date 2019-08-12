# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response404 import InlineResponse404  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDentistController(BaseTestCase):
    """DentistController integration test stubs"""

    def test_get_available_dentist(self):
        """Test case for get_available_dentist

        Return a list of available_dentist
        """
        response = self.client.open(
            '/v1/dentists',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_dentist_information(self):
        """Test case for get_dentist_information

        Return detail information of the dentist
        """
        response = self.client.open(
            '/v1/dentists/{id}/information'.format(id='id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
