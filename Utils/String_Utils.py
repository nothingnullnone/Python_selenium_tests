import random
import string

from Config.Filenames import Filenames
from Utils import JSON_Utils


def get_random_string():
    text_min_len = JSON_Utils.get_json_field(Filenames.test_file_alerts.value, "text_min_length")
    text_max_len = JSON_Utils.get_json_field(Filenames.test_file_alerts.value, "text_max_length")
    text_len = random.choice(range(text_min_len, text_max_len))
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(text_len))

