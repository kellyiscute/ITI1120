# COPYRIGHT 2019, Vida Dujmovic. All rights reserved.
# Any unauthorised distribution will constitute an infringement of copyright.
import typing


class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point(' + str(self.x) + ',' + str(self.y) + ')'

    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point(' + str(self.x) + ',' + str(self.y) + ')'


class Rectangle(object):
    num = 0

    def __init__(self, bottom_left: Point, top_right: Point, color='blue'):
        self.color = color
        self.bottom_left = bottom_left
        self.top_right = top_right

    def __eq__(self, other: 'Rectangle'):
        return self.top_right == other.top_right and self.bottom_left == other.bottom_left

    def __repr__(self):
        return f'{self.color} Rectangle at {self.bottom_left} with perimeter: {self.get_perimeter()}'

    def __str__(self):
        return f'{self.color} Rectangle at {self.bottom_left} with perimeter: {self.get_perimeter()}'

    def get_bottom_left(self):
        return self.bottom_left

    def get_top_right(self):
        return self.top_right

    def get_color(self):
        return self.color

    def reset_color(self, color):
        self.color = color

    def get_perimeter(self):
        return ((self.top_right.x - self.bottom_left.x) + (self.top_right.y - self.bottom_left.y)) * 2

    def get_area(self):
        return (self.top_right.x - self.bottom_left.x) * (self.top_right.y - self.bottom_left.y)

    def move(self, dx, dy):
        self.bottom_left.move(dx, dy)
        self.top_right.move(dx, dy)

    def intersects(self, other: 'Rectangle'):
        return self.contains(other.bottom_left.x, other.bottom_left.y) or \
               self.contains(other.top_right.x, other.bottom_left.y) or \
               self.contains(other.top_right.x, other.top_right.y) or \
               self.contains(other.bottom_left.x, other.top_right.y) or \
               (self.bottom_left.x <= other.top_right.x <= self.top_right.x
                and other.top_right.y >= self.top_right.y and other.bottom_left.y <= self.bottom_left.y) or \
               (self.bottom_left.x >= other.top_right.x >= self.top_right.x
                and other.top_right.y <= self.top_right.y and other.bottom_left.y >= self.bottom_left.y) or \
               (self.bottom_left.y <= other.top_right.y <= self.top_right.y
                and other.top_right.x >= self.top_right.x and other.bottom_left.x <= self.bottom_left.x) or \
               (self.bottom_left.y >= other.top_right.y >= self.top_right.y
                and other.top_right.x <= self.top_right.x and other.bottom_left.x >= self.bottom_left.x)

    def contains(self, x, y):
        return (self.bottom_left.x <= x <= self.top_right.x) and \
               (self.bottom_left.y <= y <= self.top_right.y)


class Canvas(object):
    def __init__(self):
        self.rectangles: typing.List[Rectangle] = []

    def __repr__(self):
        return f'Canvas with {len(self.rectangles)} rectangles'

    def __len__(self):
        return len(self.rectangles)

    def add_one_rectangle(self, rect: Rectangle):
        self.rectangles.append(rect)

    def count_same_color(self, color):
        total = 0
        for rectangle in self.rectangles:
            if rectangle.color == color:
                total += 1
        return total

    def total_perimeter(self):
        total = 0
        for rectangle in self.rectangles:
            total += rectangle.get_perimeter()
        return total

    def min_enclosing_rectangle(self):
        if len(self.rectangles) == 0:
            return None

        min_x = self.rectangles[0].bottom_left.x
        max_x = 0
        min_y = self.rectangles[0].bottom_left.y
        max_y = 0

        # Find min x
        for rectangle in self.rectangles:
            if rectangle.bottom_left.x < min_x:
                min_x = rectangle.bottom_left.x

        # Find min y
        for rectangle in self.rectangles:
            if rectangle.bottom_left.y < min_y:
                min_y = rectangle.bottom_left.y

        # Find max x
        for rectangle in self.rectangles:
            if rectangle.top_right.x > max_x:
                max_x = rectangle.top_right.x

        # Find max y
        for rectangle in self.rectangles:
            if rectangle.top_right.y > max_y:
                max_y = rectangle.top_right.y

        return Rectangle(Point(min_x, min_y), Point(max_x, max_y))

    def common_point(self):
        current_rect = self.rectangles[0]
        for rectangle in self.rectangles:
            if rectangle.intersects(current_rect):
                bottom_left = Point(min((rectangle.bottom_left.x, current_rect.bottom_left.x)),
                                    min((rectangle.bottom_left.y, current_rect.bottom_left.y)))
                top_right = Point(min((rectangle.top_right.x, current_rect.top_right.x)),
                                  min((rectangle.top_right.y, current_rect.top_right.y)))
                current_rect = Rectangle(bottom_left, top_right)
            else:
                return False
        return True
