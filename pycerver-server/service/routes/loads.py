import ctypes
import json
import random
import re
from cerver import *
from cerver.http import *
from cerver.headers import *

from service.errors import *
from service import runtime, loads
from service.utils.body_validator import *
from service.utils.request import *

#GET        /api/py
#Desc       Top level
#Access     Public
@ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)
def top_handler (http_receive, request):
	try:
		http_send_response(http_receive,HTTP_STATUS_OK, {"msg": "Loads works!"})
	except:
		loads_error_send_response(REPORTS_ERROR_SERVER_ERROR, http_receive)

#GET /api/py/sum
@ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)
def sum_handler (http_receive, request):
	try:
		body = http_request_get_body_json(request)
		http_send_response(http_receive, HTTP_STATUS_OK, {"result": body["a"] + body["b"]})
	except:
		loads_error_send_response(LOADS_ERROR_SERVER_ERROR, http_receive)

#GET /api/py/substract
@ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)
def substract_handler (http_receive, request):
	try:
		body = http_request_get_body_json(request)
		http_send_response(http_receive, HTTP_STATUS_OK, {"result": body["a"] - body["b"]})
	except:
		loads_error_send_response(LOADS_ERROR_SERVER_ERROR, http_receive)

#GET /api/py/multiply
@ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)
def multiply_handler (http_receive, request):
	try:
		body = http_request_get_body_json(request)
		http_send_response(http_receive, HTTP_STATUS_OK, {"result": body["a"] * body["b"]})
	except:
		loads_error_send_response(LOADS_ERROR_SERVER_ERROR, http_receive)

#GET /api/py/divide
@ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)
def divide_handler (http_receive, request):
	try:
		body = http_request_get_body_json(request)
		http_send_response(http_receive, HTTP_STATUS_OK, {"result": body["a"] / body["b"]})
	except:
		loads_error_send_response(LOADS_ERROR_SERVER_ERROR, http_receive)