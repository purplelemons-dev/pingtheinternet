from app import FILENAME, loads

with open(f"./data/{FILENAME}", "r") as f:
    MAIN = loads(f.read())
    print(f"loaded {len(MAIN)} IPs")

count = len({ip for ip in MAIN if MAIN[ip] == 0})

print(f"Responsive IPs: {count}")
