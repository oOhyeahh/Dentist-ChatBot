# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.timeslot_timeslot import TimeslotTimeslot  # noqa: F401,E501
from swagger_server import util


class InlineResponse200(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, dentist_id: float=None, timeslot: List[TimeslotTimeslot]=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger

        :param dentist_id: The dentist_id of this InlineResponse200.  # noqa: E501
        :type dentist_id: float
        :param timeslot: The timeslot of this InlineResponse200.  # noqa: E501
        :type timeslot: List[TimeslotTimeslot]
        """
        self.swagger_types = {
            'dentist_id': float,
            'timeslot': List[TimeslotTimeslot]
        }

        self.attribute_map = {
            'dentist_id': 'dentistId',
            'timeslot': 'timeslot'
        }

        self._dentist_id = dentist_id
        self._timeslot = timeslot

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
    def dentist_id(self) -> float:
        """Gets the dentist_id of this InlineResponse200.

        dentist id  # noqa: E501

        :return: The dentist_id of this InlineResponse200.
        :rtype: float
        """
        return self._dentist_id

    @dentist_id.setter
    def dentist_id(self, dentist_id: float):
        """Sets the dentist_id of this InlineResponse200.

        dentist id  # noqa: E501

        :param dentist_id: The dentist_id of this InlineResponse200.
        :type dentist_id: float
        """

        self._dentist_id = dentist_id

    @property
    def timeslot(self) -> List[TimeslotTimeslot]:
        """Gets the timeslot of this InlineResponse200.


        :return: The timeslot of this InlineResponse200.
        :rtype: List[TimeslotTimeslot]
        """
        return self._timeslot

    @timeslot.setter
    def timeslot(self, timeslot: List[TimeslotTimeslot]):
        """Sets the timeslot of this InlineResponse200.


        :param timeslot: The timeslot of this InlineResponse200.
        :type timeslot: List[TimeslotTimeslot]
        """

        self._timeslot = timeslot
