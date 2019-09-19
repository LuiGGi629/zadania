def dict_from_truple(input_list):
    """Turn three-item tuples into a dicitonary of two-valued tuples."""
    new_dict = {}
    for tup in input_list:
        new_dict[tup[0]] = (tup[1], tup[2])
    return new_dict
