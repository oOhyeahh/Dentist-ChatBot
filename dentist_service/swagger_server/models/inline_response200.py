# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse200(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: float=None, name: str=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger

        :param id: The id of this InlineResponse200.  # noqa: E501
        :type id: float
        :param name: The name of this InlineResponse200.  # noqa: E501
        :type name: str
        """
        self.swagger_types = {
            'id': float,
            'name': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name'
        }

        self._id = id
        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse200':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200 of this InlineResponse200.  # noqa: E501
        :rtype: InlineResponse200
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> float:
        """Gets the id of this InlineResponse200.

        dentist id  # noqa: E501

        :return: The id of this InlineResponse200.
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id: float):
        """Sets the id of this InlineResponse200.

        dentist id  # noqa: E501

        :param id: The id of this InlineResponse200.
        :type id: float
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this InlineResponse200.

        dentist name  # noqa: E501

        :return: The name of this InlineResponse200.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this InlineResponse200.

        dentist name  # noqa: E501

        :param name: The name of this InlineResponse200.
        :type name: str
        """

        self._name = name