def first_last6(num):
	return num[0] == 6 or num[-1] == 6

def same_first_last(num):
	return False if len(num) < 1 else num[0] == num[-1]

#not really sure if i should include this one or not, but i'm including it anyway haha.
def make_pi():
	return [3,1,4]

def common_end(a, b):
	return(a[0] == b[0] or a[-1] == b[-1])

#this one feels like cheating, honestly...
def sum3(nums):
	return sum(nums)

def rotate_left3(n):
	return n[1:] + n[:1]

def reverse3(nums):
	return nums[::-1]

def max_end3(nums):
	return 3 * [max(nums[0],nums[-1])]

def sum2(nums):
	return sum(nums[:2])

def middle_way(a, b):
	return[a[1],b[1]]

def make_ends(i):
	return [i[0],i[-1]]

def has23(nums):
	return ((2 in nums) or (3 in nums))