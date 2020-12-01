"""Name: Krystyan Severin
   PSID: 1916594"""
# Global variable
num_calls = 0


def partition(user, i, k):
    mid = i + (k - i) // 2
    pivot = user[mid]
    done = False
    low = i
    high = k
    while not done:
        while user[low] < pivot:
            low += 1
        while pivot < user[high]:
            high -= 1
        if low >= high:
            done = True
        else:
            t = user[low]
            user[low] = user[high]
            user[high] = t
            low += 1
            high -= 1
    return high


def quicksort(users, i, k):
    global num_calls
    num_calls += 1
    if i >= k:
        return
    part = partition(users, i, k)
    quicksort(users, i, part)
    quicksort(users, part+1, k)
    return


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()
    # Initial call to quicksort
    quicksort(user_ids, 0, len(user_ids) - 1)
    # Print number of calls to quicksort
    print(num_calls)
    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)
