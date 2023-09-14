def sort_by_avg_ping(rtt: dict) -> dict:
    return dict(sorted(rtt.items(), key=lambda world: world[1]['avg']))
