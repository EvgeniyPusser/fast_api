from threading import Thread


def worker():
    print("Worker thread started")
    print("Worker thread finished")


if __name__ == "__main__":
    thread1 = Thread(target=worker)
    thread2 = Thread(target=worker)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
