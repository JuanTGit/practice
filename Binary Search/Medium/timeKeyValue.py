# 981. Time Based Key-Value Store
# Medium
# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

# Implement the TimeMap class:

# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
 

# Example 1:

# Input
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
# Output
# [null, null, "bar", "bar", null, "bar2", "bar2"]

# Explanation
# TimeMap timeMap = new TimeMap();
# timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
# timeMap.get("foo", 1);         // return "bar"
# timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
# timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
# timeMap.get("foo", 4);         // return "bar2"
# timeMap.get("foo", 5);         // return "bar2"
 

# Constraints:

# 1 <= key.length, value.length <= 100
# key and value consist of lowercase English letters and digits.
# 1 <= timestamp <= 107

class TimeMap:

    def __init__(self):
        self.table = {}

    def set(self, key, value, timestamp):
        if key not in self.table:
            self.table[key] = []

        self.table[key].append((value, timestamp))

    def get(self, key, timestamp):
        if key not in self.table:
            return ""

        keyTable = self.table[key]

        start, end = 0, len(keyTable) - 1

        while start <= end:
            mid = (start + end) // 2
            if timestamp > keyTable[mid][1]:
                start = mid + 1
            elif timestamp < keyTable[mid][1]:
                end = mid - 1
            else:
                return self.table[key][mid][0]
        middle = (start + end) // 2
        return keyTable[middle][0] if timestamp >= keyTable[middle][1] else ""



table = {}
def createTimeMap(key, value, time):

    table[key] = table.get(key, []) + [(value, time)]



def getTimeMap(key, time):
    start, end = table[key][0][1], table[key][-1][1]
    print(start, end)

    # for items in table[key]:
    #     mid = (start + end) // 2


createTimeMap('foo', 'bar', 1)
createTimeMap('foo', 'bar2', 2)
createTimeMap('foo', 'bar3', 5)
createTimeMap('foo2', 'bar3', 4)



getTimeMap('foo', 3)