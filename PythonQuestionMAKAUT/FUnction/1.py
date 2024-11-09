def emp(li):
    cur_hour=0
    emp_of_month=''
    for emp,hour in li:
        if hour > cur_hour:
            cur_hour=hour
            emp_of_month=emp
        else:
            pass
    return (emp_of_month,cur_hour)

f=[('Roy',100),('Ehs',30),('Modi',800),('Dev',5)]
t,i=emp(f)
print(t)