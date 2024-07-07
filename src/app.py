import os
from json import dumps, loads
from threading import Thread

# to name the file the current date
from datetime import datetime


def ping(ip: str):
    response = os.system(f"ping -c 2 {ip}")
    return response


NOW = datetime.now().strftime("%Y-%m-%d")

FILENAME = "result_2024-07-02.json"
with open(f"./data/{FILENAME}", "r") as f:
    MAIN: dict[str, str] = loads(f.read())
    print(f"loaded {len(MAIN)} IPs")

START_IP = (1, 35, 61, 0)


def main():
    for a in range(1, 224):
        if a in {10, 127}:
            continue
        for b in range(1, 256):
            print(f"Current: {a}.{b}.0.0/16")
            if (
                (a == 172 and b in range(16, 32))
                or (a == 192 and b == 168)
                or (a == 100 and b in range(64, 128))
                or (a == 169 and b == 254)
            ):
                continue
            for c in range(1, 256):
                pool: list[Thread] = []
                for d in range(1, 255):
                    if (a, b, c, d) < START_IP:
                        continue
                    ip = f"{a}.{b}.{c}.{d}"
                    t = Thread(target=lambda: MAIN.update({ip: ping(ip)}))
                    t.start()
                    pool.append(t)

                for t in pool:
                    t.join()

                with open(f"./data/{FILENAME}", "w") as f:
                    f.write(dumps(MAIN, indent=4))


if __name__ == "__main__":
    main()
