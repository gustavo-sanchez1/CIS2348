# Gustavo Sanchez PSID#1861118

import csv

class OutputInventory:  # class to output inventory
    def __init__(self, item_in_list):  # define
        self.item_in_list = item_in_list
    def fullin(self):  # full inventory
        with open('FullInventory.csv', 'w'):  # open file
            item = self.item_in_list
            keys = sorted(item.keys(), key=lambda x: item[x]['manufacturer'])  # use lambda
            for item in keys:  # create row
                id = item
                manuf_name = item[item]['manufacturer']
                item_type = item[item]['item_type']
                item_price = item[item]['price']
                service_date = item[item]['service_date']
                damaged_item = item[item]['damaged']
                file.write('{},{},{},{},{},{}'.format
                           (id, manuf_name, item_type, item_price, service_date, damaged_item))

    def type(self):  # define type
        item = self.item_in_list
        types = []
        keys = sorted(item.keys())
        for item in item:
            item_type = item[item]['item_type']
            if item_type != types:
                types.append(item_type)

        with open('LaptopInventory.csv', 'w') as file:  # open file
            for item in key:  #craete row
                id = item
                manuf_name = item[item]['manufacturer']
                item_price = item[item]['price']
                service_date = item[item]['service_date']
                item_type = item[item]['item_type']
                damaged_item = item[item]['damaged']
                if types == item_type:  # write the files out
                    file.write('{},{},{},{},{'.format
                            (id, manuf_name, item_price, service_date, damaged_item))





if __name__=='__main__':  # main code
    item = {}
    files_names = ['ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv']  # dictionary
    for file in files_names:
        with open(file, 'r') as csv_file:  # open file and read
            csv_reader = csv_reader(csv_file, delimeter=',')
            for line in csv_reader:
                id_item = line[0]
                if file == files_names[0]:  #rows
                    item[id_item] = {}
                    manuf_name = line[1]
                    item_type = line[2]
                    damaged_item = line[3]
                    item[id_item]['manufacturer'] = manuf_name.strip()  #strip them
                    item[id_item]['item_type'] = item_type.strip()
                    item[id_item]['damaged'] = manuf_name.strip()

    inventory = OutputInventory(item)
    inventory.fullin()
    inventory.type()

