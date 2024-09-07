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

	if not json_file_path.exists():
		logging.debug("Creating JSON file.")

		item_id = 1
		logging.debug(f"Item ID of {item_id} provided.")

		item_status = Status.TODO
		logging.debug(f"Status of '{item_status.value}' provided.")

		item_dict = {
			ID_FN: item_id,
			DESCR_FN: item_description,
			STATU_FN: item_status,
			CREAT_FN: current_utc_time,
			UPDAT_FN: current_utc_time
		}
		file_dict = {"todo": item_dict}
		json_data = orjson.dumps(file_dict)

		with json_file_path.open("wb") as file:
			file.write(json_data)

		

	else:
		logging.debug("JSON file exists, appending item.")
		# open, deserialize, add item to array, write to file

		# item ID is updated to be correct when added
		item_id = 2



	return item_id

# load file