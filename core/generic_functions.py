def qs_to_array_dict(qs):
    arr = []
    for index, item in enumerate(qs):
        dict = model_to_dict(item)
        arr.append(dict)
    return arr
def model_to_dict(model):
    dict = {}
    for field in model._meta.fields:
        dict[field.name] = getattr(model, field.name, False)
    return dict