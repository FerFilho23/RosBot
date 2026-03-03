import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/fernando/Desktop/RosBot/install/rosbot_py_examples'
