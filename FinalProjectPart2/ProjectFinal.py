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
            for item in keys:  #craete row
                id = item
                manuf_name = item[item]['manufacturer']
                item_price = item[item]['price']
                service_date = item[item]['service_date']
                item_type = item[item]['item_type']
                damaged_item = item[item]['damaged']
                if types == item_type:  # write the files out
                    file.write('{},{},{},{},{'.format
                            (id, manuf_name, item_price, service_date, damaged_item))

    def past_service(self):
        item = self.item_in_list
        keys = sorted(item.keys(), key=lambda x: datetime(items[x]['service_date']).date(), reverse=True)
        with open('./output_files/PastServiceInventory.csv', 'w') as file:
            for item in keys:
                id=item
                manuf_name = item[item]['manufacturer']
                item_price = item[item]['price']
                service_date = item[item]['service_date']
                item_type = item[item]['item_type']
                damaged_item = item[item]['damaged']
                today = datetime.now().date()
                service_exp = datetime, "m/d/Y").date()
                expired = service_exp < today
                if expired:
                    file.write('{},{},{},{},{},{}\n'.format(id, manuf_name, item_type, item_price, service_date, damaged_item))

    def damaged(self):
        item = self.item_in_list
        keys = sorted(item.keys(), key=lambda x: items[x]['price'], reverse=True)
        with open('./output_files/DamagedInventory.csv', 'w') as file:
            for item in keys:
                id=item
                manuf_name = item[item]['manufacturer']
                item_price = item[item]['price']
                service_date = item[item]['service_date']
                item_type = item[item]['item_type']
                damaged_item = item[item]['damaged']
                if expired:
                    file.write('{},{},{},{},{}\n'.format(id, manuf_name, item_type, item_price, service_date))




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
    inventory.past_service()
    inventory.damaged()

# PART 2
   types = []
   manufacturer = []
   for item in item:
       check_manufacturer = item[item]['manufacturer']
       check_type = item[item]['item_type']
       if check_manufacturer not in types:
           manufacturer.append(check_manufacturer)
       if check_type not in types:
           types.append(check_type)

   user_input = None
   while user_input != 'q':
       if user_input == 'q':
           break
       else:
           manufacturer_selected = None
           type_selected = None
           user_input = user_input.split()
           bad_input = False
           for words in user_input:
               if words in manufacturer:
                   if manufacturer_selected:
                       bad_input=True
                   else:
                       manufacturer_selected = words
               elif words in types:
                   if type_selected:
                       bad_input=True
                   else:
                       type_selected = words
           if not manufacturer_selected  or not type_selected or bad_input:
               print("No such item in inventory")





