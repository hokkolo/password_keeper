#Password manager
#Author Gautham Sreenivasan
from core import *

if db_exist() is True:
    create_user()
else:
    step1()
    display()


