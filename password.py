import string
from random import SystemRandom
from random import shuffle

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digit = string.digits
symbol = "~!@#$%^&*()_+-=\|[]{}/?,.<>;:'\""
smallsymbol = "!@#$%^&-+=().,"
allchars = lower+upper+digit+symbol

def gen_pass(length, charset):
	result = ''.join(SystemRandom().choice(charset) for _ in range(length))
	lst = list(result)
	for _ in range(10):
		shuffle(lst)
	result = ''.join(lst)
	return result

for _ in range(1):
	print gen_pass(18, allchars)
