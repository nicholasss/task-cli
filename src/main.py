import argparse
import logging

import json_handler

logging.basicConfig(
	level=logging.DEBUG,
	format="%(asctime)s %(levelname)s %(message)s"
)

logging.info("Initializing main.py")
parser = argparse.ArgumentParser(description="To Do List CLI written in Python.")

parser.add_argument('-a', '--add', help="Add an item to the list.", metavar="Item")

logging.debug(f"Arguments passed are %% \"{parser.parse_args()}\"")
