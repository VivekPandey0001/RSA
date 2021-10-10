
import numpy as np
import os
import time
from Endec import Endec



class En(Endec):
    def __init__(self):
        print('Initializing Enc class')
        super().__init__()
    
    def __filestoenc():
        cwd = os.getcwd()
        print('cwd -', cwd)
        fl = os.listdir(cwd)
        filestoenc = filter(lambda x: not x.split('.')[-2].endswith('_') if '.' in x else not x.endswith('_'), fl)
        filestoenc = list(filestoenc)
        if Endec.op_folder in filestoenc:
            filestoenc.remove(Endec.op_folder)
        if '__pycache__' in filestoenc:
            filestoenc.remove('__pycache__')
        for src_file in Endec.src_file_names:
            if src_file in filestoenc:
                filestoenc.remove(src_file)
        print('filestoenc -', len(filestoenc))
        return filestoenc
    
    def enc(m):
        m = np.frombuffer(m, dtype='uint8')
        m = m.astype(np.uint64)
        
        if En.K is None or En.N is None:
            raise Exception('N or K cannot be None')
        e = Endec.mypow(m, En.K, En.N)
        e = e.astype(np.uint16)
        return e
    
    def enc_runner(self):
        try:
            t0 = time.time()
            
            filestoenc = En.__filestoenc()
            print('filestoenc', filestoenc)
            nooff = len(filestoenc)
            
            print('nooff', nooff)
            for i in range(nooff):
                m = Endec.read_f(filestoenc[i])
                Endec.size += len(m)
                
                e = En.enc(m)
                
                epath = Endec.get_endec_path(filestoenc[i])
                Endec.write_f(epath, e)
                
                print(i+1, '/', nooff)
                print(((i+1)*100)/nooff, '% done')
            
            Endec.time = time.time()-t0
            Endec.print_stats()
            Endec.cmd_exit('All '+str(nooff)+' files encoded')
        except Exception as e:
            print('Exception Occured')
            print(e)
            raise e
            Endec.cmd_exit('')



if __name__ == '__main__':
    En().enc_runner()




