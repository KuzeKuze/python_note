#这里定义几个函数和解包
def print_two( *args ):
	arg1, arg2 = args		#解包操作
	print( f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
	print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
	print(f"arg1: {arg1}")

def print_none():
	print("I got nothin'.")

print_two("Kuze","Du")
print_two_again("Kuze","Du")
print_one("First")
print_none()