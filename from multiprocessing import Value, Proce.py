from multiprocessing import Process, Pipe

class StudentClass():
    def __init__(self):
        self.passing = False
    def isPassing(self):
        return self.passing
    


def work(connection):
        instance = connection.recv()
        instance.passing = True
        print("CILD: {}".format(instance.isPassing()))

if __name__ == "__main__":
    parent_conn, child_conn = Pipe() #Connection between parent and child
    child = Process(target=work, args=(child_conn,))

    item = StudentClass()
    print("PRNT: {}".format(item.isPassing()))
    parent_conn.send(item)

    child.start()
    print("PRNT: {}".format(item.isPassing()))
    child.join()


