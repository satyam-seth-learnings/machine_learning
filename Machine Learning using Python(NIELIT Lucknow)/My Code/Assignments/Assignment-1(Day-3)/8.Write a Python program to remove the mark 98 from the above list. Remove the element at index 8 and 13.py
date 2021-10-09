# Write a Python program to remove the mark 98 from the above list. Remove the element at index 8 and 13

marks=[78,87,89,98,67,65,45,56,77,89]
print(f'Marks: {marks}')
marks.remove(98)
marks.pop(8)
print(f'Marks: {marks}')
# marks.pop(13)