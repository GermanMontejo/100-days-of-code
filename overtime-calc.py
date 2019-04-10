from datetime import datetime
from datetime import timedelta
import os

ot_hours_list = []

while True:

	print('Press 1 to calculate the number of hours you rendered for your OT.')
	print('Press 2 to get your total number of OT hours.')
	print('Press 3 to quit this program.')
	selection = int(input(''))
	

	if selection == 1:
		
		try:
			ot_dt_start = input('Enter the datetime from which you started your OT, i.e. 04/10/2019 19:00: ')
			ot_dt_st = datetime.strptime(ot_dt_start,'%d/%m/%Y %H:%M' )
			
			ot_dt_end = input('Enter the datetime from which you ended your OT, i.e. 04/10/2019 21:00: ')
			ot_dt_en = datetime.strptime(ot_dt_end, '%d/%m/%Y %H:%M')

			ot_hours = ot_dt_en - ot_dt_st
			ot_hours_list.append(ot_hours)
			os.system('clear')
			print('You have rendered {} hour(s)'.format(ot_hours))
		except Exception:
			os.system('clear')
			print('Invalid format. Please check the datetime you inputted.')

	elif selection == 2:
		total_hours = timedelta(hours=0)
		for dt in ot_hours_list:
			total_hours += dt
		os.system('clear')
		print('total hours rendered: {}'.format(total_hours))
	elif selection == 3:
		os.system('clear')
		break
	else:
		os.system('clear')
		print('Invalid selection.')