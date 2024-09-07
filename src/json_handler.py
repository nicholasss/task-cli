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
def add_item(item_description: str) -> int:
	"""Adds item to the JSON file."""
	# ID, Description, status, createdAt, updatedAt
	__create_data_dir()

	current_utc_time = datetime.datetime.now(datetime.timezone.utc).isoformat()
	item_id: int

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

		with json_file_path.open("wb") as file:
			file.write(json_data)
			logging.debug("Wrote one item to new JSON file.")

	else:
		logging.debug("JSON file exists, appending item.")
		# open, deserialize, add item to array, write to file

		logging.warning("Adding to a previously created list is not supported yet.")

		with json_file_path.open("rb") as file:
			previous_json_data = file.read()
			logging.debug("Opened file to append a new item.")

		previous_file_array = orjson.loads(previous_json_data)
		item_dict[ID_FN] = len(previous_file_array) + 1
		logging.debug(f"Item ID of {item_dict[ID_FN]} provided.")
		logging.debug(f"Status of '{item_dict[STATU_FN]}' provided.")

		print(previous_file_array)

		previous_file_array.append(item_dict)
		json_data = orjson.dumps(previous_file_array)

		with json_file_path.open("wb") as file:
			file.write(json_data)
			logging.debug("Wrote new item to JSON file.")

	return item_dict[ID_FN]

# load file