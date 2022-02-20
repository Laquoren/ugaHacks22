def read_customers_file(file):
    list1 = []
    with open(file, "r") as new_file:
        for line in new_file:
            customers = line[12:len(line)]
            list1.append(customers)
    return list1
# This is the beginning of the file system for the survailence system. 
# In the final product, this will be followed by a string to int list conversion function, 
# then a functon that changes the numbers in the list into objects using the Restaurant class in the Class.py file, 
# then a function like the one below will do the precent work using the objects 


# this is for the manual option for restaurants in the app
def restaurant_percent(customers, max_cap):
    decimal = customers / max_cap
    percent = decimal * 100
    print(str(percent) + "%")


restaurant_percent(int(input("Current No. of Customers: ")), int(input("Max Capacity: ")))
