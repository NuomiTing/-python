import time

import blog_spider
import threading

def single_thread():
    for url in blog_spider.urls:
        blog_spider.craw(url)

def multi_tread():
    threads=[]
    for url in blog_spider.urls:
        threads.append(threading.Thread(
            target=blog_spider.craw,
            args=(url,)
        ))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__=="__main__":
    '''
    通过时间就可以看出这个多线远远高效与单线程
    '''
    start = time.time()
    single_thread()
    end = time.time()
    print("single_thread cost:", end-start,"sceonds")

    start = time.time()
    multi_tread()
    end = time.time()
    print("multi_tread cost:", end - start, "sceonds")
