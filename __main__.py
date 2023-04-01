import random

pizza_details = []
with open('/Users/sujithrn/Desktop/pizza_list.txt','r') as file_handle:
    lines = file_handle.readlines()
    for line in lines:
        line_without_n = line.strip()
        final_line = line_without_n.split(',')
        pizza_details.append(final_line)
for i in range(len(pizza_details)):
    pizza_details[i].pop()
for i in range(len(pizza_details)):
    for j in range(2,len(pizza_details[0])):
        pizza_details[i][j] = int(float(pizza_details[i][j]))
print('\tPizza_name'+'\t\t Quantity')
print('\r')
for i in range(len(pizza_details)):
    for j in range(1,4,2):
        print(pizza_details[i][j],'\t\t',end = '')
    print('\r')
file_handle.close()

order_id = []
random_number = 0
while random_number not in order_id:
        random_number = random.randint(100000,9999999)
        if random_number not in order_id:
            order_id.append(random_number)
        else:
            pass

def total_income():
    temp_customer_details = []
    income = 0
    with open('/Users/sujithrn/Desktop/desc_list.txt','r') as file_handle:
        customer_list = file_handle.readlines()
        for line in customer_list:
            line_without_n = line.strip()
            final_line = line_without_n.split(',')
            temp_customer_details.append(final_line)
        for i in range(len(temp_customer_details)):
            temp_customer_details[i].pop()
        for i in range(len(temp_customer_details)):
            temp_customer_details[i][1] = float(temp_customer_details[i][1])
        for i in range(len(temp_customer_details)):
            income += temp_customer_details[i][1]
    return round(income,2)

def desc_order():
    temp_customer_details = []
    with open('/Users/sujithrn/Desktop/desc_list.txt','r') as file_handle:
        customer_list = file_handle.readlines()
        for line in customer_list:
            line_without_n = line.strip()
            final_line = line_without_n.split(',')
            temp_customer_details.append(final_line)
        for i in range(len(temp_customer_details)):
            temp_customer_details[i].pop()
        for i in range(len(temp_customer_details)):
            temp_customer_details[i][1] = float(temp_customer_details[i][1])
        temporary_check_list = sorted(temp_customer_details,key = lambda x : x[1],reverse = True)
        print('-------------------------------------------------')
        print('\t\tCustomer Name','\t\tAmount Spent')
        print('-------------------------------------------------')
        for i in range(len(temporary_check_list)-1):
            for j in range(len(temporary_check_list[0])):
                print('\t\t  ',temporary_check_list[i][j],end = '\t  ')
            print('\r')
            print('-------------------------------------------------')
    with open('/Users/sujithrn/Desktop/desc_list.txt','w') as file_handle:
        random_list = ['manager',0]
        for i in range(len(random_list)):
            file_handle.writelines(str(random_list[i])+',')
        file_handle.writelines('\n')

def order_check():
    user_input = input('Do you want to proceed to next order (Y/N) : ')
    if user_input.lower() == 'y':
        customer_information()
    elif user_input.lower() == 'n':
        print()
        report_input = input('Would you like to see the day report (Y/N) : ')
        if report_input.lower() == 'y':
            day_report()
            desc_order()
        elif report_input.lower() == 'n':
            order_check()

