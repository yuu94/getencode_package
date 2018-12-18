import glob
import csv

# Python3.6 Standard Encodings
# (https://docs.python.org/3.6/library/codecs.html#standard-encodings)
# ascii big5 big5hkscs 
# cp037 cp273 cp424 cp437 cp500 cp720 cp737 cp775cp850 cp852 cp855 cp856
# cp857 cp858 cp860 cp861 cp862 cp863cp864 cp865 cp866 cp869 cp874 cp875
# cp932 cp949 cp950 cp1006 cp1026 cp1125 cp1140 cp1250 cp1251 cp1252 cp1253 
# cp1254 cp1255 cp1256 cp1257 cp1258 cp65001
# euc_jp euc_jis_2004 euc_jisx0213 euc_kr
# gb2312 gbk gb18030 hz iso2022_jp
# iso2022_jp_1 iso2022_jp_2 iso2022_jp_2004 iso2022_jp_3 iso2022_jp_ext iso2022_kr
# latin_1 iso8859_2 iso8859_3 iso8859_4 iso8859_5 iso8859_6 iso8859_7 iso8859_8
# iso8859_9 iso8859_10 iso8859_11 iso8859_13 iso8859_14 iso8859_15 iso8859_16 
# johab koi8_r koi8_t koi8_u kz1048
# mac_cyrillic mac_greek mac_iceland mac_latin2 mac_roman mac_turkish
# ptcp154 shift_jis shift_jis_2004 shift_jisx0213 
# utf_32 utf_32_be utf_32_le utf_16 utf_16_be utf_16_le utf_7 utf_8 utf_8_sig

default = 'ascii euc-jp iso2022-jp iso2022_jp_2 shift_jis utf-8 utf_16_le cp932'

def getEncode(path, encType='default'):
    if encType == 'default':
        encType = default.split(' ')
    else:
        encType = encType.split(' ')

    for enc in encType:
        # print(enc)
        with open(path, encoding=enc) as f:
            try:
                fp = f.read()
            except UnicodeDecodeError:
                continue
        return enc

if __name__ == '__main__':
    # How to use
    # Load file(path:./)
    fileList = glob.glob('./file/*')

    for path in fileList:
        # Use functions
        # Default character code is "ascii euc-jp iso2022-jp iso2022_jp_2 shift_jis utf-8 utf_16_le cp932"
        enc = getEncode(path)
        print(path, 'is Encoding:',enc)

    print()
    print('#####################')
    print()

    for path in fileList:
        # If you want to specify a character code, pass it as an argument to encType
        # Please leave a space between character codes
        origin = 'shift_jis cp932'
        enc = getEncode(path, encType=origin)
        print(path, 'is Encoding:',enc)
