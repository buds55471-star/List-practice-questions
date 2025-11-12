''' Remove duplicates from a list without using set().
Create a nested list (a list inside another list) and access an inner item.

Reverse a list manually using slicing (not reverse()).

Flatten a list of lists into a single list.'''

def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

# Example
nums = [1, 2, 2, 3, 1, 4, 5, 4]
print(remove_duplicates(nums))
