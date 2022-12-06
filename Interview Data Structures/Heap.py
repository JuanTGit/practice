"""
Operation   Time Complexity
---------------------------
Insert  O(logn)
Pop     O(logn)
Min/Max O(1)

Typically Visualized as trees, with either a Min heap or a Max heap.
Where the min/max value is typically the root of the tree, and the children will always be greater/lesser.

The structure of the heap is always going to be a complete tree. Which means that every level in the tree will be completely full
except the last level potentially.

Starts at idx 1, to get elements by multiplying the number by the idx and adding.
"""