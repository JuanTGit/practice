"""
The patterns looks like this for an ascending order set:
    1.) First, find the middle of start and end. An easy way to find the middle would be: middle = (start + end) / 2. 
    But this has a good chance of producing an integer overflow so its recommended that you represent the middle as: middle = start + (end — start) / 2
    2.) If the key is equal to the number at index middle then return middle
    3.) If (key) isnt equal to the index middle:
    4.) Check if key < arr[middle]. If it is reduce your search to end = middle — 1
    5.) Check if key > arr[middle]. If it is reduce your search to end = middle + 1

Problems featuring the Modified Binary Search pattern:
    Order-agnostic Binary Search (easy)
    Search in a Sorted Infinite Array (medium)
"""