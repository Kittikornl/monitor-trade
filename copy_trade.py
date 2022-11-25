import time

from utils import *


def main():
    send_alert(f"Start monitoring trader")
    sent_positions = {}
    while True:
        positions = []
        res = fetch_open_position()
        positions = res["data"]["otherPositionRetList"]
        out = ["update positions:\n"]
        update_positions = []
        for position in positions:
            # check update 
            if position["symbol"] not in sent_positions:
                sent_positions[position["symbol"]] = position["updateTimeStamp"]
                update_positions.append(position)
            else:
                if sent_positions[position["symbol"]] != position["updateTimeStamp"]:
                    sent_positions[position["symbol"]] = position["updateTimeStamp"]
                    update_positions.append(position)
        for position in update_positions:
            out.append(dict_to_str(position))
        # NOTE: sent alert if have any update
        if len(out) > 1:
            out.append("=" * 40 + "\n")
            send_alert("".join(out))
        time.sleep(FETCH_INTERVAL)


if __name__ == "__main__":
    main()
