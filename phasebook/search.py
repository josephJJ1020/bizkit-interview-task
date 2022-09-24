from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!

    res = []

    if not args:
        return USERS

    for user in USERS:
        if "id" in args and args["id"] == user["id"]:
            res.append(user)
            continue
        if "name" in args and args["name"] in user["name"]:
            res.append(user)
            continue
        if "age" in args and abs(int(args["age"]) - int(user["age"])) < 2:
            res.append(user)
            continue
        if "occupation" in args and args["occupation"] in user["occupation"]:
            res.append(user)
            continue
        
    return res
