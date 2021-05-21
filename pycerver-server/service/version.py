import cerver.utils

LOAD_TEST_VERSION = "0.1"
LOAD_TEST_VERSION_NAME = "Version 0.1"
LOAD_TEST_VERSION_DATE = "20/05/2021"
LOAD_TEST_VERSION_TIME = "17:00 CST"
LOAD_TEST_VERSION_AUTHOR = "Juan Carlos Lara"

def loads_version_print_full ():
   cerver.utils.cerver_log_both (
   cerver.utils.LOG_TYPE_NONE, cerver.utils.LOG_TYPE_NONE,
   "LoadTest PyCerver Version: %s".encode ('utf-8'), LOAD_TEST_VERSION_NAME.encode ('utf-8')
   )

   cerver.utils.cerver_log_both (
   cerver.utils.LOG_TYPE_NONE, cerver.utils.LOG_TYPE_NONE,
   "Release Date & time: %s - %s".encode ('utf-8'),
   LOAD_TEST_VERSION_DATE.encode ('utf-8'), LOAD_TEST_VERSION_TIME.encode ('utf-8')
   )

   cerver.utils.cerver_log_both (
   cerver.utils.LOG_TYPE_NONE, cerver.utils.LOG_TYPE_NONE,
   "Author: %s\n".encode ('utf-8'),
   LOAD_TEST_VERSION_AUTHOR.encode ('utf-8')
   )

def api_version_print_version_id ():
   cerver.utils.cerver_log_both (
   cerver.utils.LOG_TYPE_NONE, cerver.utils.LOG_TYPE_NONE,
   "\nLoadTest PyCerver Version ID: %s\n".encode ('utf-8'),
   LOAD_TEST_VERSION.encode ('utf-8')
   )

def api_version_print_version_name ():
   cerver.utils.cerver_log_both (
   cerver.utils.LOG_TYPE_NONE, cerver.utils.LOG_TYPE_NONE,
   "\nLoadTest PyCerver Version: %s\n".encode ('utf-8'),
   LOAD_TEST_VERSION_NAME.encode ('utf-8')
   )