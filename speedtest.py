import heapq
from collections import defaultdict

def get_top_error_sensors(filepath: str, top_n: int = 5) -> list[tuple[str, int]]:
    error_counts = defaultdict(int)

    with open(filepath, "r") as f:
        for line in f:
            parts = line.split()
            if len(parts) == 2 and parts[1] == "ERROR":
                error_counts[parts[0]] += 1

    return heapq.nlargest(top_n, error_counts.items(), key=lambda x: x[1])
if _name_ == "_main_":
    results = get_top_error_sensors("sensors.log")
    for sensor, count in results:
        print(f"{sensor}: {count}")
