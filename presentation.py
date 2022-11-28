# List comprehension
squares = [i * i for i in range(10)]
print(squares)

# comprehension with if else
multiply_number = [i * 2 if i % 2 == 0 else i * 2 for i in range(10)]
print(multiply_number)

# comprehension with if else
tax_list = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08


def get_price_with_tax(tax):
    return tax * (1 + TAX_RATE)


final_prices = [get_price_with_tax(i) for i in tax_list if i < 4.00]
print(final_prices)


# nested list comprehension
l = [['40', '20', '10', '30'], ['20', '20', '20', '20', '20', '30', '20'],
     ['30', '20', '30', '50', '10', '30', '20', '20', '20']]
new_list = [[int(y) for y in x] for x in l]
print(new_list)

# dictionary comprehension
old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}

price = 0.76
new_price = {item: value*price for (item, value) in old_price.items()}
print(new_price)


# example for id
list_one = ['apple', 'banana', 'sugarcane']
list_two = ['apple', 'banana', 'sugarcane']

print(id(list_one))
id_of_list_element = [id(i) for i in list_two]
print(id_of_list_element)
equal_two_list = [True for i in list_one for j in list_two if id(i) == id(j)]
print(equal_two_list)

# example for type
list_one = ['apple', 'banana', 'sugarcane']
list_two = ['apple', 'banana', 'sugarcane']

print(type(list_one))
equal_two_lists = [True for i in list_one if type(list_one) == type(list_two)]
print(equal_two_list)

