def my_func(variable,*args):
    list = []
    for arg in str(args):
        if arg % 2 == 0:
            list.append(char.upper())
        else:
            list.append(char.lower())
        return list


print (my_func("hello"))
        
