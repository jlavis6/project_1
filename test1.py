#import camelot
import os

BASE_PATH = "C:\\Users\jlavi\OneDrive - IPADE Business School\\"

a = os.path.join(BASE_PATH, "To invest or not to.pdf")

b = os.path.isfile(a)

print(b)
print()

#pdf = camelot.read_pdf('To invest or not to.pdf')
