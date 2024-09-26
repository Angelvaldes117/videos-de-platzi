price = 100 

def increment():
  price = 200
  result = price + 10
  print(result)
  return result

print(price)
price_2 = increment()
print(price_2)
