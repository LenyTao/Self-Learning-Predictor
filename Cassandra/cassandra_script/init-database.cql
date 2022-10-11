CREATE KEYSPACE IF NOT EXISTS covid_predictor_app WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : '1' };		
				 
CREATE TABLE IF NOT EXISTS covid_predictor_app.predictions (
id_event text,
sex double,
patient_type double,
intubed double,
pneumonia double,
age double,
pregnancy double,
diabetes double,
copd double,
asthma double,
inmsupr double,
hypertension double,
other_disease double,
cardiovascular double,
obesity double,
renal_chronic double,
tobacco double,
contact_other_covid double,
covid_res double,
icu double,
entry_date text,
date_symptoms text,
name text,
classifier_prediction double,
regression_prediction double,
PRIMARY KEY (id_event, entry_date)
)
WITH CLUSTERING ORDER BY (entry_date DESC);