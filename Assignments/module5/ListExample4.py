"""
reverse()
sort()
count()
membership
"""

dayOfweek= ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
print(dayOfweek)
dayOfweek.reverse()
print(dayOfweek)

nums=[23,2,65,31,9]
print(nums)
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
nums=[0,2,34,0,435,0]

# count is used to count number of occurance in list
print(nums.count(0))

item_to_count= int(input(print(f"Enter the number to be counted")))
c=nums.count(item_to_count);
print(f"Occurance of {item_to_count} is : {c}")

languages= ["java","python","js"]

print("python" in languages)
print("java" not in languages)