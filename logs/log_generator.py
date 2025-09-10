import time
import random
from datetime import datetime

LOG_FILE = "/opt/log/access.log"  # file mà Flume đang tail

urls = ["/home", "/login", "/products", "/cart", "/checkout", "/profile", "/search"]
status_codes = ["404 Not Found"] * 5 + ["200 OK"] * 3 + ["500 Internal Server Error"]

while True:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0,255)}.{random.randint(0,255)}"
    method = random.choice(["GET", "POST", "PUT", "DELETE"])
    url = random.choice(urls)
    status = random.choice(status_codes)

    log_line = f"{timestamp} - {ip} {method} {url} {status}\n"
    
    with open(LOG_FILE, "a") as f:
        f.write(log_line)
    
    print(log_line)

    time.sleep(random.uniform(0.5, 2))
