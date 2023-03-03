def add_to_list(arr,value):
    arr.append(value)

def insert_into_list(arr,index,value):
    arr.insert(index,value)

def remove_from_list(arr,value):
    if value in arr:
        arr.remove(value)
    else:
        print("value not found")

def update_list(arr,old_value,new_value):
    if old_value in arr:
        arr[arr.index(old_value)] = new_value



my_list = []

add_to_list(my_list,5)
insert_into_list(my_list,0,2)
update_list(my_list,5,3)
remove_from_list(my_list,2)
print(my_list)