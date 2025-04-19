'''Time scheduled downloads sorting'''
import os
import shutil
import datetime

while 1:

    TODAY = datetime.datetime.today()
    TODAY = str(TODAY)
    CHOUR = TODAY[11:13]
    CMIN = TODAY[14:16]
    CSEC = TODAY[17:19]

    if CHOUR == '10' and CMIN == '00' and CSEC == '00':
        os.chdir("/home/---/Downloads")
        files = os.listdir(os.getcwd())

        for filename in files:
            if not os.path.isdir(filename):
                # mp3
                if '.mp3' in filename:
                    if not os.path.exists('Music'):
                        os.mkdir('Music')
                    shutil.move(filename, 'Music')
                # jpg/png
                elif '.jpg' in filename or '.png' in filename:
                    if not os.path.exists('Images'):
                        os.mkdir('Images')
                    shutil.move(filename, 'Images')
                # pdf
                elif '.pdf' in filename:
                    if not os.path.exists('pdf'):
                        os.mkdir('pdf')
                    shutil.move(filename, 'pdf')
