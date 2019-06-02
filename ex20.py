from sys import argv
script, input_file = argv

def print_all(f):
	print( f.read())

def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print( line_count, f.readline())

current_file = open( input_file )

print("让我们先来全部打印一下。")

print_all(current_file)

print("像磁带那样回溯到一个位置。")

rewind(current_file)

print("打印3行")

current_line = 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)

