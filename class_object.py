class Time():
    def __init__(self,hours,minutes):
        self.hours=hours
        self.minutes=minutes
    def print_time(self):
        s = "After the operation total time is: {0} hour {1:02d} minutes"
        print(s.format(self.hours, self.minutes))
    def add_time(time1,time2):
        h=time1.hours+time2.hours
        m=time1.minutes+time2.minutes
        sum_time=Time(h,m)
        if sum_time.minutes >= 60:
            sum_time.minutes = sum_time.minutes - 60
            sum_time.hours = sum_time.hours + 1
        return sum_time
    def substract_time(time1,time2):
        h = time1.hours-time2.hours
        m = time1.minutes-time2.minutes
        sub_time = Time(h, m)
        return sub_time
    def total_min(time1,time2):
        m= time1.hours*60+time2.hours*60+ time1.minutes+time2.minutes
        addition_time = Time(0,m)
        return addition_time
t1=Time(5,50)
t2=Time(2,15)
done_time=Time.add_time(t1,t2)
new_time=Time.substract_time(t1,t2)
time_in_min=Time.total_min(t1,t2)
Time.print_time(done_time)
Time.print_time(new_time)
Time.print_time(time_in_min)