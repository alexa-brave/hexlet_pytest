import pytest


def test_stack():
    stack = []
    stack.append(1)
    stack.append(2)
    assert stack.pop() == 2
    assert stack.pop() == 1


def test_stack_empty():
    stack = []
    assert not stack
    stack.append(3)
    assert bool(stack)
    stack.pop()
    assert not stack


def test_stack_pop():
    stack = []
    with pytest.raises(IndexError):
        assert stack.pop()
