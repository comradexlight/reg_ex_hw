from funcs import order_for_names, normalize_phone_numbers, merge_list
import csv

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

contacts_list = merge_list(normalize_phone_numbers(order_for_names(contacts_list)))

with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)
    print('файл phonebook.csv создан')
