
#This is a program to find the number of characters to be removed to form an anagram, given 2 strings 
#https://www.geeksforgeeks.org/using-counter-python-find-minimum-character-removal-make-two-strings-anagram/
from collections import Counter
def anagram(st1,st2):
    c = 0
    #using Counter, convert the string to a dictionary 
    dict1 = Counter(st1)
    dict2 = Counter(st2)
    #get a list of the keys of the dictionary
    keys1 = dict1.keys()
    keys2 = dict2.keys()
    #count the total number of keys
    count1 = len(keys1)
    count2 = len(keys2)
    #create a set of the keys to find out the intersection 
    set1 = set(dict1.keys())
    set2 = set(dict2.keys())
    print(set1)
    commonkeys = (set1.intersection(set2))
    print(commonkeys)
    #find the common keys and compare the differences in occurences 
    for d in commonkeys:
        if(dict1[d]!=dict2[d]):
            c = abs(dict2[d]-dict1[d])
        
    if (commonkeys == 0):
        return count1 + count2
    else :
        return (max(count1,count2)-len(commonkeys)) + c
st1 = "bcadeh"
st2 = "hea"
print (anagram(st1,st2))