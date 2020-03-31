#Password manager
#Author Gautham Sreenivasan
from core import *

if db_exist() is True:
    login()
else:
    step1()
display()


