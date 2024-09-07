import os, logging, time, uuid
from pathlib import Path

import orjson


DATA_DIR_NAME = "data"
JSON_DATA_NAME = "todo_list.json"
CURRENT_DIRECTORY = os.getcwd()


logging.basicConfig(
	level=logging.DEBUG,
	format="%(asctime)s %(levelname)s %(message)s"
)

logging.info("Initializing json_handler.py")
logging.debug(f"Current Directory %% {CURRENT_DIRECTORY}")

# Goal is to provide objects for this module to serialize directly to the file


def __create_data_dir():
	"""Creates the data dir './data' if it does not exist already."""
	data_dir_path = Path(f"{CURRENT_DIRECTORY}/{DATA_DIR_NAME}")
	logging.debug(f"Data Directory Path %% {data_dir_path}")
	if not data_dir_path.is_dir():
		os.mkdir(data_dir_path)
		logging.debug("Created Data Directory.")
	else:
		logging.debug("Prexisting Data Directory")

# write to file
def add_item(item: str):
	"""Adds item to the JSON file."""
	# ID, Description, status, createdAt, updatedAt
	__create_data_dir()

	json_file_path = Path(f"{CURRENT_DIRECTORY}/{DATA_DIR_NAME}/{JSON_DATA_NAME}")
	logging.debug(f"JSON File Path %% {json_file_path}")

	if not json_file_path.exists():
		logging.debug("Creating JSON file.")
		with json_file_path.open("w") as file:
			file.write(item)

	else:
		logging.debug("JSON file exists, appending item.")
		# open, deserialize, add item to array, write to file


# load file