##--------------------- instant bootup ------------------------------------------------------------------------
## No long waiting anymore at boot up of ht

##--------------------- no warranty by DO7OO ------------------------------------------------------------------
import os,sys,struct
print('Running',os.path.basename(sys.argv[0]),'mod...')

fw =  bytearray(open(sys.argv[1],'rb').read())

if fw[0xD1E6:0xD1E6+4] == b'\xfc\xf7\xa9\xfc':
    print('Set branch to jump over bootup screen')
    fw[0xD1E6:0xD1E6+4] = b'\x00\xf0\x06\xf8'
else:
    print('ERROR: Cant find branch to bootscreen')
    sys.exit(0)

open(sys.argv[1],'wb').write(fw)
