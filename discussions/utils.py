import json
from collections import Counter
from uuid import uuid4

from storage.fake_db import fake_db


def get_contact_discussions(data):
    discussions = fake_db.get("discussions", {}).values()
    for discussion in discussions:
        contact_id = discussion.get("contacts")
        if Counter(contact_id) == Counter(data):
            return discussion
    return None


def create_new_discussion(data):
    discussions = fake_db.get("discussions", {})

    discussion_id = str(uuid4())
    discussion_data = data.model_dump()
    discussion_data["id"] = discussion_id
    discussions[discussion_id] = discussion_data

    with open("storage/discussions.json", "w") as file:
        json.dump(discussions, file, default=str)

    return discussion_data


def get_discussions(user_id):
    discussion_list = []
    users = fake_db.get("users", {})
    discussions = fake_db.get("discussions", {}).values()

    for discussion in discussions:
        contacts = discussion.get("contacts", [])

        one_to_one = contacts[0] != contacts[1]
        yourself = contacts[0] == contacts[1]

        if user_id in contacts:
            if one_to_one:
                text = ""
                for contact in contacts:
                    if user_id != contact:
                        text = text + users.get(contact)["name"] + ", "
                discussion["name"] = text[:-2]
            elif yourself:
                contact = contacts[0]
                if user_id == contact:
                    discussion["name"] = "You"

            discussion_list.append(discussion)

    return discussion_list
