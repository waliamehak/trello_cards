#!/usr/bin/env python3
import argparse
import requests
import os

TRELLO_KEY = os.getenv("TRELLO_KEY")
TRELLO_TOKEN = os.getenv("TRELLO_TOKEN")

def main():
    parser = argparse.ArgumentParser(description="Add a card to a Trello board")
    parser.add_argument("board_id", help="Trello board ID")
    parser.add_argument("list_name", help="Name of the column/list")
    parser.add_argument("card_name", help="Name of the card")
    parser.add_argument("--labels", nargs="*", default=[], help="Label IDs to add")
    parser.add_argument("--comment", default="", help="Comment to add to the card")
    args = parser.parse_args()

    if not TRELLO_KEY or not TRELLO_TOKEN:
        print("Error: Please set TRELLO_KEY and TRELLO_TOKEN as environment variables.")
        return
    
    list_id = get_list_id(args.board_id, args.list_name)
    add_card(list_id, args.card_name, labels=args.labels, comment=args.comment)


def get_list_id(board_id, list_name):
    url = f"https://api.trello.com/1/boards/{board_id}/lists"
    params = {"key": TRELLO_KEY, "token": TRELLO_TOKEN}
    response = requests.get(url, params=params)
    response.raise_for_status()
    lists = response.json()
    for lst in lists:
        if lst["name"].lower() == list_name.lower():
            return lst["id"]
    raise ValueError(f"List '{list_name}' not found on board {board_id}")

def add_card(list_id, card_name, labels=[], comment=""):
    url = "https://api.trello.com/1/cards"
    headers = {
        "Accept": "application/json"
    }
    params = {
        "key": TRELLO_KEY,
        "token": TRELLO_TOKEN,
        "idList": list_id,
        "name": card_name,
        "idLabels": ",".join(labels) if labels else None
    }
    response = requests.post(url, params=params)
    response.raise_for_status()
    card = response.json()
    
    if comment:
        comment_url = f"https://api.trello.com/1/cards/{card['id']}/actions/comments"
        comment_params = {"key": TRELLO_KEY, "token": TRELLO_TOKEN, "text": comment}
        requests.post(comment_url, params=comment_params)
    
    print(f"Card '{card_name}' created with ID: {card['id']}")



if __name__ == "__main__":
    main()
