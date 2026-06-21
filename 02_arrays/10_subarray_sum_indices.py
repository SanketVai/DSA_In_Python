def build_prefix_sum(arr):
    if len(arr) == 0:
        return []

    prefix = [0] * len(arr)
    prefix[0] = arr[0]

    for i in range(1, len(arr)):
        prefix[i] = prefix[i - 1] + arr[i]

    return prefix


def build_subarray_sum_indices(arr, k):
    if len(arr) == 0:
        return []

    prefix = build_prefix_sum(arr)
    print(f"Prefix Sum = {prefix}")

    # prefix_sum -> list of indices where it occurred
    positions = {0: [-1]}

    answer = []

    for i in range(len(prefix)):

        target = prefix[i] - k

        # Have we seen this prefix sum before?
        if target in positions:

            # There may be multiple previous indices
            for prev_index in positions[target]:
                start = prev_index + 1
                end = i

                answer.append((start, end))

        # Store current index for current prefix sum
        if prefix[i] not in positions:
            positions[prefix[i]] = []

        positions[prefix[i]].append(i)

    return answer


# Input
arr = [1, 2, 1, 3]
k = 4

print(build_subarray_sum_indices(arr, k))


def build_subarray_sum_indices(arr, k):
    positions = {0: [-1]}
    prefix = 0
    answer = []

    for i, num in enumerate(arr):
        prefix += num
        target = prefix - k

        if target in positions:
            for prev_index in positions[target]:
                answer.append((prev_index + 1, i))

        positions.setdefault(prefix, []).append(i)

    return answer