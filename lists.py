"""SKILLS: LISTS

Complete the following functions.
"""


def print_indices(items):
    """Print each item in the list, followed by its index."""
    for indices, item in enumerate(items):
        print(indices, item)

items = ['apple', 'berry', 'cherry']
print_indices(items)

def words_in_common(words1, words2):
    """Return words that are shared between `words1` and `words2`. """
    common_words = words1 & words2
    if len(common_words) == 0: #doesn't seem like most concise way to do this, but it works
        common_words = []
    
    print(common_words)

words1 = {'Python', 'Ape'}
words2 = {'Lizard', 'Turtle'}

words_in_common(words1, words2)
    
def every_other_item(mixed_list):
    """Return every other item in `items`, starting at first item. """
    every_other = mixed_list[0::2]
    print(every_other)

mixed_list = 'a', 400, True, 'b', 0
every_other_item(mixed_list)

def smallest_n_items(nums, n):
    """Return the `n` smallest integers in list in descending order."""
    n = int(-(n + 1)) #this seems like an incorrect workaround, but it works the way I want it to
    print(nums[n:-1])

nums = [2, 6006, 700, 42, 6, 59, 3]
nums.sort(reverse=True)
print(nums)
smallest_n_items(nums, 5)

