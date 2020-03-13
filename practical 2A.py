#python program to show iterables,itertors and itertry
#python program to show iterator

print("----------ITERATORS------------")
lst1=["Mumbai","Pune","Delhi","Patna"]

iterator_obj=iter(lst1)
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))

#python program to show iterator
lst1=["Mumbai","Pune","Delhi","Patna"]
for city in lst1:
                print(city)
print("\n")

lst2=["Python","Pearl","C","C++","Java"]
for lang in lst2:
                print(lang)
print("\n")

for s in "Iteration is easy":
                print(s,end=" ")

#python program to show iteratry
def iterable(obj):
                try:
                                iter(obj)
                                return True
                except TypeError:
                                return False
for element in[34,[4,5],(4,5),{"a":4},"abcd",4.5]:
                print(element ,"is iterable:",iterable(element))






