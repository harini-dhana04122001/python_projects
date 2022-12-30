from collections import ChainMap

""" ChainMap """
A = {"Pen": 15, "Eraser": 22}
B = {"Marker": 10, "Pen": 20}
C = {"Notebook": 20, "BlackPen": 10}
D = {"Papers": 10, "GraphSheets": 15}
chain = ChainMap(A, B)

print(chain)
print("value of the given key : ", chain["Pen"])
chain.maps.append(C)
print("dictionary after appending : ", chain)
chain2 = chain.new_child(D)
print("dictionary after appending it to front : ", chain2)

""" Iterating over a chainmap dictionary """
for k, v in chain.items():
    print(k, ":", v)
for k, v in reversed(list(chain.items())):
    print(k, ":", v)

""" Deleting A Item in chainmap """
del chain["Pen"]
print(A)    # deleting a key from chain map affects actual dictionary as chain map only stores reference
print(chain)

""" Use Case problem for chainmap """
fruits_prices = {"apple": 100, "grape": 90, "orange": 120}
veggies_prices = {"tomato": 60, "bellpepper": 80, "onion": 100}
prices = ChainMap(fruits_prices, veggies_prices)

order = {"apple": 4, "tomato": 8, "orange": 4}

for product, units in order.items():
    price = prices[product]
    subtotal = units * price
    print(f"{product:8}:  {price} Rs x {units} = {subtotal} Rs")

