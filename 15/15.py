import fileinput

starting_nums = list(map(int, next(fileinput.input()).split(',')))

def solve(nums, limit):
    prev = None
    last_spoken = {}

    for i, num in enumerate(starting_nums):
        last_spoken[num] = [None, i]
        prev = num

    i = len(starting_nums)
    for i in range(i, limit):
        if last_spoken[prev][0] is None:
            if 0 in last_spoken:
                last_spoken[0] = [last_spoken[0][1], i]
            else:
                last_spoken[0] = [None, i]
            prev = 0
        else:
            num = last_spoken[prev][1] - last_spoken[prev][0]
            if num in last_spoken:
                last_spoken[num] = [last_spoken[num][1], i]
            else:
                last_spoken[num] = [None, i]
            prev = num
    return num

print(solve(starting_nums, 2020))
print(solve(starting_nums, 30000000))