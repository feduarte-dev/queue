from src.queue import Queue


def test_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(3)
    queue.enqueue(2)

    expect = [1, 3, 2]

    out = []
    while not queue.is_empty():
        out.append(queue.dequeue().value)

    assert out == expect
