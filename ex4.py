cars = 100#一共100辆车
space_in_a_car = 4#车上的空位
drivers = 30#司机的数量
passengers = 90#乘客的数量
cars_not_driven = cars - drivers #空车的数量
cars_driven = drivers#有司机的车的数量
carpool_capacity = cars_driven * space_in_a_car#车的总容量
average_passengers_per_car = passengers / cars_driven#平均每辆车的乘客数，似乎/这种除法的结果怎么都是浮点数

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport",carpool_capacity,"people today.")
print("We have",passengers,"to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car.")
