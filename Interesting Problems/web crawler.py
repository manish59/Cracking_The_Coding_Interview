import threading
import time
from bs4 import BeautifulSoup
import requests
import urllib.parse
import requests
from queue import Queue
import traceback
################################################
global LOCK
global THREADS
global THREAD_COUNT
global MAIN_URL
global LINK_QUEUE
global LINKS
######################################################
LOCK=threading.Lock()
THREAD_COUNT=4
THREADS_QUEUE=Queue(maxsize=THREAD_COUNT)
MAIN_URL="https://realpython.com/"
LINK_QUEUE=Queue()
LINKS={}
#######################################################
def get_links(url,LINKS):
    domain=urllib.parse.urlparse(url).netloc
    print(domain)
    a=open(f"{domain}.txt","a+")
    try:

        global LINK_QUEUE
        flag=False
        if url in LINKS:
            if LINKS[url]!=True:
                flag=True
        else:
            flag=True
        if flag:
            api_call=requests.get(url)
            if api_call.status_code==200:
                print("API Called successfully")
                html=api_call.text
                soup = BeautifulSoup(html, 'html.parser')
                print("Parsed Web Page")
                child_links=soup.find_all('a',href=True)
                print("Filetered hyperlinks")
                for link in child_links:
                    link = link['href']
                    if len(link)>5:
                        if link[0:4]!="http":
                            link=urllib.parse.urljoin(url,link)
                        if link not in LINKS:
                            print("Lock Acquired")
                            LOCK.acquire()
                            a.write(link + "\n")
                            LINKS[link]=False
                            LINK_QUEUE.put(link)
                            print("Lock Released")
                            LOCK.release()
                print(threading.current_thread())
                print(LINK_QUEUE.qsize())
            else:
                print(api_call.status_code)
    except Exception as error:
        print(traceback.format_exc())
        LOCK.release()
        print("Lock Released")
        THREADS_QUEUE.get()
        print(LINK_QUEUE.qsize())
    finally:
        a.close()
def main():
    main_thread=threading.Thread(target=get_links,name="Main Thread", args=(MAIN_URL,LINKS))
    print("Added Main thread to Queue")
    THREADS_QUEUE.put(main_thread)
    print("Main Thread started")
    main_thread.start()
    main_thread.join()
    print(f"Thread count:{threading.active_count()}")
    print(f"Link Queue:{LINK_QUEUE.qsize()}")
    print(LINK_QUEUE.empty()!=True and threading.active_count()<THREAD_COUNT)
    while(LINK_QUEUE.empty()!=True):
        if THREADS_QUEUE.full():
            print("Threads full waiting for all the threads to complete")
            THREADS_QUEUE.get().join()
            print(f"Current Threading Count:{threading.active_count()}")
            continue
        thread=threading.Thread(target=get_links,args=(LINK_QUEUE.get(),LINKS))
        THREADS_QUEUE.put(thread)
        thread.start()
        print(f"Thread count:{threading.active_count()}")

if __name__ == '__main__':
    main()
