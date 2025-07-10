from threading import Semaphore

class Foo:
    def __init__(self):
        self.semaphores = [Semaphore(1), Semaphore(0), Semaphore(0)]

    def first(self, printFirst: 'Callable[[], None]') -> None:
        self.semaphores[0].acquire()
        printFirst()
        self.semaphores[1].release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.semaphores[1].acquire()
        printSecond()
        self.semaphores[2].release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.semaphores[2].acquire()
        printThird()
        self.semaphores[0].release()
