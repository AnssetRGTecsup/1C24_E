import sys

def ShowSizeOf(struct, nameVar):
    print(f'Size of {nameVar}: {sys.getsizeof(struct)}')

n_numero = str()
a_list = list()
a_tuple = tuple()

a_list = [1,2,3,4,5, "a"]
a_tuple = (1,2,3,4,5, "a")

#ShowSizeOf(n_numero, "n_numero")

ShowSizeOf(a_list, "a_list")
ShowSizeOf(a_tuple, "a_tuple")

print("2nd test")

a_list2 = [1,2,3,4,5, "a", "b"]
a_tuple2 = (1,2,3,4,5, "a", "b")

ShowSizeOf(a_list2, "a_list2")
ShowSizeOf(a_tuple2, "a_tuple2")