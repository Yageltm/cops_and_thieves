import random


class Map:
    def __init__(self, map_file):
        f = open(map_file, 'rb')
        b_map = f.read()
        self.g_map = []
        length = int(b_map[0])
        b_map = b_map[1:]
        count = 0
        for i in range(len(b_map) // length):
            new_list = []
            for j in range(length):
                new_list.append(int(b_map[count]))
                count += 1
            self.g_map.append(new_list)
        self.t_loc, self.c_loc, self.x_loc = self.random_location(self.g_map), self.random_location(self.g_map),\
    self.random_location(self.g_map)

    @staticmethod
    def random_location(map_list):
        while True:
            y = random.randint(0, len(map_list)-1)
            x = random.randint(0, len(map_list[0])-1)
            loc = map_list[y][x]
            if loc == 0:
                return [y, x]

    def __str__(self):
        updated_map = self.g_map
        updated_map[self.t_loc[0]][self.t_loc[1]] = 'T'
        updated_map[self.c_loc[0]][self.c_loc[1]] = 'C'
        updated_map[self.x_loc[0]][self.x_loc[1]] = 'X'
        str_map = ''
        for raw in updated_map:
            for chr in raw:
                if chr == 1:
                    str_map += '*'
                elif chr == 0:
                    str_map += ' '
                else:
                    str_map += chr
            str_map += '\n'
        return str_map

    def status(self):
        print(self)
        if abs(self.c_loc[0]-self.t_loc[0]) == 1 and self.c_loc[1]-self.t_loc[1] == 0:
            return 'COP NEAR'
        if abs(self.c_loc[0]-self.t_loc[0]) == 0 and self.c_loc[1]-self.t_loc[1] == 1:
            return 'COP NEAR'
        if abs(self.x_loc[0]-self.t_loc[0]) == 1 and self.x_loc[1]-self.t_loc[1] == 0:
            return 'TREASURE NEAR'
        if abs(self.x_loc[1]-self.t_loc[1]) == 1 and self.x_loc[0]-self.t_loc[0] == 0:
            return 'TREASURE NEAR'
        else:
            return 'GAME ON'

    def wall_check(self, loc):
        if self.g_map[loc[0]][loc[1]] == 1:
            return True
        return False

    def move(self, direction):
        if direction == "LEFT":
            new_loc = [self.t_loc[0], self.t_loc[1]-1]
        elif direction == "RIGHT":
            new_loc = [self.t_loc[0], self.t_loc[1]+1]
        elif direction == "UP":
            new_loc = [self.t_loc[0]-1, self.t_loc[1]]
        elif direction == "DOWN":
            new_loc = [self.t_loc[0]+1, self.t_loc[1]]
        if self.wall_check(new_loc):
            return 'WALL'
        if new_loc == self.x_loc:
            return 'WON'
        if new_loc == self.c_loc:
            return 'LOST'
        else:
            self.g_map[self.t_loc[0]][self.t_loc[1]] = 0
            self.t_loc = new_loc
            return 'OK'

    def move_cop(self):
        x_change = random.randint(-1, 1)
        y_change = random.randint(-1, 1)
        new_loc = [self.c_loc[0]+y_change, self.c_loc[1]+x_change]
        if not self.wall_check(new_loc) and new_loc != self.t_loc and new_loc != self.x_loc:
            self.g_map[self.c_loc[0]][self.c_loc[1]] = 0
            self.c_loc = new_loc



