import argparse
import logging

import json_handler as jh
from utils import *


LOGGING_LEVEL = logging.DEBUG


logging.basicConfig(level=LOGGING_LEVEL,
                    format="%(asctime)s %(levelname)s %(message)s")

logging.debug("Initializing main.py")
parser = argparse.ArgumentParser(
    description="To Do List CLI written in Python.")

parser.add_argument(
    "-a", "--add", help="Add an item to the list.", metavar="Item")
parser.add_argument(
    "-l", "--list", help="List out all items on the list.", nargs='?', const='all')
parser.add_argument(
    "-u",
    "--update",
    help="Update description of specified task.",
    nargs=2,
    metavar=("ID", "Description"),
)
parser.add_argument(
    "-md", "--mark-done", help="Mark an item as done.", metavar="ID")
parser.add_argument(
    "-mip", "--mark-in-progress", help="Mark an item as in-progress.", metavar='ID'
)
parser.add_argument(
    "-mt", "--mark-todo", help="Mark an item as to-do.", metavar="ID"
)
parser.add_argument(
    "-d", "--delete", help="Deletes specified task.", metavar="ID")

# TODO: Add a argument for marking the items a different status

args = parser.parse_args()
logging.debug(f'Arguments passed are %% "{args}"')

if args.add:
    logging.debug("'--add' argument found.")
    added_item_id = jh.add_item(args.add)
    print(f" %%% Item added successfully. (ID: {added_item_id})")

if args.list:
    list_arg = args.list
    if list_arg == 'all':
        logging.debug("'--list' argument found.")
        jh.list_items()
    elif list_arg == 'done':
        logging.debug("'--list done' argument found.")
        jh.list_conditional_items('done')
    elif list_arg == 'todo':
        logging.debug("'--list todo' argument found.")
        jh.list_conditional_items('todo')
    elif list_arg == 'in-progress':
        logging.debug("'--list in-progress' argument found.")
        jh.list_conditional_items('in-progress')

if args.update:
    logging.debug("'--update' argument found.")
    if not args.update[0].isdigit():
        logging.warning("First argument needs to be a task id.")
    jh.update_item_desc(int(args.update[0]), args.update[1])

if args.mark_done:
    logging.debug("'--mark-done' arugment found.")
    jh.update_item_status(int(args.mark_done), Status.Done)

if args.mark_in_progress:
    logging.debug("'--mark-in-progress' arugment found.")
    jh.update_item_status(int(args.mark_in_progress), Status.In_Progress)

if args.mark_todo:
    logging.debug("'--mark-todo' arugment found.")
    jh.update_item_status(int(args.mark_todo), Status.To_Do)

if args.delete:
    logging.debug("'--delete' argument found.")
    if not args.delete.isdigit():
        logging.warning("'--delete' argument requires a task id.")
    jh.delete_item(int(args.delete))
