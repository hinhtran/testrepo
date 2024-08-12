items = [x for x in input("Nhap mot chuoi: ").split(',')]
items.sort()
print(items)
print(','.join(items))