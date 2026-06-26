class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except ValueError:
            return -1

# haystack = input("Enter haystack string: ")
# needle = input("Enter needle string: ")
# haystack = haystack.lower()
# needle = needle.lower()
# length = 0
# indexl = []
# i = 0
# while i!=len(haystack)-1:
#     if haystack[i]==needle[length]:
#         length+=1
#         indexl.append(i)
#         #print(haystack[i])
#         if len(needle)==length:
#             print(indexl[0])
#             break
#         i+=1
#     else:
#         if len(indexl)!=0:
#             i=indexl[0]
#         else:
#             i+=1
#         length = 0
#         indexl = []
# if length!=len(needle):
#     print(-1)