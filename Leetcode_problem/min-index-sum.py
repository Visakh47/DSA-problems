class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
#         matchedIndex = []
#         matchedEle = []
#         rslt = []
#         for i in range(0,len(list1)):
#             for j in range(0,len(list2)):
#                 if(list1[i]==list2[j]):
#                     matchedIndex.append(i+j)
#                     matchedEle.append(list2[j])
        
#         minEle = matchedIndex.index(min(matchedIndex))
#         rslt.append(matchedEle[minEle])
        
        
#         for i in range(0,len(matchedIndex)):
#             if (min(matchedIndex) == matchedIndex[i]):
#                 rslt.append(matchedEle[i])
        
#         if len(rslt) > 1 :
#             rslt.pop(0)
        
#         return rslt

        common = list(set(list1).intersection(list2))
        ans = []
        matchedIndex = []
        
        for i in range(len(common)):
            matchedIndex.append(list1.index(common[i]) + list2.index(common[i])) #we are getting the matched Indexes list1.index(element) , finding the sum of matchedIndex 
        
        minSum = min(matchedIndex)
        
        while (minSum in matchedIndex):
            ans.append(common[matchedIndex.index(minSum)])  # appending the common element found at index of minimumSum in matchedIndexes
            common.remove(common[matchedIndex.index(minSum)]) # removing that element from common element 
            matchedIndex.remove(minSum) #removing that minimum Index
        
        return ans
            
            
            
            
                    