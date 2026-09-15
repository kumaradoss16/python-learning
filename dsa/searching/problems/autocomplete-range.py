def autocomplete_range(sorted_words, prefix):
    import bisect

    low = bisect.bisect_left(sorted_words, prefix)
    high = bisect.bisect_left(sorted_words, prefix[:-1] + chr(ord(prefix[-1]) + 1))
    return sorted_words[low:high]

words = ["apple", "application", "apply", "banana", "band", "bandana"]
print(autocomplete_range(words, 'app'))

