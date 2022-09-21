import qrcode

print('The site you want to convert to QR.')
print('Write Stop for exit()')
print()

site = input('Convert to QR: ')

while site != 'Stop':
    img = qrcode.make(site)
    img.save('scan_it.png')
    print('Convert to QR: ', end='')
    site = input()

# comment :
# A file appears in the project bar .png (scan_it.png). Double click and will open QR file.
# if you are going to generate another site in QR just close the open QR and
# double click on the file in the project bar (.png) to open the new QR.

#It doesn't matter how written is http://youtube.com or youtube.com