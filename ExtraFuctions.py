def process_le_to_number(s_num, to_type, default_num):
    try:
        return to_type(s_num)
    except:
        return default_num