
import numpy as np
import os
import time
from Endec import Endec



class Dec(Endec):
    def __init__(self):
        print('Initializing Dec class')
        super().__init__()
    
    def __filestodec():
        cwd = os.getcwd()
        print('cwd -', cwd)
        fl = os.listdir(cwd)
        filestodec = filter(lambda x: x.split('.')[-2].endswith('_') if '.' in x else x.endswith('_'), fl)
        filestodec = list(filestodec)
        if Endec.op_folder in filestodec:
            filestodec.remove(Endec.op_folder)
        if '__pycache__' in filestodec:
            filestodec.remove('__pycache__')
        for src_file in Endec.src_file_names:
            if src_file in filestodec:
                filestodec.remove(src_file)
        return filestodec
    
    def dec(e):
        e = np.frombuffer(e, dtype='uint16')
        e = e.astype(np.uint64)
        
        m = Endec.mypow(e, Dec.K, Dec.N)
        m = m.astype(np.uint8)
        return m
    
    def dec_runner(self):
        try:
            t0 = time.time()
            
            filestodec = Dec.__filestodec()
            print('filestodec', filestodec)
            nooff = len(filestodec)
            
            print('nooff', nooff)
            for i in range(nooff):
                e = Endec.read_f(filestodec[i])
                Endec.size += len(e)
                
                m = Dec.dec(e)
                
                epath = Endec.get_endec_path(filestodec[i])
                Endec.write_f(epath, m)
                
                print(i+1, '/', nooff)
                print(((i+1)*100)/nooff, '% done')
            
            Endec.time = time.time()-t0
            Endec.print_stats()
            Endec.cmd_exit('All '+str(nooff)+' files decoded')
        except Exception as e:
            print('Exception Occured')
            print(e)
            raise e
            Endec.cmd_exit('')



if __name__ == '__main__':
    Dec().dec_runner()




