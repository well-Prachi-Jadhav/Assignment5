Original=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list: ",Original)
ext=[]
for i in Original:
    if i<6:
        ext.append(i)
print("Extracted first five elements: ",ext)
ext2=[]
for i in reversed(ext):
        ext2.append(i)
print("Reversed extracted elements: ",ext2)
