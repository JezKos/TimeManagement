/*CREATE DATABASE timemanagement;*/

/*CREATE TABLE time_entries (id SERIAL PRIMARY KEY, consultantName VARCHAR(255) NOT NULL, customerName VARCHAR(255) NOT NULL, startTime TIMESTAMP NOT NULL, endTime TIMESTAMP NOT NULL, lunchStart TIMESTAMP, lunchEnd TIMESTAMP);*/

/*INSERT INTO time_entries (consultantName, customerName, startTime, endTime, lunchStart, lunchEnd) VALUES ('John Doe', 'Ernst & Young Oy', '2025-11-04 08:00:00', '2025-11-04 16:00:00', '2025-11-04 12:00:00', '2025-11-04 12:30:00'), ('Harley Queen', 'Pwc Oy', '2025-11-04 10:00:00', '2025-11-04 15:00:00', '2025-11-04 11:30:00', '2025-11-04 12:30:00');*/

SELECT consultantName, customerName,  ROUND((EXTRACT(EPOCH FROM (endtime - starttime)) / 3600),2) AS shift_time, ROUND((EXTRACT(EPOCH FROM (lunchend - lunchstart)) / 3600),2) AS lunch_time, (ROUND((EXTRACT(EPOCH FROM (endtime - starttime)) / 3600),2) - ROUND((EXTRACT(EPOCH FROM (lunchend - lunchstart)) / 3600),2)) AS  working_hours FROM time_entries WHERE DATE(starttime) BETWEEN  '2025-11-02' AND '2025-11-06';