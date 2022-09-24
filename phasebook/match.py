import time
from flask import Blueprint

from .data.match_data import MATCHES


bp = Blueprint("match", __name__, url_prefix="/match")


@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404

    start = time.time()
    # msg = "Match found" if (is_match(*MATCHES[match_id])) else "No match"
    msg = "Match found" if (match_test(*MATCHES[match_id])) else "No match"
    end = time.time()

    return {"message": msg, "elapsedTime": end - start}, 200


def is_match(fave_numbers_1, fave_numbers_2):
    for number in fave_numbers_2:
        if number not in fave_numbers_1:
            return False

    return True

# my function
def match_test(list1, list2):
    # list 1: array to search from
    # list 2: array to search with
    list_to_hash =  {x: 'x' for x in list2} 
    found = {}

    for n in list1: 
        if n in list_to_hash:
        # if list_to_hash.get(n):
            found[n] = 'x'

    return list_to_hash == found
