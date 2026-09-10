def count_occurrences(items):
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts


log_codes = ["404", "500", "404", "200", "500", "500"]
print(count_occurrences(log_codes))