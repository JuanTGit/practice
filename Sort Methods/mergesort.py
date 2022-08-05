"""
Selects entire array
Split the selected array(as evenly as possible)
Selects left array
Calls merge sort on the split array (splits again)
Continues to split the left array until we have a length of one.
Merge selected arrays back together, in sorted order.
Then goes to the right.
Merges the two split arrays and sorts starting with the 0 index from both sides.
Worst case: O(n log n) - Linear Logarithmic
"""

# Step 1: Split everything into it's own group down to len == 1
# Step 2: From left to right, merge two groups together
# Step 3: While merging, place eath item in the correct index position in the main list
# Step 4: Continue until we have only one group left

def merge_sort(array):
    # If the length of our array is greater than 1. This includes calling upon it's self until it is down to len == 1
    if len(array) > 1:
        # We want to floor divide(split evenly w/o floats) the array by 2, and set it to our variable mid.
        mid = len(array) // 2
        # Our left half will be from the beginning of our array up until the middle
        left_half = array[:mid]
        # Our right half will be from the middle until the end
        right_half = array[mid:]

        # We call our function on it's left half to recursively split our array.
        merge_sort(left_half)
        merge_sort(right_half)

        # 0 Index pointers for our lists
        l = 0 # pointer for left half list
        r = 0 # pointer for right half list
        m = 0 # pointer for main list

        # While our index at l or r pointer is < the length of our left/right_half execute.
        while l < len(left_half) and r < len(right_half):
            # If the integer at our left_half at index l is greater than the integer of our right half at index r
            if left_half[l] < right_half[r]:
                # In place set our main array at index m starting at index 0 to the integer of the left_half at index l
                array[m] = left_half[l]
                # Increase our left pointer by 1                
                l += 1
            else:
                array[m] = right_half[r]
                r += 1
            # We want to increase the pointer for the main array to have our integers placed in the correct index
            m += 1
        

        # In the case we have nothing to compare our right or left array to (left over elements)
        while l < len(left_half):
            array[m] = left_half[l]
            l += 1
            m += 1
        while r < len(right_half):
            array[m] = right_half[r]
            r += 1
            m += 1

arr_test = [3, 5, 1, 7, 2, 6, 24, 6, 8]

merge_sort(arr_test)
print(arr_test)