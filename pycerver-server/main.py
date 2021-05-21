import signal 
import sys
from service import version as v
from service import loads, conf, db
from cerver import *

if __name__ == "__main__":
    signal.signal(signal.SIGPIPE, signal.SIG_IGN)

    cerver_initialize(conf.end)
    v.loads_version_print_full()
    loads.loads_config ()

    db.load_mongo_init()
    conf.start()