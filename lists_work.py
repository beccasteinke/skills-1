def print_indices(items):

    for indices, item in enumerate(items):
        print(indices, item)

items = ['apple', 'berry', 'cherry']
print_indices(items)


def words_in_common(words1, words2):
    common_words = words1 & words2
    if common_words == set():
        print(empty set)
    print(common_words)

words1 = {'Python', 'Ape'}
words2 = {'Lizard', 'Turtle'}

words_in_common(words1, words2)


def every_other_item(items2):
    every_other = items2[0::2]
    print(every_other)

items2 = 'a', 400, True, 'b', 0
every_other_item(items2)

def smallest_n_items(items3, n):
    Return the `n` smallest integers in list in descending order.

    You can assume that `n` will be less than the length of the list.

    For example:

        >>> smallest_n_items([2, 6006, 700, 42, 6, 59], 3)
        [42, 6, 2]

    If `n` is 0, return an empty list:

        >>> smallest_n_items([3, 4, 5], 0)
        []

    Duplicates are OK:

        >>> smallest_n_items([1, 1, 1, 1, 1, 1], 2)
        [1, 1]
    

    return []"""