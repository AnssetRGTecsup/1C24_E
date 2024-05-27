import sys

def ShowSizeOf(struct, nameVar):
    print(f'Size of {nameVar}: {sys.getsizeof(struct)}')

a_list = list()
a_tuple = tuple()

a_list = [1,2,3,4,5, "alumno_1", "alumno_1"]
a_tuple = (1,2,3,4,5, "alumno_1", "alumno_1")

ShowSizeOf(a_list, "a_list")
ShowSizeOf(a_tuple, "a_tuple")