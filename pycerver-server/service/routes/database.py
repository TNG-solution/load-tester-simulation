import ctypes
import json
import random
import re
from cerver import *
from cerver.http import *
from cerver.headers import *

from service.errors import *
from service import runtime, loads
from service.models.user import *
from service.models.role import *
from service.utils.body_validator import *

#GET /api/database
@ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)
def top_level_handler (http_receive, request):
    try:
        http_send_response(http_receive, HTTP_STATUS_OK, {"oki":"doki"})
    except:
        load_error_send_response(LOAD_ERROR_SERVER_ERROR, http_receive)


#POST /api/database/register
@ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)
def register_handler (http_receive, request):
    body = None
    try:
        body = http_request_get_body_json(request)
        print(body)
        validate_body_required_keys(["name", "username"], body)
    except:
        load_error_send_response(LOAD_ERROR_MISSING_VALUES, http_receive)
    try:
        role = Role.find({"name": "common"}, one=True)
        user = User(
            name=body["name"],
            username=body["username"],
            role=role.id
        )
        user.save()

        http_send_response(http_receive,HTTP_STATUS_OK, {"oki":"doki"})

    except:
        load_print_exception()
        load_error_send_response(LOAD_ERROR_SERVER_ERROR, http_receive)


#GET /api/database/profile
@ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)
def profile_handler (http_receive, request):
    name = None
    try:
        param_values = http_request_get_query_params(request)
        name = http_request_get_query_value(param_values, "name")
    except:
        load_error_send_response(LOAD_ERROR_MISSING_VALUES, http_receive)
    try:
        user = User.find({"name": name}, one=True)

        if user is None:
            http_send_response(http_receive, HTTP_STATUS_NOT_FOUND, {"error": "User not found"})
        else:
            http_send_response(http_receive,HTTP_STATUS_OK, {"oki":"doki"})

    except:
        load_print_exception()
        load_error_send_response(LOAD_ERROR_SERVER_ERROR, http_receive)

#DELETE /api/database/delete
@ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)
def delete_handler (http_receive, request):
    try:
        param_values = http_request_get_query_params(request)
        name = http_request_get_query_value(param_values, "name")
    except:
        load_error_send_response(LOAD_ERROR_MISSING_VALUES, http_receive)
    try:
        print(name)
        count = User.delete({"name": name})

        if count == 0:
            return http_send_response(http_receive, HTTP_STATUS_NOT_MODIFIED, {"msg": "No user was deleted"})
        
        http_send_response(http_receive,HTTP_STATUS_OK, {"oki":"doki"})

    except:
        load_error_send_response(LOAD_ERROR_SERVER_ERROR, http_receive)
