def this_fals():
    x = 1/0

try:
    this_fals()

except ZeroDivisionError as err:
    print ("Handling run-time error : ", err)