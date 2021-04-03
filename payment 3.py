def salary(hour, per_hour) :
    a = True
    if hour > 8 :
        print ('too much work,you should rest')
        a = False
    if per_hour < 10 :
        print ('the payment is too low')
    else:
        payment = hour * per_hour
        if a == True :
            return payment
a = 5
b = 2
print (salary(a,b))