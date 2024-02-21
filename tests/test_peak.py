from src.queue import Queue


def test_peek():
    queue = Queue()
    queue.enqueue(1)
    assert queue.peek().value == 1
