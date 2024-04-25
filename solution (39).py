import datetime
from collections import Counter
from typing import List

def most_common_months(dates: List[str], n) -> List[int]:
    months = [int(date.split('-')[1]) for date in dates]
    month_counter = Counter(months)
    most_common = month_counter.most_common(n) 
    return [month for month, _ in most_common]
    
code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)