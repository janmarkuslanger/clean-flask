from functools import wraps
from flask import session, abort


def login_required(f):
    @wraps(f)
    def check_login(*args, **kwargs):
        if 'username' not in session:
            abort(403)
        return f(*args, **kwargs)
    return check_login
