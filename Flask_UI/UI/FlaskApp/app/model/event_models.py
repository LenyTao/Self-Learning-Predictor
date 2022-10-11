class Event:
    def __init__(self,
                 id_event: str,
                 sex: int,
                 patient_type: int,
                 intubed: int,
                 pneumonia: int,
                 age: int,
                 pregnancy: int,
                 diabetes: int,
                 copd: int,
                 asthma: int,
                 inmsupr: int,
                 hypertension: int,
                 other_disease: int,
                 cardiovascular: int,
                 obesity: int,
                 renal_chronic: int,
                 tobacco: int,
                 contact_other_covid: int,
                 covid_res: int,
                 icu: int,
                 entry_date: str,
                 date_symptoms: str,
                 name: str):
        self.id_event = id_event
        self.sex = sex
        self.patient_type = patient_type
        self.intubed = intubed
        self.pneumonia = pneumonia
        self.age = age
        self.pregnancy = pregnancy
        self.diabetes = diabetes
        self.copd = copd
        self.asthma = asthma
        self.inmsupr = inmsupr
        self.hypertension = hypertension
        self.other_disease = other_disease
        self.cardiovascular = cardiovascular
        self.obesity = obesity
        self.renal_chronic = renal_chronic
        self.tobacco = tobacco
        self.contact_other_covid = contact_other_covid
        self.covid_res = covid_res
        self.icu = icu
        self.entry_date = entry_date
        self.date_symptoms = date_symptoms
        self.name = name


class Ml_Event:
    def __init__(self,
                 id_event: str,
                 sex: float,
                 patient_type: float,
                 entry_date: str,
                 date_symptoms: str,
                 death: float,
                 intubed: float,
                 pneumonia: float,
                 age: float,
                 pregnancy: float,
                 diabetes: float,
                 copd: float,
                 asthma: float,
                 inmsupr: float,
                 hypertension: float,
                 other_disease: float,
                 cardiovascular: float,
                 obesity: float,
                 renal_chronic: float,
                 tobacco: float,
                 contact_other_covid: float,
                 covid_res: float,
                 icu: float):
        self.id_event = id_event
        self.sex = sex
        self.patient_type = patient_type
        self.entry_date = entry_date
        self.date_symptoms = date_symptoms
        self.death = death
        self.intubed = intubed
        self.pneumonia = pneumonia
        self.age = age
        self.pregnancy = pregnancy
        self.diabetes = diabetes
        self.copd = copd
        self.asthma = asthma
        self.inmsupr = inmsupr
        self.hypertension = hypertension
        self.other_disease = other_disease
        self.cardiovascular = cardiovascular
        self.obesity = obesity
        self.renal_chronic = renal_chronic
        self.tobacco = tobacco
        self.contact_other_covid = contact_other_covid
        self.covid_res = covid_res
        self.icu = icu
