import os, logging, datetime
from pathlib import Path
from enum import Enum

import orjson


DATA_DIR_NAME = "data"
JSON_DATA_NAME = "todo_list.json"
CURRENT_DIRECTORY = os.getcwd()

ID_FN = "id"
DESCR_FN = "description"
STATU_FN = "status"
CREAT_FN = "createdAt"
UPDAT_FN = "updatedAt"


class Status(Enum):
	Done = "done"
	To_Do = "todo"
	In_Progress = "in-progress"

logging.basicConfig(
	level=logging.DEBUG,
	format="%(asctime)s %(levelname)s %(message)s"
)

logging.info("Initializing json_handler.py")
logging.debug(f"Current Directory %% {CURRENT_DIRECTORY}")


def __create_data_dir():
	"""Creates the data directory './data' if it does not exist already."""
	data_dir_path = Path(f"{CURRENT_DIRECTORY}/{DATA_DIR_NAME}")
	logging.debug(f"Data Directory Path %% {data_dir_path}")
	if not data_dir_path.is_dir():
		os.mkdir(data_dir_path)
		logging.debug("Created Data Directory.")
	else:
		logging.debug("Prexisting Data Directory")

def __read_file_b(file_path: str) -> bytes:
	"""Reading arbitrary bytes to file."""
	with file_path.open("rb") as file:
			file_data = file.read()
			logging.debug(f"Opened file at path %% {file_path}")
			return file_data

def __write_file_b(file_path: str, file_data: bytes):
	"""Writing arbitrary bytes to file."""
	with file_path.open("wb") as file:
			file.write(file_data)
			logging.debug(f"Wrote to file at path %% {file_path}")

# write to file
def add_item(item_description: str) -> int:
	"""Adds item to the JSON file."""
	# ID, Description, status, createdAt, updatedAt
	__create_data_dir()

	current_utc_time = datetime.datetime.now(datetime.timezone.utc).isoformat()

	json_file_path = Path(f"{CURRENT_DIRECTORY}/{DATA_DIR_NAME}/{JSON_DATA_NAME}")
	logging.debug(f"JSON File Path %% {json_file_path}")

	item_dict = {
			ID_FN: 0,
			DESCR_FN: item_description,
			STATU_FN: Status.To_Do, # Explicitly set to To_Do
			CREAT_FN: current_utc_time,
			UPDAT_FN: current_utc_time
		}

	if not json_file_path.exists():
		logging.debug("Creating JSON file.")

		item_dict[ID_FN] = 1
		logging.debug(f"Item ID of {item_dict[ID_FN]} provided.")
		logging.debug(f"Status of '{item_dict[STATU_FN]}' provided.")

		file_array = [item_dict]
		json_data = orjson.dumps(file_array)
		__write_file_b(json_file_path, json_data)
		
		logging.debug("Wrote one item to new JSON file.")

	else:
		logging.debug("Opened file to append a new item.")

		previous_json_data = __read_file_b(json_file_path)
		previous_file_array = orjson.loads(previous_json_data)
		item_dict[ID_FN] = len(previous_file_array) + 1
		logging.debug(f"Item ID of {item_dict[ID_FN]} provided.")
		logging.debug(f"Status of '{item_dict[STATU_FN]}' provided.")

		previous_file_array.append(item_dict)
		json_data = orjson.dumps(previous_file_array)

		__write_file_b(json_file_path, json_data)

	return item_dict[ID_FN]

# load file