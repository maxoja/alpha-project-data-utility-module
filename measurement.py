#measurement.py

def squared_error_list(list1, list2):
    try:
        len1 = len(list1)
    except:
        len1 = list1.size
        
    try:
        len2 = len(list2)
    except:
        len2 = list2.size
        
    assert(len1 == len2)
    
    return sum([ (list1[i] - list2[i])**2 for i in range(len1) ])/len1