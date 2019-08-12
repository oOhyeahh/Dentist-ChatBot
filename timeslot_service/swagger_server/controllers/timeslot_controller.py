import connexion
import six
import datetime
from datetime import date, time

from swagger_server.models.booking_details import BookingDetails  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.inline_response400 import InlineResponse400  # noqa: E501
from swagger_server.models.inline_response404 import InlineResponse404  # noqa: E501
from swagger_server.models.inline_response4041 import InlineResponse4041  # noqa: E501
from swagger_server import util
from .db import *
from .utils import *



def delete_booking(id):  # noqa: E501
    """delete the reserve booking

    delete the reserve booking # noqa: E501

    :param id: booking id
    :type id: str

    :rtype: InlineResponse2002
    """
    if find_booking_by_id(id) > 0:
        result = cancel_booking(id)
        if result:
            return InlineResponse2002("delete success"), 200
    return InlineResponse404("booking id {} is not found".format(id)), 404


def get_dentist_timeslot(id):  # noqa: E501
    """get all dentists timeslot

    get all dentists timeslot # noqa: E501

    :rtype: List[object]
    """
    current_date = date.today()
    appointments = serach_booking_by_dentist(id)
    target_date_appointments = []
    for i in range(len(appointments)):
        start, end = appointments[i]
        if datetime.date(start) == current_date:
            target_date_appointments.append(appointments[i])
            

    return get_slots(get_working_hours(current_date),target_date_appointments)

def reserve_booking(booking_details=None):  # noqa: E501
    """make reservation

    make reservation with the dentist # noqa: E501

    :param booking_details: 
    :type booking_details: dict | bytes

    :rtype: InlineResponse2001
    """
    if connexion.request.is_json:
        booking_details = BookingDetails.from_dict(connexion.request.get_json())  # noqa: E501
        start_time = get_format_time(booking_details._start_time)
        end_time = get_format_time(booking_details._end_time)
        if start_time > end_time:
            return InlineResponse400("The starting time is earlyer than ending time"), 400

        if start_time < get_format_time('9:00') or end_time > get_format_time('17:00'):
            return InlineResponse400("The office hour is between 9am-5pm. The booking time is out of range"), 400

        dentist_id = booking_details._id
        patient_name = booking_details._patient_name
        phonenumber = booking_details._phonenumber
        booking_date = booking_details._booking_date
        appointment_list = serach_booking_by_dentist(dentist_id)
        current_day_appointments = []
        for i in range(len(appointment_list)):
            booking_start_time, booking_end_time = appointment_list[i]
            if (booking_start_time.date()==datetime.strptime(booking_date, '%Y-%m-%d').date()):
                current_day_appointments.append(appointment_list[i])

        timeslot_list = get_slots(get_working_hours(datetime.strptime(booking_date, '%Y-%m-%d').date()), current_day_appointments)
        if check_crashing_time(timeslot_list, start_time, end_time) is False:
            booking_ref = create_booking(dentist_id, patient_name, phonenumber, booking_date, start_time, end_time)
            return InlineResponse2001("create the booking success. The booking id {} is the reference".format(booking_ref)), 201            
        else:
            return InlineResponse400("The booking time is crashing"), 400