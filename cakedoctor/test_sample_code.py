import threading

def do_some_work(val):
    print ("Doing some work in thread")
    print ("echo : {}".format(val))
    return

val = "text"
exicutor_thread = threading.Thread(target=do_some_work, args=(val,))
exicutor_thread.start()
exicutor_thread.join() 