# def remove_dup (list):
#     newlist=[]
#     for i in list:
#         if i not in newlist:
#             newlist.append(i)
#     return newlist

# my_list = [1,1,2,3,4,41,1,2,4]

# result = remove_dup(my_list)

# print("List without dupe: ", result)

n_list = [1,32,1,4,5]
set1 = set(n_list)
new_list = list(set1)

print(new_list)