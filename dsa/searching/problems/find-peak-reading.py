def find_peak_reading(readings):
    low, high = 0, len(readings) - 1
    while high - low > 2:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3
        if readings[mid1] < readings[mid2]:
            low = mid1 + 1
        else:
            high = mid2 - 1

    return low + readings[low:high + 1].index(max(readings[low:high + 1]))


hourly_temps = [60, 63, 67, 72, 75, 78, 80, 76, 71, 65]
print(find_peak_reading(hourly_temps))