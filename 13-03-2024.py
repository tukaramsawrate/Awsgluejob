1.
def longest_common_prefix(strs):
    if not strs:
        return ""
    
    shortest_str = min(strs, key=len)
    
    for i, char in enumerate(shortest_str):
        for string in strs:
            if string[i] != char:
                return shortest_str[:i]
    
    return shortest_str

strs1 = ["flower", "flow", "flight"]
print(longest_common_prefix(strs1))  

strs2 = ["dog", "racecar", "car"]
print(longest_common_prefix(strs2))  


2.
def str_str(haystack, needle):
    if not needle:
        return 0
    
    if len(needle) > len(haystack):
        return -1
    
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    
    return -1

haystack1 = "sadbutsad"
needle1 = "sad"
print(str_str(haystack1, needle1))  

haystack2 = "leetcode"
needle2 = "leeto"
print(str_str(haystack2, needle2))  
