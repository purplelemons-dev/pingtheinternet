import os
from json import dumps

# to name the file the current date
from datetime import datetime


def ping(ip: str):
    response = os.system(f"ping -c 2 {ip}")
    return response


NOW = datetime.now().strftime('%Y-%m-%d')
MAIN = {}


def main():
    for a in range(1, 256):
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
                for d in range(1, 255):
                    ip = f"{a}.{b}.{c}.{d}"
                    response = ping(ip)
                    MAIN[ip] = response

                with open(
                    f"./data/result_{NOW}.json", "w"
                ) as f:
                    f.write(dumps(MAIN, indent=4))


if __name__ == "__main__":
    main()
