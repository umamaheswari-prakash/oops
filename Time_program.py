class Time():
    def __init__(self,hours,minutes):
        self.hours=hours
        self.minutes=minutes
    def print_time(self):
        s = "After the operation total time is: {0} hour {1:02d} minutes"
        print(s.format(self.hours, self.minutes))
    def total_min(time1,time2):
        m= time1.hours*60+time2.hours*60+ time1.minutes+time2.minutes
        addition_time = Time(0,m)
        return addition_time
def add_time(time1,time2):
    h=time1.hours+time2.hours
    m=time1.minutes+time2.minutes
    if m >= 60:
        m = m - 60
        h = h + 1
    s=Time(h,m)
    Time.print_time(s)
def substract_time(t1,t2):
    h = t1.hours-t2.hours
    m = t1.minutes-t2.minutes
    if m < 0:
      m = 60+ m
      h = h - 1
    p=Time(h,m)
    Time.print_time(p)

t1=Time(5,10)
t2=Time(2,55)
add_time(t1,t2)
substract_time(t1,t2)
time_in_min=Time.total_min(t1,t2)
Time.print_time(time_in_min)