def pizza_order(discount,mobile_no):
    global pizza_details
    global random_number
    order_number = 0
    print('Order ID :',order_id[order_number])
    print()
    order_number += 1
    temporary_list = []
    no_of_pizzas = int(input('Enter the number of pizzas to be ordered : '))
    count = 0
    total = 0
    print()
    print('Select the pizza from given below : ')
    while count < no_of_pizzas:
        for i in range(len(pizza_details)):
            print('{} . {}'.format(i+1,pizza_details[i][1]))
        count += 1
        print()
        user_input = int(input('Enter the pizza number {} : '.format(count)))
        print()
        pizza_details[user_input-1][3] -= 1
        total += pizza_details[user_input-1][2]
        if pizza_details[user_input-1][1] not in temporary_list:
            temporary_list.append(pizza_details[user_input-1][1])
            temporary_list.append(1)
            temporary_list.append(pizza_details[user_input-1][2])
        else:
            temporary_index_store = temporary_list.index(pizza_details[user_input-1][1])
            temporary_list[temporary_index_store + 1] += 1
            temporary_list[temporary_index_store + 2] += pizza_details[user_input-1][2]
        total_cost = 0
        temporary_index_store = temporary_list.index(pizza_details[user_input-1][1])
        for i in range(2 , len(temporary_list) , 3):
            total_cost += temporary_list[i]
    print('-------------------------------------------------')
    print('\t\t  Pizza\t\t\t  Quantity\t\tCost')
    print('-------------------------------------------------')
    for i in range(0,len(temporary_list) - 2 , 3):
        print('  ',temporary_list[i],'\t\t',temporary_list[i+1],'\t\t\t',temporary_list[i+2])
        print('-------------------------------------------------')
    print('\t   Total Cost\t\t\t\t\t\t',total_cost)
    print('-------------------------------------------------')
    print('Total Cost after discount\t\t\t\t',total_cost - discount*total_cost)
    print('-------------------------------------------------')
    print()

    with open('/Users/sujithrn/Desktop/pizza_list.txt','w') as file_handle:
        for i in range(len(pizza_details)):
            for j in range(4):
                file_handle.writelines(str(pizza_details[i][j])+str(','))
            file_handle.writelines('\n')
    file_handle.close()

    temp_customer_details = []
    with open('/Users/sujithrn/Desktop/customer_list.txt','r') as file_handle:
        customer_list = file_handle.readlines()
        for line in customer_list:
            line_without_n = line.strip()
            final_line = line_without_n.split(',')
            temp_customer_details.append(final_line)
        for i in range(len(temp_customer_details)):
            temp_customer_details[i].pop()
        for i in range(len(temp_customer_details)):
            temp_customer_details[i][0] = int(float(temp_customer_details[i][0]))
        for i in range(len(temp_customer_details)):
            for j in range(2,len(temp_customer_details[0])):
                temp_customer_details[i][j] = int(float(temp_customer_details[i][j]))
    temp_customer_details_1 = []
    with open('/Users/sujithrn/Desktop/desc_list.txt','r') as file_handle:
        customer_list = file_handle.readlines()
        for line in customer_list:
            line_without_n = line.strip()
            final_line = line_without_n.split(',')
            temp_customer_details_1.append(final_line)
        for i in range(len(temp_customer_details_1)):
            temp_customer_details_1[i].pop()
        for i in range(len(temp_customer_details)):
            if mobile_no == temp_customer_details[i][2]:
                temporary = [temp_customer_details[i][1],total_cost-discount]
                temp_customer_details_1.append(temporary)

    with open('/Users/sujithrn/Desktop/desc_list.txt','w') as file_handle:
        for i in range(len(temp_customer_details_1)):
            for j in range(len(temp_customer_details_1[0])):
                file_handle.writelines(str(temp_customer_details_1[i][j])+',')
            file_handle.writelines('\n')
    order_check()

def discount(mobile_no):
    temp_customer_details = []
    with open('/Users/sujithrn/Desktop/customer_list.txt','r') as file_handle:
        customer_list = file_handle.readlines()
        for line in customer_list:
            line_without_n = line.strip()
            final_line = line_without_n.split(',')
            temp_customer_details.append(final_line)
        for i in range(len(temp_customer_details)):
            temp_customer_details[i].pop()
        for i in range(len(temp_customer_details)):
            temp_customer_details[i][0] = int(float(temp_customer_details[i][0]))
        for i in range(len(temp_customer_details)):
            for j in range(2,len(temp_customer_details[0])):
                temp_customer_details[i][j] = int(float(temp_customer_details[i][j]))
    for i in range(len(temp_customer_details)):
        if mobile_no == temp_customer_details[i][2]:
            count = temp_customer_details[i][3]
            discount_per = count/1000
            return discount_per
    file_handle.close()

