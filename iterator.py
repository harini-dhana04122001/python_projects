# import itertools
# import operator
#
# # example for count in itertools
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# seq1 = itertools.count(start=5, step=5)
# print('count : ', list(zip(list(next(seq1) for _ in range(1, 11)), list1)))
#
# # example for cycle  in itertools
# list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# seq2 = itertools.cycle(list2)
# print('cycle : ', list(next(seq2) for _ in range(20)))
#
# # example for chain in itertools
# list3 = [{1, 2, 3}, 'def', {1: 'q', 2: 'w'}]
# seq3 = itertools.chain.from_iterable(list3)
# print('chain : ', list(seq3))
#
# # example for repeat in itertools
# seq4 = itertools.repeat({1, 2, 3}, 10)
# print('repeat : ', list(seq4))
#
# # we can fill the list with default value for lesser list while zipping
# list4 = ['harini', 'moni', 'siva', 'saira']
# list5 = [21, 22]
# print('zip longest : ', list(itertools.zip_longest(list4, list5, fillvalue=21)))
#
#
# # gives the product of an iterable with itself
# print('product of sequence : ', list(itertools.product('ABCD', repeat=2)))
#
#
# '''gives out permutation result of given iterable, and we can also specify length of
# the iterable  '''
# seq5 = itertools.permutations(['A', 'B', 'C'], 2)
# print('permutation : ', list(seq5))
#
#
# ''' Same as permutation, return possible combination of iterable with specified length '''
# seq1 = itertools.combinations(['A', 'B', 'C'], 2)
# print('combination : ', list(seq1))
#
#
# '''  elements from the input iterable allowing individual elements to be repeated more than once '''
# print('combination with replacement : ', list(itertools.combinations_with_replacement(
#     ['A', 'B', 'C'], 2
# )))    # output will be the same as product
#
# ''' returns result of accumulated sum '''
# list6 = [1, 7, 3, 10, 5]
# print('accumulation : ', list(itertools.accumulate(list6)))
# print('accumulation with multiplication : ', list(itertools.accumulate(list6, operator.mul)))
# # gives max value until new maximum is found
# print('accumulation with max', list(itertools.accumulate(list6, max)))
#
# list7 = {'name', 'age'}
# print('compress :', list(itertools.compress(list7, [True, False])))

"""
creating custom iterator.
"""


class ReverseList:

    def __init__(self, iterable):
        self.iterable = list(iterable)
        self.index = len(self.iterable)

    def __iter__(self):
        # self.index = len(self.iterable)
        return self

    def __next__(self):
        self.index -= 1
        if self.index < 0:
            raise StopIteration()
        return self.iterable[self.index]


reverse = ReverseList([1, 2, 4, 5, 6])
reversed_iter = iter(reverse)

for n in reversed_iter:
    print(n)
