def merge_lists_to_dictionary(keys, values):
    return dict(zip(keys, values))
merge_lists_to_dictionary(['a', 'b', 'c'], [1, 2, 3])
# Output: {'a': 1, 'b': 2, 'c': 3}
