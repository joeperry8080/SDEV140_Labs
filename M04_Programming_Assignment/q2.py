item_list = {'Apple': 0.50, 'Banana': 0.20, 'Mango': 0.99, 
            'Coconut': 2.99, 'Pineapple': 3.99}

sorted_items = sorted(item_list.values())
sorted_items.reverse()

sorted_dict = {}
    
for i in sorted_items:
    for k in item_list.keys():
        if item_list[k] == i:
            sorted_dict[k] = item_list[k]
            break 

for x in list(sorted_dict)[0:3]:
    #print(sorted_dict[x])
    #print ("key {}, value {} ".format(x,  sorted_dict[x]))
    print("{} {} ".format(x, sorted_dict[x]))