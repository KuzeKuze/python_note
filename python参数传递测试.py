from sys import argv
script,file_name = argv
def print_id_arg(arg):
	print(f"在函数内部,b的id为{id(arg)}",end="\n\n")

a = 10
b = [10,20]
c = "str"
d = (10,)
e = open( file_name )

print(id(a))
print_id_arg(a)
print(id(b))
print_id_arg(b)
print(id(c))
print_id_arg(c) 
print(id(d))
print_id_arg(d)
print(id(e))
print_id_arg(e)
#显然结论是，传入函数的东西就是这个对象本身
e.close()

def return_num():
	data = 6
	print(f"The id of data in func:{id(data)}")
	return data

def return_tuple():
	data = (10,)
	print(f"The id of tuple in func:{id(data)}")
	return data

def return_list():
	data = [10]
	print(f"The id of list in func:{id(data)}")
	return data

def return_string():
	data = "str"
	print(f"The id of string in func:{id(data)}")
	return data

def return_file():
	data = open(file_name)
	print(f"The id of file in func:{id(data)}")
	return data

print(id( return_num() ))
print(id( return_tuple() ))
print(id( return_list() ))
print(id( return_string() ))
print(id( return_file() ))
#一毛一样，说明从函数传出的对象就是在函数中构造的对象本身！
