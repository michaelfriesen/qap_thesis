import os
import re

for p in range(1,9):
    for v in range(0,10):
        for n in range(5,15,5):
            file = 'ori-n''%s''p''%s''v''%s''.lp' % (n, p, v)
            open_file = open(file,'r')
            read_file = open_file.read()
            regex = re.compile(r'\[(\d+)\,(\d+)\]')
            read_file = regex.sub(r'(\1,\2)', read_file)
            write_file = open(file,'w')
            write_file.write(read_file)

            file = 'dia-n''%s''p''%s''v''%s''.lp' % (n, p, v)
            open_file = open(file,'r')
            read_file = open_file.read()
            read_file = regex.sub(r'\1\2', read_file)
            write_file = open(file,'w')
            write_file.write(read_file)

            file = 'lin-n''%s''p''%s''v''%s''.lp' % (n, p, v)
            open_file = open(file,'r')
            read_file = open_file.read()
            read_file = regex.sub(r'\1\2', read_file)
            write_file = open(file,'w')
            write_file.write(read_file)

            file = 'pos-n''%s''p''%s''v''%s''.lp' % (n, p, v)
            open_file = open(file,'r')
            read_file = open_file.read()
            read_file = regex.sub(r'\1\2', read_file)
            write_file = open(file,'w')
            write_file.write(read_file)                    

            file = 'neg-n''%s''p''%s''v''%s''.lp' % (n, p, v)
            open_file = open(file,'r')
            read_file = open_file.read()
            read_file = regex.sub(r'\1\2', read_file)
            write_file = open(file,'w')
            write_file.write(read_file)             

            file = 'tri-n''%s''p''%s''v''%s''.lp' % (n, p, v)
            open_file = open(file,'r')
            read_file = open_file.read()
            read_file = regex.sub(r'\1\2', read_file)
            write_file = open(file,'w')
            write_file.write(read_file)
