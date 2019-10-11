
def count_negative_slopes(points):
    """Return the number of pairs of points whose slope is negative.

       We sort the points by x-coordinate and determine how
       many y-coordinates are "inverted" w.r.t their index.

       This is done in O(n log n) time instead of the naive O(n^2).

       The function assumes that no two points share the same x-coordinate.
    """
    return count_inversions([p[1] for p in sorted(points)])


def count_inversions(arr):
    """Return the number of inversions within arr.

       An inversion is a pair not in sorted order.
       That is to say: j > i but arr[i] > arr[j]

       We use the comparison checks within mergesort
       to count the number of right-side elements greater
       than the current left-side element. This gives
       us a running total we return recursively until
       we've sorted the entire array.

       Hence, this is an O(n log n) algorithm.
    """
    if len(arr) < 2:
        return 0
    
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    inversions = count_inversions(left)
    inversions += count_inversions(right)

    index = i = j = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            arr[index] = right[j]
            j += 1
            index += 1
        else:
            arr[index] = left[i]
            i += 1
            index += 1
            inversions += j

    while i < len(left):
        arr[index] = left[i]
        i += 1
        index += 1
        inversions += len(right)

    while j < len(right):
        arr[index] = right[j]
        j += 1
        index += 1

    return inversions


if __name__ == '__main__':

    points = [
        (0, 2),
        (1, 1),
        (2, 4),
        (3, 0),
        (4, 3)
    ]
    print(count_negative_slopes(points))  # 5




