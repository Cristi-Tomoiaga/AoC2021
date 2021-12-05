"""
AoC day 5
"""


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def __eq__(self, other):
        return self.get_x() == other.get_x() and self.get_y() == other.get_y()

    def __str__(self):
        return f"{self.get_x()},{self.get_y()}"

    def __hash__(self):  # used for sets, equal objects should have equal hash results
        return hash(str(self))


class Line:
    def __init__(self, point1, point2):
        self.__points = set()

        if point1.get_x() == point2.get_x() and point1.get_y() != point2.get_y():  # vertical line
            common_x = point1.get_x()
            start_y = min(point1.get_y(), point2.get_y())
            end_y = max(point1.get_y(), point2.get_y())

            for y in range(start_y, end_y + 1):
                self.__points.add(Point(common_x, y))

        elif point1.get_y() == point2.get_y() and point1.get_x() != point2.get_x():  # horizontal line
            common_y = point1.get_y()
            start_x = min(point1.get_x(), point2.get_x())
            end_x = max(point1.get_x(), point2.get_x())

            for x in range(start_x, end_x + 1):
                self.__points.add(Point(x, common_y))

        else:  # diagonal lines - part 2
            m = int((point1.get_y() - point2.get_y()) / (point1.get_x() - point2.get_x()))
            start_point = point1 if point1.get_x() < point2.get_x() else point2
            end_point = point1 if point1.get_x() > point2.get_x() else point2
            steps = abs(start_point.get_x() - end_point.get_x()) + 1

            if m > 0:  # +45 degrees
                for step in range(steps):
                    self.__points.add(Point(start_point.get_x() + m * step, start_point.get_y() + m * step))
            elif m < 0:  # -45 degrees
                for step in range(steps):
                    self.__points.add(Point(start_point.get_x() - m * step, start_point.get_y() + m * step))

    def intersect_with(self, other_line):
        return self.__points.intersection(other_line.__points)


class OceanFloor:
    def __init__(self, filename):
        self.__lines = []
        with open(filename, "r") as fh:
            for line in fh:
                points = line.strip().split(" -> ")
                point1 = [int(el) for el in points[0].strip().split(",")]
                point2 = [int(el) for el in points[1].strip().split(",")]
                line = Line(Point(point1[0], point1[1]), Point(point2[0], point2[1]))

                self.__lines.append(line)

    def count_points(self):
        points = set()
        for i in range(len(self.__lines)):
            for j in range(i + 1, len(self.__lines)):
                points.update(self.__lines[i].intersect_with(self.__lines[j]))

        return len(points)


ocean_floor = OceanFloor("input.txt")
print(ocean_floor.count_points())
