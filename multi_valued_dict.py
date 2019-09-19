def multi_valued_dict(tuple_list):
    """Turn multi-item tuples into a dictionary of two-valued tuples."""
    new_dict = {}
    for items in tuple_list:
        new_dict[items[0]] = items[1:]
    return new_dict
