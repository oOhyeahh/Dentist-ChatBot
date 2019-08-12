import connexion
import six

from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response404 import InlineResponse404  # noqa: E501
from swagger_server import util
from .db import get_all_available_dentists_fromdb, get_dentist_info_fromdb, serach_dentist_by_name


def get_available_dentist():  # noqa: E501
    """Return a list of available_dentist

     # noqa: E501


    :rtype: List[object]
    """
    result = get_all_available_dentists_fromdb()
    print(result)
    if len(result) is 0:
        return InlineResponse404, 404
    return result, 200


def get_dentist_information(id):  # noqa: E501
    """Return detail information of the dentist

     # noqa: E501

    :param id: dentist id
    :type id: str

    :rtype: InlineResponse2001
    """
    result = get_dentist_info_fromdb(id)
    if len(result) is 0:
        return InlineResponse404(), 404
    
    return result[0], 200

def get_dentist_by_name(name):
    result = serach_dentist_by_name(name)
    if len(result) is 0:
        return InlineResponse404('dentist is not found'), 404
    
    return result, 200
