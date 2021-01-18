def make_bricks(s1, b5, goal):
	return (goal - min(goal // 5, b5) * 5) <= s1

def lone_sum(*args):
	return sum(args[i] for i in range(len(args)) if args[i] not in (args[:i] + args[i+1:]))

def lucky_sum(*args):
	return sum(args[:args.index(13)]) if 13 in args else sum(args)

def no_teen_sum(*args):
	return sum(i for i in args if i in [15,16] or i not in range(13,20))

def round_sum(*args):
	return sum(i//10*10 if i % 10 < 5 else (i//10+1)*10 for i in args)

#if I try to do this in one line, it's going to be really long, so I decided against it.
def close_far(a, b, c):
	if min(abs(a - b), abs(a - c)) > 1 : return False
	if abs(a - c) <= 1 : b,c = c,b
	return(abs(c-a) >= 2 and abs(c-b) >= 2)

#basically the same as the make_bricks one. 
def make_chocolate(s1, b5, goal):
	goal -= min(goal//5,b5) * 5
 	return goal if goal <= s1 else -1
