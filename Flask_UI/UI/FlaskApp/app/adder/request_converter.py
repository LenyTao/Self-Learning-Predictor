from app.adder import model_creator

from flask import Request


def convert_request_to_model(request: Request):
    request_dict = request.form
    if request_dict.__contains__("death"):
        return model_creator.create_model_for_learning(request_dict)
    else:
        return model_creator.create_model_for_prediction(request_dict)
