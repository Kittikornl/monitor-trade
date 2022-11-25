import requests
from config import *


def send_alert(data):
    # NOTE: using discord's webhooks for notification
    data = {
        "content": data,
        "embeds": None,
        "attachments": [],
    }
    requests.post(
        DISCORD_WEB_HOOK,
        data=data,
    )


def dict_to_str(position):
    out = ""
    out += "=" * 40 + "\n"
    for k, i in position.items():
        out += f"{k}: {i}\n"
    return out


# NOTE: fetch trader's positions from binance
def fetch_open_position():
    data = {
        "encryptedUid": USER_ID,
        "tradeType": "PERPETUAL",
    }
    return requests.post(
        TRADER_POSTIONS_URL,
        json=data,
    ).json()
