
import os
import sys



class Endec():
    src_file_names = ['Endec.py', 'En.py', 'Dec.py']
    op_folder = 'endec'
    file_post_str = '_'
    time = 0
    size = 0
    N = None
    K = None
    
    def __init__(self, n = None, k = None):
        print('Initializing Encdec class')
        Endec.op_folder = 'endec'
        Endec.file_post_str = '_'
        Endec.time = 0
        Endec.size = 0
        Endec.N = n
        Endec.K = k
        
        Endec.set_endec_path()
        if n is None or k is None:
            Endec.setNK()
    
    def setNK():
        try:
            print('n:')
            n = int(input())
            if n < 0:
                raise ValueError('number invalid')
            Endec.N = n
            print('k:')
            k = int(input())
            if k < 0 or k >= n:
                raise ValueError('number invalid')
            Endec.K = k
        except ValueError as ve:
            Endec.cmd_exit(str(ve))
    
    def set_endec_path():
        if not os.path.isdir(Endec.op_folder):
            os.mkdir(Endec.op_folder)
    
    def cmd_exit(msg):
        print(msg)
        print(
            'Terminating program\
            \nPress enter to close'
        )
        input() # pause cmd, to view op
        sys.exit()
    
    def get_endec_path(path):
        ext = ''
        if '.' in path:
            p = path.split('.')
            path = '.'.join(p[:-1])
            ext = p[-1]
            return Endec.op_folder + '/' + path + Endec.file_post_str + '.' + ext
        else:
            return Endec.op_folder + '/' + path + Endec.file_post_str
    
    def read_f(path):
        print('reading file', path)
        with open(path, 'rb') as f:
            m = f.read()
        return m
    
    def write_f(epath, e):
        with open(epath, 'wb') as f2:
            for ei in e:
                f2.write(ei)
    
    def mypow(n, p, m):
        n%=m
        if p>1:
            if p%2:
                return (Endec.mypow(n*n, p//2, m) * n)%m
            else:
                return Endec.mypow(n*n, p/2, m)
        else:
            return n%m
    
    def print_stats():
        print('time', Endec.time)
        if Endec.size > 0 and Endec.time > 0:
            print('seconds/byte', Endec.time/Endec.size)
            print('bytes/second', Endec.size/Endec.time)
            print('KB/second', (Endec.size/1024)/Endec.time)
            print('MB/second', (Endec.size/1048576)/Endec.time)



if __name__ == '__main__':
    endecobj = Endec()




