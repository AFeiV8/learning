'''
驻留机制：相同的字符串只保留一份
驻留机制的几种情况：字符串长度为0或1；符合标识符的字符串，
                 [-5,256]之间的整数；编译时驻留，运行时不驻留
多个字符串相加时，建议使用.join()
'''