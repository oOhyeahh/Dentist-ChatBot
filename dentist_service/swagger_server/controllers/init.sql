CREATE TABLE DENTIST (
    DentistId integer primary key,  
    FullName varchar(256),
    workplace varchar(256),
    specialist varchar(256)
);

-- CREATE TABLE TIMESLOT (
--     BookingId SERIAL primary key,
--     DentistId integer REFERENCES DENTIST(DentistId), 
--     PatientName varchar(256),
--     PhoneNumber varchar(256),
--     BookingDate Date,
--     StartTime varchar(256),
-- 	EndTime varchar(256)
-- );

INSERT INTO DENTIST(FullName, workplace, specialist) VALUES ('Sam Zhang', 'Kingsford Dentist Health Care', 'Paediatric Dentistry');
INSERT INTO DENTIST(FullName, workplace, specialist) VALUES ('John Lo', 'Kingsford Dentist Health Care', 'Orthodontics');
INSERT INTO DENTIST(FullName, workplace, specialist) VALUES ('Adam Smith', 'Randwick Dentist center', 'Oral Surgery');
INSERT INTO DENTIST(FullName, workplace, specialist) VALUES ('Tammy Queen', 'Randwick Dentist center', 'Paediatric Dentistry');
INSERT INTO DENTIST(FullName, workplace, specialist) VALUES ('John Stevenson', 'Coogee Dentist Health Care', 'Oral Surgery');
-- INSERT INTO TIMESLOT(DentistId, PatientName, PhoneNumber, BookingDate, StartTime, EndTime) VALUES (1, 'test' , '0435333333', '2001-07-28', '9:30:00', '10:30:00');