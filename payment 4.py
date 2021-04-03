def salary(hour, per_hour) :
    status = True
    if hour > 8 :
        print ('too much work,you should rest')
        status = False
    if per_hour < 10 :
        print ('the payment is too low')
        status = False
    else:
        if status :
            return hour * per_hour
a = 7
b = 15
print (salary(a,b))