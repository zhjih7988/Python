# coding: utf-8
import os
import sys

here = os.path.abspath(os.path.dirname(__file__))
sys.path.append(here)

from login.logger import logger

from login.main import run

try:
    run()
except KeyboardInterrupt:
    logger.info("User stop. exit.")
    exit(0)