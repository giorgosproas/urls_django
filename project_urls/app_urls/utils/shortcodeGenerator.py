import random
import string

def get_shortcode(length):
    choice = string.ascii_lowercase + string.digits + "_"
    result_str=""
    for i in range(length):
        randomChoice=random.choice(choice)
        result_str+=randomChoice
    return result_str