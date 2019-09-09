''' name = input('введите имя')

print(f'привет {name}') '''

#v =  int (input('введите число от 1 до 10'))
#print(v + 10)

#b = bool('0')
# print(b)

'''random_list =[3,5,7,9,10.5]
print(random_list)
random_list.append('python')
print(random_list)
#print(random_list[1:4])
#print(len(random_list))
del random_list[-1]
print(random_list )'''

'''
new_dict = {
    "city":"Москва",
    "temperature":"20"
    }
print(new_dict)
print(new_dict["temperature"])
#new_dict[2]["temperature"] = int(new_dict[2]["temperature"]) - 5
#print(new_dict["temperature"])
#print(new_dict)
 new_dict["country"] = "Россия"
new_dict["date"] = "27.05.2019"
print(new_dict)
print(len(new_dict))
'''
'''
x = 0
while x < 10:
    print(x) 
    x += 1
'''
'''
price = 100
discount = 5
price_with_discount = price - price * discount / 100
print(price_with_ discount)
'''
'''
def get_summ(one, two, delimeter = '&'):
    a = str(one)
    b = str(two)
    sum_result = (a + '&' + b)
    print(sum_result)
    return sum_result

one = 'learn'
two = 'python'
get_summ(one, two)
'''

def format_price(price):
    a = int(price)
    b = str(a)
    print(b + " руб")


price = 56.24
format_price(price)

