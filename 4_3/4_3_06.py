def merge(left, right):
    records = []
    leftIndex = rightIndex = 0

    for _ in range(len(left) + len(right)):
        if leftIndex < len(left) and rightIndex < len(right):
            if left[leftIndex] <= right[rightIndex]:
                records.append(left[leftIndex])
                leftIndex += 1
            else:
                records.append(right[rightIndex])
                rightIndex += 1
        elif leftIndex == len(left):
            records.append(right[rightIndex])
            rightIndex += 1
        elif rightIndex == len(right):
            records.append(left[leftIndex])
            leftIndex += 1
    return records


def merge_sort(numList):
    if len(numList) <= 1:
        return numList

    left = merge_sort(numList[:len(numList) // 2])
    right = merge_sort(numList[len(numList) // 2:])

    return merge(left, right)
