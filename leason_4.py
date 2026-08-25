# nums = [1, 2, 4 ,5, "s", True, [4,5,6, 1]]
#
# nums[0] = 10
# nums[5] = 4.1
# print(nums)
# print(nums[0])
# print(nums[-1][2])
numbers = [5,2,7]
numbers.append(100)
numbers.append(True)
numbers.insert(1, False)
print(numbers)             #b = [0,0,0]
numbers.extend([0,0,0])    #numbers.extend([0,0,0]) = numbers.extend(b)
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers.pop(0)
print(numbers)
numbers.remove(2)
print(numbers)
# numbers.clear()
# print(numbers)
print(numbers.count(0))
print(len(numbers))
nums = [5,2,7,"67",False]