def customer_information():
    temporary_mobile_number_list = []
    temporary_random_number_list = []
    print()
    user_input = input('Would you like to order pizzas (Y/N): ')
    if user_input.lower() == 'y':
        customer_details = []
        print()
        customer_name = input('Enter the name of the customer : ')
        print()
        mobile_no = int(input('Enter the mobile number of the customer : '))
        print()
        with open('/Users/sujithrn/Desktop/customer_list.txt','r') as file_handle:
            customer_list = file_handle.readlines()
            for line in customer_list:
                line_without_n = line.strip()
                final_line = line_without_n.split(',')
                customer_details.append(final_line)
            for i in range(len(customer_details)):
                customer_details[i].pop()
            for i in range(len(customer_details)):
                customer_details[i][0] = int(float(customer_details[i][0]))
            for i in range(len(customer_details)):
                for j in range(2,len(customer_details[0])):
                    customer_details[i][j] = int(float(customer_details[i][j]))
        for i in range(len(customer_details)):
            temporary_mobile_number_list.append(customer_details[i][2])
        for i in range(len(customer_details)):
            temporary_random_number_list.append(customer_details[i][0])
        if mobile_no not in temporary_mobile_number_list:
            random_number = 0
            while random_number not in temporary_random_number_list:
                random_number = random.randint(100000,9999999)
                count = 1
                temporary_customer_details = [random_number,customer_name,mobile_no,count]
                temporary_random_number_list.append(random_number)
                customer_details.append(temporary_customer_details)

            with open('/Users/sujithrn/Desktop/customer_list.txt','w') as file_handle:
                for i in range(len(customer_details)):
                    for j in  range(len(customer_details[0])):
                        file_handle.writelines(str(customer_details[i][j])+str(','))
                    file_handle.writelines('\n')
            file_handle.close()
        elif mobile_no in temporary_mobile_number_list:
            temp_customer_details = []
            with open('/Users/sujithrn/Desktop/customer_list.txt','r') as file_handle:
                customer_list = file_handle.readlines()
                for line in customer_list:
                    line_without_n = line.strip()
                    final_line = line_without_n.split(',')
                    temp_customer_details.append(final_line)
                for i in range(len(temp_customer_details)):
                    temp_customer_details[i].pop()
                for i in range(len(temp_customer_details)):
                    temp_customer_details[i][0] = int(float(temp_customer_details[i][0]))
                for i in range(len(temp_customer_details)):
                    for j in range(2,len(temp_customer_details[0])):
                        temp_customer_details[i][j] = int(float(temp_customer_details[i][j]))
                for i in range(len(temp_customer_details)):
                    if temp_customer_details[i][2] == mobile_no:
                        temp_customer_details[i][3] += 1
            file_handle.close()
            with open('/Users/sujithrn/Desktop/customer_list.txt','w') as file_handle:
                for i in range(len(temp_customer_details)):
                    for j in  range(len(temp_customer_details[0])):
                        file_handle.writelines(str(temp_customer_details[i][j])+str(','))
                    file_handle.writelines('\n')
            file_handle.close()
        discount_m = discount(mobile_no)
        pizza_order(discount_m,mobile_no)

def day_report():
    pizza_details = []
    with open('/Users/sujithrn/Desktop/pizza_list.txt','r') as file_handle:
        lines = file_handle.readlines()
    for line in lines:
        line_without_n = line.strip()
        final_line = line_without_n.split(',')
        pizza_details.append(final_line)
    for i in range(len(pizza_details)):
        pizza_details[i].pop()
    for i in range(len(pizza_details)):
        for j in range(2,len(pizza_details[0])):
            pizza_details[i][j] = int(float(pizza_details[i][j]))
    print()
    print('-------------------------------------------------')
    print('\t\t Pizza_name'+'\t\t\t Quantity')
    print('-------------------------------------------------')
    for i in range(len(pizza_details)):
        for j in range(1,4,2):
            print('\t',pizza_details[i][j],'\t\t',end = '')
        print('\r')
    print('-------------------------------------------------')
    print()
    print('-------------------------------------------------')
    print("\tTodays total income\t   ",total_income())
    print('-------------------------------------------------')
    print()
    file_handle.close()
customer_information()
