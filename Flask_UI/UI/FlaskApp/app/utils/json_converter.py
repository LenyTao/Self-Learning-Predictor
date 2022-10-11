import jsonpickle


def convert_to_json(obj) -> str:
    return jsonpickle.encode(obj, unpicklable=False)
