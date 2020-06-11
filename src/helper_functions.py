# function to return key for any value, if it's found
# in the dict
def get_key(val, the_dict):
    for key, value in the_dict.items():
        if val == value:
            return key

    return "key doesn't exist"
