# Add Card Using Trello CLI

A simple Python command-line tool to create cards on Trello boards. You can specify which list the card should go in within a Trello board, add labels, and include a comment.

---

## Key Concepts

Before using the script, here's a quick overview of Trello terminology:

- **Board** – A workspace where you organize your projects.
- **List** – A column inside a board. There can be multiple lists within a board.
- **Card** – A task or item in a list. Multiple cards can exist within a list.
- **Board ID** – A unique id for your board (required ).
- **List ID** – A unique id for a list (required to create a card within that list).
- **Labels** – Can be attached to cards for categorization.

---
## Setup (followed Trello API Guide: https://developer.atlassian.com/cloud/trello/rest/)

### 1. Create an Account with Trello.com

### 2. Generate Trello API Key and Token

To allow this script to interact with your Trello account, you need:

- **API Key** – Identifies your application.
- **API Token** – Grants access to your Trello data.

Get them here:
- [API Key & Token](https://trello.com/app-key)

**Note:** You need to create a custom Power-Up before generating an API key.

After generating them, set them as environment variables:

```bash
export TRELLO_KEY="your_trello_api_key"
export TRELLO_TOKEN="your_trello_api_token"
```

### 3. Install Dependencies

This script uses the requests library:

```bash
pip install requests
```

### 4. Find Board and List IDs

**Board ID** – Visit your board in Trello and get the ID from the URL:
```
https://trello.com/b/<board_id>/<board-name>
```

Or you can also use the API to get your boards:
```bash
curl "https://api.trello.com/1/members/me/boards?key=$TRELLO_KEY&token=$TRELLO_TOKEN"
```

**List ID** – Use the API to get lists for your board:
```bash
curl "https://api.trello.com/1/boards/<board_id>/lists?key=$TRELLO_KEY&token=$TRELLO_TOKEN"
```

---

## Usage

Run the script from the terminal:

```bash
python3 trello_cards.py <board_id> "<list_name>" "<card_name>" [--labels <label_id_1> <label_id_2> ...] [--comment "Your comment"]
```

### Arguments

- `board_id` – The ID of your board
- `list_name` – Name of the  list (added logic for this to be case-insensitive)
- `card_name` – Name the card
- `--labels` – Optional. List of label IDs to attach
- `--comment` – Optional. Comment to add to the card

---

## Notes

- The script only attaches existing labels. It does not create new labels.
- The script prints the card ID after successful creation.
- Make sure your API key and token are correct; otherwise, API requests will fail. 

---

## Next Steps

Future improvements could include:

- Automatically creating labels if they don't exist
- Better error handling
- Adding unit tests