class Point(object):
    x = 1
    y = 1

    def distance(self, x, y):
        return ((self.x - x) ** 2 + (self.y - y) ** 2) ** 0.5

my_point = Point()
print(my_point.distance(4, 5)) # 5
print(my_point.x) # 1
print(my_point.y) # 1