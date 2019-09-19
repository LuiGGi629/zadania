def dict_from_truple(input_list):
    """Turn three-item tuples into a dicitonary of two-valued tuples."""
    return {
        key: (value1, value2)
        for key, value1, value2 in input_list
    }
