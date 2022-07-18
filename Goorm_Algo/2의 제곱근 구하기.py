# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = int(input())
binary_input = format(user_input, 'b')
binary_list = [i for i in str(binary_input)]

if binary_list.count('1') == 1:
	print('Yes')
else :
	print('No')