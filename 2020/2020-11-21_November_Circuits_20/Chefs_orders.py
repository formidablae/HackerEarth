file_handler = open("input_chefs_orders.txt", 'r')
N_customers, K_chefs = map(int, file_handler.readline().strip().split())
A_customers_arrival_times = list(map(int, file_handler.readline().strip().split()))
B_times_to_perpare_order = list(map(int, file_handler.readline().strip().split()))
C_anger_for_wait = list(map(int, file_handler.readline().strip().split()))
D_chefs_contract_times = list(map(int, file_handler.readline().strip().split()))
file_handler.close()

# N_customers, K_chefs = map(int, input().split())
# A_customers_arrival_times = list(map(int, input().split()))
# B_times_to_perpare_order = list(map(int, input().split()))
# C_anger_for_wait = list(map(int, input().split()))
# D_chefs_contract_times = list(map(int, input().split()))

chefs_still_working = [True] * K_chefs
D_free = [0] * K_chefs
D_worked_time = [0] * K_chefs
A_customers_in_wait_list = []
time = 0
# assigned_orders_to_chefs = {}
output = {}
done_orders = 0
customes_to_do = list(range(N_customers))
print("Time at the moment {}\n"
          "Orders started now {}\n"
          "Chefs occupied for {}\n"
          "Chefs still workin {}\n"
          "Chefs worked for t {}\n"
          "Chefs who are free {}\n"
          "Orders in waitlist {}\n"
          # "Orders assigned as {}\n"
          "Customers yet todo {}\n"
          "Output for now is: {}\n".format(time,
                                           done_orders,
                                           D_free,
                                           chefs_still_working,
                                           D_worked_time,
                                           0,
                                           A_customers_in_wait_list,
                                           # assigned_orders_to_chefs,
                                           customes_to_do,
                                           output))
while len(customes_to_do) > 0:
    time += 1
    free_chefs = 0
    for k in range(K_chefs):
        if D_free[k] > 0:
            D_free[k] -= 1
            D_worked_time[k] += 1
        if D_chefs_contract_times[k] == D_worked_time[k]:
            chefs_still_working[k] = False
        if D_free[k] == 0 and chefs_still_working[k]:
            free_chefs += 1
    if len(A_customers_in_wait_list) != 0:
        i = 0
        while i < len(A_customers_in_wait_list):
            m = 0
            if free_chefs > 0:
                list_of_ranges = list(range(m, K_chefs))
                for n in list_of_ranges:
                    m += 1
                    if D_free[n] == 0 and chefs_still_working[n]:
                        # assigned_orders_to_chefs[A_customers_in_wait_list[i]] = n
                        output[A_customers_in_wait_list[i]] = [time, n]
                        D_free[n] = B_times_to_perpare_order[A_customers_in_wait_list[i]]
                        done_orders += 1
                        free_chefs -= 1
                        customes_to_do.remove(A_customers_in_wait_list[i])
                        A_customers_in_wait_list.pop(i)
                        i -= 1
                        break
            i += 1
    elements_to_remove = []
    for i in customes_to_do:
        if time == A_customers_arrival_times[i]:
            if free_chefs > 0:
                for j in range(K_chefs):
                    if D_free[j] == 0 and chefs_still_working[j]:
                        # assigned_orders_to_chefs[i] = j
                        output[i] = [time, j]
                        D_free[j] = B_times_to_perpare_order[i]
                        elements_to_remove.append(i)
                        done_orders += 1
                        free_chefs -= 1
                        break
            else:
                A_customers_in_wait_list.append(i)
    for elem in elements_to_remove:
        customes_to_do.remove(elem)
    print("Time at the moment {}\n"
          "Orders started now {}\n"
          "Chefs occupied for {}\n"
          "Chefs still workin {}\n"
          "Chefs worked for t {}\n"
          "Chefs who are free {}\n"
          "Orders in waitlist {}\n"
          # "Orders assigned as {}\n"
          "Customers yet todo {}\n"
          "Output for now is: {}\n".format(time,
                                           done_orders,
                                           D_free,
                                           chefs_still_working,
                                           D_worked_time,
                                           free_chefs,
                                           A_customers_in_wait_list,
                                           # assigned_orders_to_chefs,
                                           customes_to_do,
                                           output))
for value in output.values():
    print(value[0], value[1] + 1)