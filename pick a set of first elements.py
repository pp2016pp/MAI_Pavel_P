
def first(seq, n=1):
    list = []
    if n > len(seq):
        n = len(seq)
    for i in range(n):
        list.append(seq[i])
    return list
    # print(list)

seq = ['a', 'b', 'c', 'd', 'e']
first(seq, 10)
"""test.assert_equals(first(seq), ['a'])
    test.assert_equals(first(seq, 0), []);
    test.assert_equals(first(seq, 1), ['a']);
    test.assert_equals(first(seq, 2), ['a', 'b']);
    test.assert_equals(first(seq, 10), ['a', 'b', 'c', 'd', 'e'])"""