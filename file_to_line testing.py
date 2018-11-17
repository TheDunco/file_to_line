
from file_to_line.file_to_line import *

# Say goodbye to this code if you run this...
with open('file_to_line testing.py', 'w') as file:
    file.write('''{}'''.format(str(file_to_line('file_to_line.py'))))
