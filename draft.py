#from dateutil import parser
#d = parser.parse('01/01/25 12:10:03.234567') 
#print(d) 

from datetime import datetime
dam = '01/01/25'
d = datetime.strptime(dam, '%d/%m/%y')
print(d)