from collections import namedtuple
from csv import reader
from json import load, dump
from typing import Tuple


Guy = namedtuple('Scholar',
            'account_name rental_ronin payout_ronin penalties additional private_key')

def get_private_keys() -> dict:
    with open('secret_keys.json', 'r', encoding='UTF-8') as f:
        return load(f)

def get_guys(file_name: str) -> Tuple[Guy]:
    keys = get_private_keys()
    with open(file_name, 'r', encoding='UTF-8') as f:
        return [Guy(row[0], row[1], row[2],
                    int(row[3] or 0), int(row[4] or 0), keys[row[1]])
                for row in tuple(reader(f))[1:] if row[2]]

def save_claims_log(claims: dict) -> None:
    with open('claimed_slp.json', 'w', encoding='UTF-8') as f:
        dump(claims, f, indent=4, ensure_ascii=False)

def get_claims_log() -> dict:
    with open('claimed_slp.json', 'r', encoding='UTF-8') as f:
        return load(f)