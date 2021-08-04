from collections import defaultdict
 
my_list = [(1234, 100.23), (345, 10.45), (1234, 75.00),
           (345, 222.66), (678, 300.25), (1234, 35.67)]

for acct_num in my_list:
    print(f"acct_num = {acct_num}")
d = defaultdict(list)
for acct_num, value in my_list:
    print(f"acct_num = {acct_num}, value = {value}")
    d[acct_num].append(value)
 
print(d)


