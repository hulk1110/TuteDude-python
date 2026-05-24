#operation on sets

nums ={11,12,7,3,18,20}
#memebership operation
print(5 in nums)
print(7 in nums)
print(1 not in nums)

# concationation,repeatation  (not supported
nums2 = {1,3,4}
# print(nums+ nums2)
# print(nums**2)

weekdays= ("mon","tue","wed","thu","fri","sat","sun")
weekdays2 = set(weekdays)
# they will come in unorderd sequence now
print(weekdays2)

# they are mutable

nums.add(1)
print(nums)
nums.add(13)
print(nums)
nums.remove(13)
print(nums)