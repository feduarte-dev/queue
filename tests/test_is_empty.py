from src.queue import Queue


def test_is_empty():
    queue = Queue()
    assert queue.is_empty() is True
    queue.enqueue(1)
    assert queue.is_empty() is False
