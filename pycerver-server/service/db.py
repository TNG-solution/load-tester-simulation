import os
from pymongo import MongoClient

import cerver.utils 
import service.loads as load

from pymongoose.methods import set_schemas

## Models
from service.models.user import User, user_model_init
from service.models.role import Role, role_model_init

load_db = None

def load_mongo_init():
	global load_db
	client = MongoClient(load.MONGO_URI)
	try:
		load_db = client.test

		cerver.utils.cerver_log_success(
			"MongoDB Connected!".encode("utf-8")
		)
		# Include models
		user_model_init(load_db)
		role_model_init(load_db)

		schemas = {
			"users": User(empty=True).schema,
			"roles": Role(empty=True).schema,
		}

		set_schemas(schemas)
	except:
		cerver.utils.cerver_log_error(
			"Error connecting to MongoDB".encode("utf-8")
		)