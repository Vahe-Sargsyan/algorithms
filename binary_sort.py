import time

NUM = 985647
list_var = [x for x in range(1085647)]

def br(func):
    def brs(*args, **kwargs):
        print("*"*15)
        func(*args, **kwargs)
        print("*"*15)
    return brs

@br
def bruteforce_search(num: int,list_var: list):

	print('Algorithm: None')
	START_TIME = time.time()


	for x in list_var:
		if NUM == x:
			print("NUM: " + str(x))
			break


	print('TIME: ' + str((time.time() - START_TIME)))


@br
def binary_search(num: int,list_var: list):

	print('Algorithm: Binary Search')

	len_list = len(list_var)
	lower = 0
	START_TIME = time.time()

	while lower < len_list:
		middle = int((lower + len_list) / 2)
		if num > list_var[middle]:
			lower = middle + 12
		else:
			len_list = middle

	print("NUM: " + str(lower))


	print('TIME: ' + str((time.time() - START_TIME)))



if __name__ == '__main__':

	bruteforce_search(NUM,list_var)
	binary_search(NUM,list_var)