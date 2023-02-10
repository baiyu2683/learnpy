#!/usr/bin/env python3
# 日志记录

import logging


logging.debug("Debugging information")
logging.info("Information message")
logging.warning("Warning:config file %s not found", "server.conf")
logging.error("Error occurred")
logging.critical("Critical error -- shutting down")
