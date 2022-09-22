item_list = {'Apple': 0.50, 'Banana': 0.20, 'Mango': 0.99, 
            'Coconut': 2.99, 'Pineapple': 3.99}

sorted_dict = {}

sorted_items = sorted(item_list.items(),key=lambda kv:(kv[1], kv[0]))
    
for i in sorted_items:
    print(i[0], i[1])