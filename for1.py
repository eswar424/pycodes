import multiprocessing
import time
class process(multiprocessing.Process):
    def __init__(self, id):
        super(process,self).__init__()
        self.id=id
        def run(self):
            time.sleep(1)
            print("i' am the processwith id:{}".format(self.id))

if __name__=="__main__":
    p=process(0)
    p.start()
    p.join()
    p=process(1)
    p.start()
    p.join()
