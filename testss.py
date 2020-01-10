
from datetime import datetime
date1 = "2020-02-10 18:09:26.244558"
date2 = "2020-01-10 18:09:26.244558"

date3 = datetime.strftime("2020-01-10 18:09:26.244558","%Y/%m/%d, %H:%M:%S")
print(date3)