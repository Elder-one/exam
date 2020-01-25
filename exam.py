from random import randint

class Game:
    def __init__(self, randomize=True, hp=5, n=10, m=10, dmg = 2):
        self.hp = hp
        self.size = (n, m)
        self.field = self.get_field(randomize)
        self.start = self.set_start(randomize)
        self.dmg = dmg


    def get_field(self, randomize=True):
        if randomize:
            n, m = self.size
            items = ['.', '.', '☒', '*']
            result = [[items[randint(0, 3)] for i in range(n)] for j in range(m)]
            i, j = (randint(0, n-1), randint(0, m-1))
            result[i][j] = '☼'
            return result
        else:
            n, m = map(int, input('Размеры -> ').split())
            self.size = (n, m)
            result = []
            for i in range(n):
                result.append([ch for ch in input()])
            return result


    def set_start(self, randomize=True):
        if randomize:
            n, m = self.size
            i, j = (randint(0, n-1), randint(0, n-1))
            while self.field[i][j] != '.':
                i, j = (randint(0, n-1), randint(0, m-1))
            self.field[i][j] = '☺'
            return (i, j)
        else:
            i, j = map(int, input('Координаты старта').split())
            self.field[i][j] = '☺'
            return (i, j)


    def draw(self):
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if self.field[i][j] == '.':
                    print('.', end = ' ')
                if self.field[i][j] == '☼':
                    print('☼', end = ' ')
                if self.field[i][j] == '☒':
                    print('☒', end = ' ')
                if self.field[i][j] == '*':
                    print('*', end = ' ')
            print()


    def find_way(self, pos, way, hp):
        global ways
        i, j = pos
        exist = False
        if i >= 0 and i < self.size[0]:
            if j >= 0 and j < self.size[1]:
                exist = True
        if not exist:
            return
        if pos in way[:-1]:
            return
        if self.field[i][j] == '☼':
            ways.append((way, hp))
            return
        if self.field[i][j] == '*':
            hp -= self.dmg
            if hp <= 0:
                return
        if self.field[i][j] == '☒':
            return
        self.find_way((i+1, j), tuple(list(way)+[(i+1, j)]), hp)
        self.find_way((i-1, j), tuple(list(way)+[(i-1, j)]), hp)
        self.find_way((i, j+1), tuple(list(way)+[(i, j+1)]), hp)
        self.find_way((i, j-1), tuple(list(way)+[(i, j-1)]), hp)


    def get_way(self):
        global ways
        ways = []
        self.find_way(self.start, (self.start,), self.hp)
        if ways == []:
            print('Путь не найден')
        else:
            lens = [len(i[0]) for i in ways]
            index = lens.index(min(lens))
            ways = [el for el in ways if len(el[0]) == lens[index]]
            hps = [el[1] for el in ways]
            index = hps.index(max(hps))
            way = ways[index]
            for el in way[0]:
                i, j = el
                if self.field[i][j] not in ['☺', '☼']:
                    #print('Ставлю доллар')
                    self.field[i][j] = '$'
            self.draw()
        


    
