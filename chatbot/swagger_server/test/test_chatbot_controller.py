# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.message import Message  # noqa: E501
from swagger_server.test import BaseTestCase


class TestChatbotController(BaseTestCase):
    """ChatbotController integration test stubs"""

    def test_message(self):
        """Test case for message

        requesting chatbot to handle task
        """
        message = Message()
        response = self.client.open(
            '/v1/bot',
            method='POST',
            data=json.dumps(message),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
