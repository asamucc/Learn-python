#返回两数之和为26的角标
target=9
nums=[2,7,11,15]
for i in range(0,4):
    for j in range(i+1,4):
     
     if (nums[i]+nums[j])==26:
        print(i,j)


