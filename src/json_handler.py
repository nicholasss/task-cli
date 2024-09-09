import os, logging, datetime
from pathlib import Path
from enum import Enum

import orjson


DATA_DIR_NAME = "data"
CURRENT_DIRECTORY = os.getcwd()
__JSON_DATA_NAME = "todo_list.json"
JSON_FILE_PATH = Path(f"{CURRENT_DIRECTORY}/{DATA_DIR_NAME}/{__JSON_DATA_NAME}")

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

logging.debug("Initializing json_handler.py")
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

def __read_file_data(file_path: str) -> list[dict[str: any]]:
	"""Reading arbitrary bytes to file."""
	with file_path.open("rb") as file:
			file_data = file.read()
			file_dict = orjson.loads(file_data)

			logging.debug(f"Opened file at path %% {file_path}")
			return file_dict

def __write_file_data(file_path: str, file_dict: list[dict[str: any]]) -> None:
	"""Writing arbitrary bytes to file."""
	with file_path.open("wb") as file:
			file_data = orjson.dumps(file_dict)
			file.write(file_data)
			logging.debug(f"Wrote to file at path %% {file_path}")

# write to file
def add_item(item_description: str) -> int:
	"""Adds item to the JSON file."""
	# ID, Description, status, createdAt, updatedAt
	__create_data_dir()

	current_utc_time = datetime.datetime.now(datetime.timezone.utc).isoformat()

	logging.debug(f"JSON File Path %% {JSON_FILE_PATH}")

	item_dict = {
			ID_FN: 0,
			DESCR_FN: item_description,
			STATU_FN: Status.To_Do, # Explicitly set to To_Do
			CREAT_FN: current_utc_time,
			UPDAT_FN: current_utc_time
		}

	if not JSON_FILE_PATH.exists():
		logging.debug("Creating JSON file.")

		item_dict[ID_FN] = 1
		logging.debug(f"Item ID of {item_dict[ID_FN]} provided.")
		logging.debug(f"Status of '{item_dict[STATU_FN]}' provided.")

		file_array = [item_dict]
		__write_file_data()(JSON_FILE_PATH, file_array)
		
		logging.debug("Wrote one item to new JSON file.")

	else:
		logging.debug("Opened file to append a new item.")

		previous_file_array = __read_file_data(JSON_FILE_PATH)

		highest_item_id = 1
		for item in previous_file_array:
			if item[ID_FN] >= highest_item_id:
				highest_item_id = item[ID_FN] + 1
		item_dict[ID_FN] = highest_item_id
		
		logging.debug(f"Item ID of {item_dict[ID_FN]} provided.")
		logging.debug(f"Status of '{item_dict[STATU_FN]}' provided.")

		previous_file_array.append(item_dict)
		__write_file_data(JSON_FILE_PATH, previous_file_array)

	return item_dict[ID_FN]

def list_items() -> list[str]:
	"""Prints out a list of items in the todo_list json file."""
	if not JSON_FILE_PATH.exists():
		print("No items are in the list.")
	
	else:
		item_list = __read_file_data(JSON_FILE_PATH)
		logging.debug(f"Read from item list %% {JSON_FILE_PATH}")

		print(" %%% Item List:")
		for item in item_list:
			print(f"ID: {item[ID_FN]}, Task: {item[DESCR_FN]}, Status: {item[STATU_FN]}")

def update_item(item_id: int, item_desc: str) -> None:
	"""Updates an item's description."""
	logging.debug(f"Updating ID: {item_id} to Name '{item_desc}'")
	
	if not JSON_FILE_PATH.exists():
		print("No items are in the list.")
	
	else:
		item_list = __read_file_data(JSON_FILE_PATH)
		logging.debug(f"Read from item list %% {JSON_FILE_PATH}")

		for item in item_list:
			if item[ID_FN] == item_id:
				item[DESCR_FN] = item_desc

		__write_file_data(JSON_FILE_PATH, item_list)

def delete_item(item_id: int) -> None:
	"""Deletes a specific item from the list."""
	logging.debug(f"Deleting ID: {item_id}")

	if not JSON_FILE_PATH.exists():
		print("No items are in the list.")
	
	else:
		item_list = __read_file_data(JSON_FILE_PATH)
		logging.debug(f"Read from item list %% {JSON_FILE_PATH}")

		for item in item_list:
			if item[ID_FN] == item_id:
				item_list.remove(item)
		__write_file_data(JSON_FILE_PATH, item_list)