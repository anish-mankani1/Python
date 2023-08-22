def days(year,month):
    days_list=[31,28,31,30,31,30,31,30,31,30,31,30]
    if(year%4==0 and month==2):
        return 29
    else:
        return days_list[month-1]# - isliye kyu ki index 0 se chalu hota hai


year=int(input("enter a year"))
month=int(input("enter a month"))
print(days(year,month))
