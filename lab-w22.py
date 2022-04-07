#convert these objects!

#1
start_list = [[2, 3, 4], [6, 8, 9]]
#turn it into [1,    2,   3, 4   ]
x, y = start_list
new_list = x+y
print(new_list)
final_list = [int(i/2) for i in new_list if (i % 2) == 0]
print(final_list)

#Solution
[item for sublist in start_list for item in sublist if item % 2 == 0]


#2
import datetime
start_dict = {'noah': '2/23/1999',
              'sarah':'9/1/2001',
              'zach': '8/8/2005'}
#turn it into {'Noah': datetime(1999, 2, 23),
#              'Sarah':datetime(2001, 9, 1),
#              'Zach': datetime(2005, 8, 8)}

final_dict = {Key.capitalize(): datetime.datetime.strptime(Val, "%m/%d/%Y").date() for Key, Val in start_dict.items()}
print(final_dict)








date1 = datetime.datetime.strptime('2/23/1999', "%m/%d/%Y")
print(date1)
datetime.datetime.date(date1)

final_dict = {for Key.capitalize(), Val in start_dict.items()}
    print("Key", Key)
    print("Val", Val)
    
akj = "about"
akj.capitalize()
