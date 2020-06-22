#Write a Python program to remove duplicates from sorted list.

test_list = [1, 3, 7, 4, 8, 2, 3, 1]
print ("The original list is : " + str(test_list))

res = []
for i in test_list:
	if i not in res:
		res.append(i)

print ("The list after removing duplicates : " + str(res))
