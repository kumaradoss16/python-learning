def filter_duplicates(event_ids):
    seen = set()
    unique_events = []
    for event_id in event_ids:
        if event_id not in seen:
            seen.add(event_id)
            unique_events.append(event_id)

    return unique_events

event_ids = ["LOGIN", "LOGOUT", "LOGIN", "ERROR", "LOGIN", "ERROR"]

result = filter_duplicates(event_ids)

print(result)