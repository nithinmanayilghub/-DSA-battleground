############################################DAY-1##############################################################
def sort_by_tuple_sum(lst: list[tuple]) -> list[tuple]:
    lst = sorted(lst, key=lambda x: x[0] + x[1], reverse=False)
    return lst


# Input
l1 = [(3, 1), (2, 2), (5, -1), (0, 0)]

print(sort_by_tuple_sum(l1))

l2 = [(7, 3), (1, 2), (4, 5), (0, 1)]
print(sort_by_tuple_sum(l2))

l3 = [(8, -3), (1, 1), (2, 0), (5, 5), (3, 2)]
print(sort_by_tuple_sum(l3))

###############################################DAY-2###########################################################
# def filter_strings(lst: list[str], k: int, m: int) -> list[str]:
#     res = [x for x in lst if len(x) >= k]
#     res = [
#         x for x in res if v in x for v in ["a", "i", "e", "o", "u"] if sum(len(v)) >= m
#     ]
#     return res


def filter_strings(lst: list[str], k: int, m: int) -> list[str]:
    res = [x for x in lst if len(x) >= k]  # Keep only strings with length >= k
    vowels = ["a", "e", "i", "o", "u"]  # Define vowel set
    res = [
        x for x in res if sum(x.count(ch) for ch in x if ch in vowels) >= m
    ]  # Count vowels
    return res


l1 = ["apple", "hi", "world", "yes", "python"]
k = 4
m = 2

print(filter_strings(l1, k=k, m=m))

l2 = ["eduction", "science", "art", "mathematics"]
k = 5
m = 3
print(filter_strings(l2, k=5, m=3))
