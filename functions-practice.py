# functions defined
def hello():
  print("Hello, user!")

def pack(a,b,c):
  return [a,b,c]

def eat_lunch(my_lst):
  if len(my_lst) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(my_lst)):
      if i == 0:
        print(f"First I eat {my_lst[0]}")
      else:
        print(f"Next I eat {my_lst[i]}")

# functions called
print(pack('a','b','c'))
print(pack('e','f','g'))
hello()
eat_lunch(['soup','chips','avocado'])