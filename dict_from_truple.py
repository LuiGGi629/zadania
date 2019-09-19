def dict_from_truple(input_list):
    """Turn three-item tuples into a dicitonary of two-valued tuples."""
    new_dict = {}
    for items in input_list:
        new_dict[items[0]] = items[1:]
    return new_dict
