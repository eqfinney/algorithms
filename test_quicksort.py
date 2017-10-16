import quicksort as q
from collections import defaultdict

"""
def test_qfirst_ten():
    integers = q.read_integers('integers_2.txt')
    integers = integers[:10]
    value = q.quicksort_first(integers)[1]
    actual = 25
    assert value == actual


def test_qfirst_hundred():
    integers = q.read_integers('integers_2.txt')
    integers = integers[:100]
    value = q.quicksort_first(integers)[1]
    actual = 620
    assert value == actual


def test_qfirst_thousand():
    integers = q.read_integers('integers_2.txt')
    integers = integers[:1000]
    value = q.quicksort_first(integers)[1]
    actual = 11175
    assert value == actual
"""

def test_qlast_ten():
    integers = q.read_integers('integers_2.txt')
    integers = integers[:10]
    value = q.quicksort_last(integers)[1]
    actual = 31
    assert value == actual


def test_qlast_hundred():
    integers = q.read_integers('integers_2.txt')
    integers = integers[:100]
    value = q.quicksort_last(integers)[1]
    actual = 573
    assert value == actual


def test_qlast_thousand():
    integers = q.read_integers('integers_2.txt')
    integers = integers[:1000]
    value = q.quicksort_last(integers)[1]
    actual = 10957
    assert value == actual
    

def test_qmedian_ten():
    integers = q.read_integers('integers_2.txt')
    integers = integers[:10]
    list_ints, value = q.quicksort_median(integers)
    actual = 21
    print(list_ints)
    print(value, actual)
    assert value == actual


def test_qmedian_hundred():
    integers = q.read_integers('integers_2.txt')
    integers = integers[:100]
    list_ints, value = q.quicksort_median(integers)
    actual = 502
    print(list_ints)
    print(value, actual)
    assert value == actual


def test_qmedian_thousand():
    integers = q.read_integers('integers_2.txt')
    integers = integers[:1000]
    value = q.quicksort_median(integers)[1]
    actual = 9735
    assert value == actual

