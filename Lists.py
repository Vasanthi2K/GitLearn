'''
List is one of the complex data types.
Its not like that lists should have same type of data. But the data inside the list can be of any type.
But this is not a very common practice. Usually we keep same type of data in a list.
'''
'''
Accessing elements of list one by one

students_list=["Kirithiv", "Vasanthi", "Navgurukul"]
list_length=len(students_list)
index=0
while index<list_length:
    print(students_list[index])
    index = index+1

'''

'''
Calculating total marks

student_marks=[23,45,49,36,42,39]
length=len(student_marks)
index=0
total_marks=0
while index<len(student_marks):
    total_marks=student_marks[index]+total_marks
    index=index+1
print(total_marks)

'''
'''
lis=[[]]*4
print(lis)
'''

'''
pop() function of lists deletes the element present at index 
list1=[3,2,5,7,3,6]
list1.pop(3)
print(list1)
'''
'''
  1. we use append() function to add an element to the list.
  2. len funciton count the number of elements in the list.
'''
'''
names=['Kirithiv', 'Vasanthi', 'Koka', 'Aurobindo']
print(names[-1][-1])
'''
'''
Counting elemets in a list without using len() function
name=[50,30,10,25,63,45,43]
count=0
for i in name:
    count+=1
print(count)
'''
'''
Counting the occurance of an element in a list
list1=[3,4,5,20,5,25,1,3]
print(list1.count(5))
'''
'''
Reverse order of items
place=["Chennai", "Andhra", "Kerala", "Bangalore"]
print(place.reverse())
'''
'''
Maximum in the list
num=[96,97,99,120,163]
print(max(num))
'''
l=[1,5,9]
print(sum(l), max(l), min(l))