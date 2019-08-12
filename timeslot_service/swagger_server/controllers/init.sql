CREATE TABLE TIMESLOT (
    BookingId integer primary key,
    DentistId integer, 
    PatientName varchar(256),
    PhoneNumber varchar(256),
    BookingDate Date,
    StartTime varchar(256),
	EndTime varchar(256)
);

INSERT INTO TIMESLOT(DentistId, PatientName, PhoneNumber, BookingDate, StartTime, EndTime) VALUES (1, 'test' , '0435333333', '2001-07-28', '9:30:00', '10:30:00');