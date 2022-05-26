import os
import shutil
import datetime

while 1:

	today = datetime.datetime.today()
	today = str(today)
	chour = today[11:13]
	cmin = today[14:16]
	csec = today[17:19]

	if chour == '10' and cmin == '00' and csec == '00':
		os.chdir("/home/---/Downloads")
		files = os.listdir(os.getcwd())

		for filename in files:
			if not os.path.isdir(filename):
				#mp3
				if '.mp3' in filename:
					if not os.path.exists('Music'):
						os.mkdir('Music')
					shutil.move(filename, 'Music')
				#jpg/png
				elif '.jpg' in filename or '.png' in filename:
					if not os.path.exists('Images'):
						os.mkdir('Images')
					shutil.move(filename, 'Images')
				#pdf
				elif '.pdf' in filname:
					if not os.path.exists('pdf'):
						os.mkdir('pdf')
					shutil.move(filename, 'pdf')
				