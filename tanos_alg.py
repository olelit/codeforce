def tanos_sort(item):
    center = len(item) // 2
    if sorted(item) == item:
        return len(item)
    return max(tanos_sort(item[:center]), tanos_sort(item[center:]))

n = int(input())
item = list(map(int, input().split()))
print(tanos_sort(item))
