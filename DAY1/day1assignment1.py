'''
Given:
D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new':3 }
Create below:
1. union of keys, #value does not matter D_UNION = { 'ok': 1, 'nok': 2 , 'new':3  } 
2. intersection of keys, #value does not matter D_INTERSECTION = {'ok': 1}
3. D1- D2 = {'nok': 2 }values are added for same keys
4 .D_MERGE = { 'ok': 3, 'nok': 2 , 'new':3  }
'''

#function defination of union
def union_dictionry(d1,d2):
    result={**d1}
    for i in d2.keys():
        if i not in result:
            result[i]=d2[i]
    return result

#function defination of intersection
def intersection_dictionry(d1,d2):
    result={}
    for i in d1.keys():
        if i in d2:
            result[i]=d1[i]
    return result 
#funtion defination for substraction
def substraction_dictionry(d1,d2):
    result={}
    for i in d1.keys():
        if i not in d2:
            result[i]=d1[i]
    return result 

#funtion defination for merge
def merge_dictionry(d1,d2):
    result={**d1}
    for i in d2.keys():
        if i in result:
            result[i]=d1[i]+d2[i]            
        else:
            result[i]=d2[i]
    return result
    
if __name__=='__main__':
    #input data
    d1 = {'ok':1, 'nok':2}
    d2 = {'ok':2, 'new':3}
    
    #function call for union operation
    union_output=union_dictionry(d1,d2)
    print("output of union operation : ")
    print(union_output)
    
    #funtion call for intersection operation
    intersection_output=intersection_dictionry(d1,d2)
    print("output of intersection operation :")
    print(intersection_output)
    
    #funtion call for substraction operation
    substraction_output=substraction_dictionry(d1,d2)
    print("output of substraction opeartion :")
    print(substraction_output)
    
    #function call for merge operation 
    merge_output=merge_dictionry(d1,d2)
    print("output of merge operation :")
    print(merge_output)
    