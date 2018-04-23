import json
with open("hotel_info.json",'r') as f:
    hotel_list=json.load(f)
print(hotel_list)
print(type(hotel_list))
print(len(hotel_list))
for x in hotel_list:
    print(type(x))
    print(x['hotel_name'])
    print(x['hotel_address'])
    print(x["hotel_phone"])

