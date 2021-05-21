import os, signal, sys
import ctypes
from service.loads import *

from cerver import *
from cerver.http import *
from cerver.headers import *

from service.routes import loads, database

api_cerver = None

def end (signum, frame):
	http_cerver_all_stats_print (http_cerver_get (api_cerver))
	cerver_teardown (api_cerver)
	cerver_end ()
	sys.exit ("Done!")

def loads_set_routes (http_cerver):
	#route_configuration
	#GET /api/py
	main_route = http_create_route(REQUEST_METHOD_GET, "api/py", loads.top_handler, http_cerver=http_cerver)

	#POST /api/py/sum
	http_create_route(REQUEST_METHOD_POST, "sum", loads.sum_handler, main_route)

	#POST /api/py/substract
	http_create_route(REQUEST_METHOD_POST, "substract", loads.substract_handler, main_route)

	#POST /api/py/multiply
	http_create_route(REQUEST_METHOD_POST, "multiply", loads.multiply_handler, main_route)

	#POST /api/py/divide
	http_create_route(REQUEST_METHOD_POST, "divide", loads.divide_handler, main_route)

	#Database

	#GET /api/py/database
	http_create_route(REQUEST_METHOD_GET, "database", database.top_level_handler, main_route)

	#POST /api/py/database/register
	http_create_route(REQUEST_METHOD_POST, "database/register", database.register_handler, main_route)

	#GET /api/py/database/profile
	http_create_route(REQUEST_METHOD_GET, "database/profile", database.profile_handler, main_route)

	#DELETE /api/py/database/delete
	http_create_route(REQUEST_METHOD_DELETE, "database/delete", database.delete_handler, main_route)

def start ():
	global api_cerver
	api_cerver = cerver_main_http_configuration (PORT, CERVER_CONNECTION_QUEUE)

	http_cerver = http_cerver_get (api_cerver)
	
	loads_set_routes (http_cerver)

	cerver_start(api_cerver)