def dict_from_truple(input_list):
    """Turn three-item tuples into a dicitonary of two-valued tuples."""
    truple_dict = {}
    for key, value1, value2 in input_list:
        truple_dict[key] = (value1, value2)
    return truple_dict
