def make_bricks(s1, b5, goal):
	return (goal - min(goal // 5, b5) * 5) <= s1

#I wanted to not use a variable and just type [a,b,c] manually to get a single line, but I decided against it.
def lone_sum(a, b, c):
	lst = [a,b,c]
	return sum(lst[i] for i in range(3) if lst[i] not in (lst[:i] + lst[i+1:]))

def lucky_sum(a, b, c):
	lst = [a,b,c]
	return sum(lst[:lst.index(13)]) if 13 in lst else sum(lst)

def no_teen_sum(a, b, c):
	lst = [a,b,c]
	return sum(i for i in lst if i in [15,16] or i not in range(13,20))

def round_sum(a, b, c):
	lst = [a,b,c]
	return sum(i//10*10 if i % 10 < 5 else (i//10+1)*10 for i in lst)

#if I try to do this in one line, it's going to be really long, so I decided against it.
def close_far(a, b, c):
	if min(abs(a - b), abs(a - c)) > 1 : return False
	if abs(a - c) <= 1 : b,c = c,b
	return(abs(c-a) >= 2 and abs(c-b) >= 2)

#basically the same as the make_bricks one. 
def make_chocolate(s1, b5, goal):
	goal -= min(goal//5,b5) * 5
 	return goal if goal <= s1 else -1