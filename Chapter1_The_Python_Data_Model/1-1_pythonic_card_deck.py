# python的特殊方法是给解释器调用的。

# len()会调用对象的__len__()
# []会调用对象的__getitem__()。实现了__getitem__()的对象即是iterable
# in会调用__contains__()。没有的话，会遍历对象，即对象是iterable就可以用in

import collections

# namedtuple一般用来创建只有属性，没有方法的简单的类
# 第一个参数是对象转化成字符串时显示的类的名字，第二个参数是一个attrs列表
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

if __name__ == '__main__':
    beer_card = Card('7', 'diamonds')
    print('beer_card = {}'.format(beer_card))

    deck = FrenchDeck()
    print('len(deck) = {}'.format(len(deck)))  # 52
    print(f'deck[0] = {deck[0]}\ndeck[-1] = {deck[-1]}')

