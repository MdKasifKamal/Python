city = ["mumbai","delhi","patna","hyderabad","kota","muzzaffarpur"]
movies=["iron man", "spider man","sholay","something something","don"]

def print_len(list):
  print(len(list))

print_len(city)
print_len(movies)

def print_list(list):
  for item in list:
    print(item,end="")
print_list(movies)