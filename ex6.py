types_of_people = 10
x = f"There are {types_of_people} types_of_people." #把types_of_people替换进字符串
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."#把binary和do_not变量替换进去

print(x)
print(y)

print(f"I said: {x}")				#把x变量替换进字符串然后输出
print(f"I also said: '{y}'")		#把y变量替换进字符串然后输出

hilarious = False
joke_evaluation = "Isn't that joke so funny?!{}"

print(joke_evaluation.format(hilarious))  #用format函数把hilarious替换到字符串的{}中

w = "This is the left side of..."
e = "a string with a right side."

print( w + e )