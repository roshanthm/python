def merge_three_dictionaries(dict1, dict2, dict3):
    return {**dict1, **dict2, **dict3}
merge_three_dictionaries({'a': 1}, {'b': 2}, {'a': 3})
# Output: {'a': 3, 'b': 2}
