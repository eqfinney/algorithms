import contraction as c
from collections import defaultdict

def test_read_graph():
    graph = c.read_graph('graph2.txt')
    actual_graph = defaultdict(list, {'1': ['2', '3', '4', '7'],
                                      '2': ['1', '3', '4'],
                                      '3': ['1', '2', '4'],
                                      '4': ['1', '2', '3', '5'],
                                      '5': ['4', '6', '7', '8'],
                                      '6': ['5', '7', '8'],
                                      '7': ['1', '5', '6', '8'],
                                      '8': ['5','6','7']})
    assert graph == actual_graph


def test_contract_nodes():
    graph = c.read_graph('graph2.txt')
    node1 = '1'
    node2 = '2'
    new_graph = c.contract_nodes(graph, node1, node2)
    actual_graph = defaultdict(list, {'2': ['3', '4', '3', '4', '7'],
                                      '3': ['2', '2', '4'],
                                      '4': ['2', '2', '3', '5'],
                                      '5': ['4', '6', '7', '8'],
                                      '6': ['5', '7', '8'],
                                      '7': ['2', '5', '6', '8'],
                                      '8': ['5','6','7']})
    assert new_graph == actual_graph


def test_remove_self_loops():
    graph = defaultdict(list, {'2': ['3', '4', '3', '4', '7'],
                               '3': ['2', '2', '4'],
                               '4': ['2', '2', '3', '5'],
                               '5': ['4', '5', '5', '5'],
                               '6': ['5', '7', '8'],
                               '7': ['2', '5', '6', '8'],
                               '8': ['5','6','7']})
    new_graph = c.remove_self_loops(graph)
    actual_graph = defaultdict(list, {'2': ['3', '4', '3', '4', '7'],
                                      '3': ['2', '2', '4'],
                                      '4': ['2', '2', '3', '5'],
                                      '5': ['4'],
                                      '6': ['5', '7', '8'],
                                      '7': ['2', '5', '6', '8'],
                                      '8': ['5','6','7']})
    assert new_graph == actual_graph
    

def test_rc_0():
    graph = defaultdict(list, {'1': ['2', '3', '5'], '2': ['1', '3'], '3': ['1', '2', '4', '5'], '4': ['3', '5'],
                               '5': ['1', '3', '4']})
    value = c.random_contraction(graph)
    answer = 2
    assert value == answer

def test_rc_1():
    graph = defaultdict(list, {'1': ['2', '3'], '2': ['1'], '3': ['1']})
    value = c.random_contraction(graph)
    answer = 1
    assert value == answer
"""
def test_rc_2():
    graph = c.read_graph('graph2.txt')
    print(graph)
    value = c.random_contraction(graph)
    answer = 2
    assert value == answer

def test_rc_3():
    graph = c.read_graph('graph3.txt')
    value = c.random_contraction(graph)
    answer = 2
    assert value == answer

def test_rc_4():
    graph = c.read_graph('graph4.txt')
    value = c.random_contraction(graph)
    answer = 1
    assert value == answer

def test_rc_5():
    graph = c.read_graph('graph5.txt')
    value = c.random_contraction(graph)
    answer = 1
    assert value == answer

def test_rc_6():
    graph = c.read_graph('graph6.txt')
    value = c.random_contraction(graph)
    answer = 3
    assert value == answer
"""
def test_rc_7():
    graph = c.read_graph('graph7.txt')
    value = c.random_contraction(graph)
    answer = 2
    assert value == answer
