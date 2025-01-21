def find_duplicate(numlist):
    """
    Returns True if there is a duplicate number in the list, otherwise False.
    Time complexity: O(n) where n is the length of the list (due to set lookups and insertions).
    Space complexity: O(n) due to the set used to track seen numbers.
    """
    seen_set = set()  # Set to store numbers we've encountered

    # Iterate through the list
    for num in numlist:
        if num in seen_set:  # Duplicate found
            return True
        seen_set.add(num)  # Add the current number to the set
    
    return False  # No duplicates found

# Test the function
print(find_duplicate([1, 3, 4, 5, 14]))  # Output: False
