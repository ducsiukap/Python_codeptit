def count_inversions(arr):
    def merge_count_split_inv(left, right):
        i, j = 0, 0
        merged = []
        inv_count = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inv_count += len(left) - i  # Tất cả phần tử còn lại trong left đều > right[j]
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inv_count

    def sort_and_count(arr):
        if len(arr) < 2:
            return arr, 0
        mid = len(arr) // 2
        left, left_inv = sort_and_count(arr[:mid])
        right, right_inv = sort_and_count(arr[mid:])
        merged, split_inv = merge_count_split_inv(left, right)
        return merged, left_inv + right_inv + split_inv

    _, total_inv = sort_and_count(arr)
    return total_inv


# Input
n = int(input())
a = list(map(int, input().split()))

# Output
print(count_inversions(a))
