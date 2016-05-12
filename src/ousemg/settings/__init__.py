from .base import *
try:
	from .local import *
	live = False
	print('local-settings')
	print(BASE_DIR)
except:
	live = True

if live:
	from .production import *	
	print('live')
