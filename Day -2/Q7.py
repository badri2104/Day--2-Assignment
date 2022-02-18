month_num = int(input("Input the number(1-12): "))
dict_month = {1:"January",2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}

if month_num in (1,3,5,7,8,10,12):
  if dict_month[month_num] == "January":
    print("Month is",dict_month[month_num])
  elif dict_month[month_num] == "March":
    print("Month is",dict_month[month_num])
  elif dict_month[month_num] == "May":
    print("Month is",dict_month[month_num])
  elif dict_month[month_num] == "July":
    print("Month is",dict_month[month_num])
  elif dict_month[month_num] == "August":
    print("Month is",dict_month[month_num])
  elif dict_month[month_num] == "October":
    print("Month is",dict_month[month_num])
  elif dict_month[month_num] == "December":
    print("Month is",dict_month[month_num])
  print("No. of days: 31 day")

elif month_num in (4,6,9,11):
  if dict_month[month_num] == "April":
    print("Month is",dict_month[month_num])
  elif dict_month[month_num] == "June":
    print("Month is",dict_month[month_num])
  elif dict_month[month_num] == "September":
    print("Month is",dict_month[month_num])
  elif dict_month[month_num] == "November":
    print("Month is",dict_month[month_num])
  print("No. of days: 30 day")


else:
  print("Month is",dict_month[month_num])
  print("No. of days: 28/29 days")
