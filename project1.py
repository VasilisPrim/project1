import datetime
day, month, year = input("Date: ").split("/")
day = int(day)
month = int(month)
year = int(year)
discount = float(input("Day discount: "))
tickets = 0
proceeds = 0
sum_vat = 0
sum_age = 0
max_age = 0
count = 0
min_age = -1
while True:
    hours, minutes = input("Time: ").split(":")
    b_day, b_month, b_year = input("DOB: ").split("/")
    b_day = int(b_day)
    b_month = int(b_month)
    b_year = int(b_year)
    today = datetime.date(year, month, day)
    birthdate = datetime.date(b_year, b_month, b_day)
    difference = today - birthdate
    day_difference = difference.days
    age = int(day_difference // 365.25)
    print("Age:",age)
    print("##")
    if age <= 17:
        base_price = 12.50
    elif age <= 74:
        base_price = 24.00
    else:
        base_price = 17.25
    print("Base price: %.2f" % base_price)
    sum_age += age
    
    if age > max_age:
        max_age = age
    
    if age < min_age or min_age == -1:
        min_age = age
        
    
    if age < 18:
        count += 1
    hours = int(hours)
    minutes = int(minutes)
    final_price = base_price - (base_price * discount) / 100
    if hours < 10 or (hours == 10 and minutes < 30) or (hours >= 17 and minutes > 0):
        proceeds += final_price
        vat_2 = final_price - final_price / 1.24
        sum_vat += vat_2
        if (hours < 10) or (hours == 10 and minutes < 30):
            print("Discount applies: EARLY ADM")
        else:
            print("Discount applies: LATE ADM")

        print("Final price: %.2f" % final_price)
        print("##")

    if (hours > 10 and hours < 17) or (hours == 17 and minutes == 0) or (hours == 10 and minutes >= 30):

        print("Discount applies: NONE")
        print("Final price: %.2f" % base_price)
        proceeds += base_price
        vat_1 = base_price - base_price/1.24
        sum_vat += vat_1
        print("##")
    y_n = input("More (y/n)? ")
    tickets += 1
    if y_n == "n":
        break

print("Tickets sold:",tickets)
print("Proceeds: %.2f" % proceeds)
print("VAT: %.2f" % sum_vat)
print("##")
avg_age = sum_age/tickets
under_18 = (count/tickets)*100
print("Max age:",max_age)
print("Min age:",min_age)
print("Avg age:",round(avg_age))
print("Under18: %.2f"%(under_18)+"%")

