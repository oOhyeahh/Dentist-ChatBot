# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.booking_details import BookingDetails  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.inline_response400 import InlineResponse400  # noqa: E501
from swagger_server.models.inline_response404 import InlineResponse404  # noqa: E501
from swagger_server.models.inline_response4041 import InlineResponse4041  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTimeslotController(BaseTestCase):
    """TimeslotController integration test stubs"""

    def test_delete_booking(self):
        """Test case for delete_booking

        delete the reserve booking
        """
        response = self.client.open(
            '/v1/timeslot/{id}'.format(id='id_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_dentists_timeslot(self):
        """Test case for get_all_dentists_timeslot

        get all dentists timeslot
        """
        query_string = [('status', 'free')]
        response = self.client.open(
            '/v1/timeslot',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_reserve_booking(self):
        """Test case for reserve_booking

        make reservation
        """
        booking_details = BookingDetails()
        response = self.client.open(
            '/v1/timeslot',
            method='POST',
            data=json.dumps(booking_details),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
