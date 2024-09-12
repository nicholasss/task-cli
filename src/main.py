import argparse
import logging

import json_handler as jh


LOGGING_LEVEL = logging.DEBUG


logging.basicConfig(level=LOGGING_LEVEL,
                    format="%(asctime)s %(levelname)s %(message)s")

logging.debug("Initializing main.py")
parser = argparse.ArgumentParser(
    description="To Do List CLI written in Python.")

parser.add_argument(
    "-a", "--add", help="Add an item to the list.", metavar="Item")
parser.add_argument(
    "-l", "--list", help="List out all items on the list.", action="store_true"
)
parser.add_argument(
    "-u",
    "--update",
    help="Update description of specified task.",
    nargs=2,
    metavar=("ID", "Description"),
)
parser.add_argument(
    "-d", "--delete", help="Deletes specified task.", metavar="ID")

args = parser.parse_args()
logging.debug(f'Arguments passed are %% "{args}"')

if args.add:
    logging.debug("'--add' argument found.")
    added_item_id = jh.add_item(args.add)
    print(f" %%% Item added successfully. (ID: {added_item_id})")

if args.list:
    logging.debug("'--list' argument found.")
    jh.list_items()

if args.update:
    logging.debug("'--update' argument found.")
    if not args.update[0].isdigit():
        logging.warning("First argument needs to be a task id.")
    jh.update_item(int(args.update[0]), args.update[1])

if args.delete:
    logging.debug("'--delete' argument found.")
    if not args.delete.isdigit():
        logging.warning("'--delete' argument requires a task id.")
    jh.delete_item(int(args.delete))
