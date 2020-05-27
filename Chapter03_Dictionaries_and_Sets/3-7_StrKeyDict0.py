# 这个程序支持用数字来索引字符串的key
# __getitem__在遇到新key是调用__missing__

class StrKeyDict(dict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


if __name__ == '__main__':
    dd = StrKeyDict([('2', 'two'), ('4', 'four')])
    print(dd[2])            # two
    print(4 in dd)          # True
    print(dd.get('5'))      # None
