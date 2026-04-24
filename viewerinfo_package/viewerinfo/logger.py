import csv
from datetime import datetime

def log_viewer(data: dict, file: str = "viewer_logs.csv"):
    data["timestamp"] = datetime.now().isoformat()
    with open(file, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data.keys())
        if f.tell() == 0:
            writer.writeheader()
        writer.writerow(data)
