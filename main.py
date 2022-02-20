def read_customers_file(file):
    list1 = []
    with open(file, "r") as new_file:
        for line in new_file:
            customers = line[12:len(line)]
            list1.append(customers)
    return list1


# this is for the manual option for restaurants in the app
def restaurant_percent(customers, max_cap):
    decimal = customers / max_cap
    percent = decimal * 100
    print(str(percent) + "%")


restaurant_percent(int(input("Current No. of Customers: ")), int(input("Max Capacity: ")))
