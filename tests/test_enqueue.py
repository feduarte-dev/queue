from src.queue import Queue


def test_enqueue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(3)
    queue.enqueue(2)
