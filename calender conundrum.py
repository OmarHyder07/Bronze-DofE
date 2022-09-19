def number_seperator(mayan_date): #seperates the inputed mayan date into different numbers in a list
    numberlist = []
    number = ""
    for i in mayan_date:
        if i != " ":
            number = number + i 
        elif i == " ":
            numberlist.append(number)
            number = ""
    numberlist.append(number) 
    return numberlist  

def day_count(m_list): #finds the total amount of days (kins) in the maya date
    gregorian_days = 0
    mayan_days = [144000, 7200, 360, 20]
    for x in range(4):
        gregorian_days = gregorian_days + int(m_list[x]) * mayan_days[x]
    gregorian_days = gregorian_days + int(m_list[4])
    return gregorian_days


print("This translator uses the range of dates: 12 19 6 15 2 <---> 14 1 15 12 3") 
print("Please input the date with one space between each number.") 
mayan_date = input("Input your mayan date to be translated to a gregorian date. ")
days = day_count(number_seperator(mayan_date))

days = days - 1867262
year = 2000
month = 0
day = 1

while days >= 31: #goes through each month.
    if days >= 31:
        days = days - 31 #to get rid of the total days count, so the loop stops. 
        month = month + 1 #cycles between the months. 
    if year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0):
        if days >= 29:
            days = days - 29
            month = month + 1
    else:
        if days >= 28:
            days = days - 28
            month = month + 1
    if days >= 31: 
        days = days - 31
        month = month + 1
    if days >= 30:
        days = days - 30
        month = month + 1
    if days >= 31:
        days = days - 31
        month = month + 1
    if days >= 30:
        days = days - 30
        month = month + 1
    if days >= 31:
        days = days - 31
        month = month + 1
    if days >= 31:
        days = days - 31
        month = month + 1
    if days >= 30:
        days = days - 30
        month = month + 1
    if days >= 31:
        days = days - 31
        month = month + 1
    if days >= 30:
        days = days - 30
        month = month + 1
    if days >= 31:
        days = days - 31
        month = 0 #restarts the months 
        year = year + 1 #adds a new year 

day = day + days #when the total days isn't >= to the month day count, that means the total days is the gregorian date. 
        
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print("The date is: " + str(day) + " " + months[month] + " " + str(year)) 
