import sys, traceback
import cerver
from cerver import http

LOAD_ERROR_NONE = 0
LOAD_ERROR_BAD_REQUEST = 1
LOAD_ERROR_MISSING_VALUES = 2
LOAD_ERROR_BAD_USER = 3
LOAD_ERROR_EXISTING_USER = 4
LOAD_ERROR_SERVER_ERROR = 5
LOAD_ERROR_NOT_FOUND_ERROR = 6

bad_request_error = None
bad_user_error = None
missing_values = None
existing_user_error = None
server_error = None
not_found_error = None

def load_errors_init ():
	global bad_request_error
	global bad_user_error
	global missing_values
	global existing_user_error
	global server_error
	global not_found_error

	bad_request_error = http.http_response_json_key_value (
	http.HTTP_STATUS_BAD_REQUEST,
		"error".encode ("utf-8"),
		"Bad request!".encode ("utf-8")
	)

	bad_user_error = http.http_response_json_key_value (
	http.HTTP_STATUS_BAD_REQUEST,
		"error".encode ("utf-8"),
		"Bad user!".encode ("utf-8")
	)

	missing_values = http.http_response_json_key_value (
	http.HTTP_STATUS_BAD_REQUEST,
		"error".encode ("utf-8"),
		"Missing values!".encode ("utf-8")
	)

	existing_user_error = http.http_response_json_key_value (
	http.HTTP_STATUS_BAD_REQUEST,
		"error".encode ("utf-8"),
		"User already exists!".encode ("utf-8")
	)

	server_error = http.http_response_json_key_value (
	http.HTTP_STATUS_INTERNAL_SERVER_ERROR,
		"error".encode ("utf-8"),
		"Server error!".encode ("utf-8")
	)
	not_found_error = http.http_response_json_key_value (
	http.HTTP_STATUS_INTERNAL_SERVER_ERROR,
		"error".encode ("utf-8"),
		"Element not found!".encode ("utf-8")
	)

def load_error_send_response (load_error, http_receive):
	if (load_error == LOAD_ERROR_NONE):
		pass

	if (load_error == LOAD_ERROR_BAD_REQUEST):
		http.http_response_send (bad_request_error, http_receive)

	if (load_error == LOAD_ERROR_MISSING_VALUES):
		http.http_response_send (missing_values, http_receive)

	if (load_error == LOAD_ERROR_BAD_USER):
		http.http_response_send (bad_user_error, http_receive)

	if (load_error == LOAD_ERROR_EXISTING_USER):
		http.http_response_send (existing_user_error, http_receive)

	if (load_error == LOAD_ERROR_SERVER_ERROR):
		http.http_response_send (server_error, http_receive)

	if (load_error == LOAD_ERROR_NOT_FOUND_ERROR):
		http.http_response_send (server_error, http_receive)

def load_print_exception():
	a, b, bt = sys.exc_info()

	print(f"{sys.exc_info()}, Line: {bt.tb_lineno}")
	traceback.print_exc()


def load_errors_end ():
	global bad_request_error
	global bad_user_error
	global missing_values
	global existing_user_error
	global server_error
	global not_found_error

	cerver.http_response_delete (bad_request_error)
	cerver.http_response_delete (bad_user_error)
	cerver.http_response_delete (missing_values)
	cerver.http_response_delete (existing_user_error)
	cerver.http_response_delete (server_error)
	cerver.http_response_delete (not_found_error)