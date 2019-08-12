import connexion
import six
import os

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.message import Message  # noqa: E501
from swagger_server import util
from rivescript import RiveScript

def message(message=None):  # noqa: E501
    """requesting chatbot to handle task

    ask bot # noqa: E501

    :param message: 
    :type message: dict | bytes

    :rtype: InlineResponse200
    """     
    if connexion.request.is_json:
        message = Message.from_dict(connexion.request.get_json())  # noqa: E501

    msg = message._message
    bot = RiveScript()
    path = os.path.dirname(os.path.realpath(__file__))+'/brain'
    bot.load_directory(path)
    bot.sort_replies()

    reply = bot.reply("localuser", msg)
    
    if reply == '[ERR: No Reply Matched]':
        reply = "The bot can not understand you question:("   
    return reply , 200, None
