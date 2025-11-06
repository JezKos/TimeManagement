/*CREATE DATABASE timemanagement;

CREATE TABLE time_entries (id SERIAL PRIMARY KEY, consultantName VARCHAR(255) NOT NULL, customerName VARCHAR(255) NOT NULL, startTime TIMESTAMP NOT NULL, endTime TIMESTAMP NOT NULL, lunchStart TIMESTAMP, lunchEnd TIMESTAMP);*/

/*INSERT INTO time_entries (consultantName, customerName, startTime, endTime, lunchStart, lunchEnd) VALUES ('Peter Parker', 'Daily Mail', '2025-11-06 08:00:00', '2025-11-06 16:00:00', '2025-11-06 12:00:00', '2025-11-06 12:30:00'), ('Down Jones', 'Microsoft', '2025-11-06 10:00:00', '2025-11-06 15:00:00', '2025-11-06 11:30:00', '2025-11-06 12:30:00');*/

/*SELECT consultantName, customerName,  ROUND((EXTRACT(EPOCH FROM (endtime - starttime)) / 3600),2) AS shift_time, ROUND((EXTRACT(EPOCH FROM (lunchend - lunchstart)) / 3600),2) AS lunch_time, (ROUND((EXTRACT(EPOCH FROM (endtime - starttime)) / 3600),2) - ROUND((EXTRACT(EPOCH FROM (lunchend - lunchstart)) / 3600),2)) AS  working_hours FROM time_entries WHERE DATE(starttime) BETWEEN  '2025-11-05' AND '2025-11-05';*/

/*SELECT customerName, COUNT(consultantName) AS number_of_consultants, SUM(ROUND((EXTRACT(EPOCH FROM (endtime - starttime)) / 3600),2) - ROUND((EXTRACT(EPOCH FROM (lunchend - lunchstart)) / 3600),2)) AS working_hours FROM time_entries WHERE DATE(starttime) BETWEEN  '2025-11-03' AND '2025-11-07' GROUP BY customerName;*/

/*SELECT * FROM time_entries WHERE DATE(starttime) BETWEEN  '2025-11-03' AND '2025-11-07';*/

