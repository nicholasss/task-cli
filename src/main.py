import argparse
import logging

import json_handler

logging.basicConfig(
	level=logging.DEBUG,
	format="%(asctime)s %(levelname)s %(message)s"
)

logging.info("Initializing main.py")
parser = argparse.ArgumentParser()

logging.debug(f"Arguments passed are %% \"{parser.parse_args()}\"")