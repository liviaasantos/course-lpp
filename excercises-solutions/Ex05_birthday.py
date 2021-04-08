birthday = input('Type your birthday in the formaty DD-MM-YYYY: ')
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
birthday_month = int(birthday[3:5]) - 1
print("You were born in", months[birthday_month])
