student ={
  "name":"Kasif",
  "age":24,
  "is_adult":True,
  "subject":{
    "chem":97,
    "phy":89,
    "math":90
  }
}
print(student)
print(student["subject"]["math"])
print(student.keys())
print(len(student.keys()))
print(student.values())
print(list(student.keys()))
print(list(student.values()))
pairs = list(student.items()) # here .items deta hai vlue ko pair ke form me as a tupple
print(pairs)
print(pairs[0])
print(student["name"]) # if i write print(student["name2"]) so here ans error
print(student.get("name")) # if i write print(student.get("name")) so here ans is none 
student.update({"city":"Delhi"})
print(student)
