import os,platform
os.system('git pull')
# exit(' Wait Tool On updating ')
duffer=platform.architecture()[0]
if duffer=="32bit":__import__("duffer32")
elif duffer=="64bit":__import__("duffer64")
