import datetime

date_time_str = 'Tue, Mar 01, 2016'
date_time_obj = datetime.datetime.strptime(date_time_str, '%a, %b %d, %Y')
print(date_time_obj)