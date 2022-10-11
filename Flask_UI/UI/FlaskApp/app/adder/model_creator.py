import uuid

from app.model.event_models import Event, Ml_Event


def create_model_for_prediction(request_dict: dict) -> Event:
    event_for_prediction: Event = Event(
        str(uuid.uuid4()),
        int(request_dict["sex"]),
        int(request_dict["patient_type"]),
        int(request_dict["intubed"]),
        int(request_dict["pneumonia"]),
        int(request_dict["age"]),
        int(request_dict["pregnancy"]),
        int(request_dict["diabetes"]),
        int(request_dict["copd"]),
        int(request_dict["asthma"]),
        int(request_dict["inmsupr"]),
        int(request_dict["hypertension"]),
        int(request_dict["other_disease"]),
        int(request_dict["cardiovascular"]),
        int(request_dict["obesity"]),
        int(request_dict["renal_chronic"]),
        int(request_dict["tobacco"]),
        int(request_dict["contact_other_covid"]),
        int(request_dict["covid_res"]),
        int(request_dict["icu"]),
        str(request_dict["entry_date"]),
        str(request_dict["date_symptoms"]),
        str(request_dict["name"]))
    return event_for_prediction


def create_model_for_learning(request_dict: dict) -> Ml_Event:
    event_for_learning: Ml_Event = Ml_Event(
        str(request_dict["id_event"]),
        float(request_dict["sex"]),
        float(request_dict["patient_type"]),
        str(request_dict["entry_date"]),
        str(request_dict["date_symptoms"]),
        float(request_dict["death"]),
        float(request_dict["intubed"]),
        float(request_dict["pneumonia"]),
        float(request_dict["age"]),
        float(request_dict["pregnancy"]),
        float(request_dict["diabetes"]),
        float(request_dict["copd"]),
        float(request_dict["asthma"]),
        float(request_dict["inmsupr"]),
        float(request_dict["hypertension"]),
        float(request_dict["other_disease"]),
        float(request_dict["cardiovascular"]),
        float(request_dict["obesity"]),
        float(request_dict["renal_chronic"]),
        float(request_dict["tobacco"]),
        float(request_dict["contact_other_covid"]),
        float(request_dict["covid_res"]),
        float(request_dict["icu"]))
    return event_for_learning
