#how to use list
new_list_1 = []
print(new_list_1)
new_list_2 = []
print(new_list_1)

#use of append function
new_list_1.append('hello')
print("new_list_1 : ")
print(new_list_1)

new_list_2.append(1)
new_list_2.append(2)
new_list_2.append(3)
print("new_list_2 : ")
print(new_list_2)

print("---------------------------------------------------")
print(new_list_1)
print(new_list_2)
new_list_1.extend(new_list_2)
print("extend function in list : " + str(new_list_1))
print("---------------------------------------------------")

#how to use dictionary data type
#key 와 value을 활용하는 dictionary
country_code = {1:'America', 2:'Italia', 3:"China"}
print("contry_code : " + str((country_code)))
print("len of contry_code : " + str(len(country_code)))
print(country_code[2]) # index값 대신에 key값을 활용하여 접근 가능

new_dict= {} #비어있는 딕셔너리 생성
new_dict[1] = "chicken" # elements 추가
new_dict[2] = "pizza"
print(new_dict)
print("---------------------------------------------------")

#튜플은 생성하고 나면 변경할 수 없다. 리스트 생성에 활용할 수 있다.
new_tuple = (1,2,3)
print(new_tuple)
list_1 = list(new_tuple)
print('list_1 : ' + str(list_1))
list_1.append(10)
print('list_1 : ' + str(list_1))

print("---------------------------------------------------")
list_for_loop = ['a', 'b', 'c', 1, 2]
for i in range(10):
    if(i %3 == 0):
        print('%03d'%i)
    else:
        print(i)

for j in list_for_loop: #리스트에 있는 elements들이 j에 들어간다.
    print(type(j))
print("---------------------------------------------------")

#클래스 활용 익숙해지기

class lab():
    def __init__(self, name):
        self.num_of_member = 12
        self.name_of_lab = name
    def print_nameOfLab(self):
        print(self.name_of_lab)
    def add_member(self):
        self.num_of_member += 1

MI = lab('Machine Intelligence')
print(MI.num_of_member)
MI.add_member()
print(MI.num_of_member)
MI.add_member()
print(MI.num_of_member)
MI.print_nameOfLab()
print("---------------------------------------------------")