nums = [0,0,1,1,1,2,2,3,3,4]
i=1
length = 0
while i!=len(nums):
    if nums[i]==nums[i-1]:
        nums.remove(nums[i])
        nums.append("_")
    i+=1
for i in nums:
    if type(i)==int:
        length+=1
print(length,",nums =",nums,sep="")