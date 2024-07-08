def quick_sort(candidates, low, high):
    if low < high:
        pi = partition(candidates, low, high)
        quick_sort(candidates, low, pi - 1)
        quick_sort(candidates, pi + 1, high)

def partition(candidates, low, high):
    pivot = candidates[high].vote_count
    i = low - 1
    for j in range(low, high):
        if candidates[j].vote_count > pivot:
            i += 1
            candidates[i], candidates[j] = candidates[j], candidates[i]
    candidates[i + 1], candidates[high] = candidates[high], candidates[i + 1]
    return i + 1
