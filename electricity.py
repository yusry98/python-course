consumer_id = input('Enter consumer ID')
consumer_name = input('Enter consumer name')
consumer_type = 'Home'
consumer_add = input('Enter consumer address')
current_reading = int(input('Enter current reading'))
previous_reading = int(input('Enter previous reading'))
total_reading = current_reading - previous_reading
first_tariff_perunit = 0.2180
second_tariff_perunit = 0.3340
third_tariff_perunit = 0.5160

print('Consumer ID: ', consumer_id)
print('Consumer Name: ', consumer_name)
print('Consumer Type: ', consumer_type)
print('Consumer Address: ', consumer_add)
print('Current Reading: ', current_reading)
print('Previous Reading: ', previous_reading)
print('Total Reading:', total_reading)

if 1 <= total_reading <= 200:
    amount = round(total_reading * first_tariff_perunit, 2)
    print('Total amount: RM', amount)
elif 201 <= total_reading <= 300:
    amount = round((total_reading - 200) * second_tariff_perunit + 43.60, 2)
    print('Total amount: RM', amount)
elif 301 <= total_reading <= 600:
    amount = round((total_reading - 300) * third_tariff_perunit + 43.60 + 33.40, 2)
    print('Total amount: RM', amount)








