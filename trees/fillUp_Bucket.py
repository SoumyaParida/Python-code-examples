"""
Bucket Fill Exercise

Imagine you are working on an image editing application. You need to implement a bucket fill tool similar to the one
in paint. The user will use the tool by selecting a color and clicking on the canvas. The tool fills the selected
region of color with the new color.

When a pixel is filled, all of its neighbors (above, below, left, or right) of the same color must also be filled,
as well as their neighbors, and so on, until the entire region has been filled with the new color.

In this exercise, you must write *TWO* implementations of the tool. Each implementation must be different. It is not
required that you invent the solutions yourself. You are encouraged to research the problem. Please write documentation
explaining the difference of each implementation, such as when one solution might be more appropriate than the other.
Don't forget to validate input. There is one existing test, however, you might consider adding some more. Keep in mind
that although the given canvas is small, the solution should be applicable for a real canvas that could have huge
resolutions.

Please use python3 to complete this assignment.
"""

import time
timing_count = 0

def timing(f):
    """
    to keep track of the time spent for bothe the solutions.
    """
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        args[0].timing_count += (time2 - time1) * 1000.0
        return ret
    return wrap


class Canvas(object):
    """
       Parent canvas with some commond method and fill method definition.
       It has some tooling to keep track of the data access and validation.
       Must be extended by the concrete implementations.
       """

    class access_count_array(list):
        """
        Access counter for image matrix.
        """

        def set_parent(self, parent):
            self.parent = parent

        def __getitem__(self, index):
            self.parent.pixel_comparisons += 1
            return list.__getitem__(self, index)

    def __init__(self, pixels):
        self.pixels = Canvas.access_count_array(pixels)
        self.pixels.set_parent(self)
        self.pixel_comparisons = 0
        self.timing_count = 0

    def __str__(self):
        return '\n'.join(map(lambda row: ''.join(row), self.pixels))

    def fill(self, x, y, color):
        """
        Fills a region of color at a given location with a given color.

        :param x:  the x coordinate where the user clicked
        :param y: the y coordinate where the user clicked
        :param color: the specified color to change the region to
        """
        raise NotImplementedError  # Override this function in the Solution classes

    def validate(self, x, y, color):
        """
        Common validation for the fill input
        :param x:  the x coordinate where the user clicked
        :param y: the y coordinate where the user clicked
        :param color: the specified color to change the region to
        """

        # check that the seed value are integers
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError(
                "Invalid pixel seed format. Expecting integers {},{}".format(
                    x, y))

        # check that the seed value are within the image interval
        if x < 0 or x >= len(self.pixels) \
                or y < 0 or y >= len(self.pixels[0]):
            raise ValueError(
                "Invalid pixel seed for flood fill {},{}".format(
                    x, y))

        # check that the image has a size
        if len(self.pixels) == 0 or len(self.pixels[0]) == 0:
            raise ValueError("Image has an empty dimension")

        # check that the image has consistent sizes accross its dimensions
        len_h = len(self.pixels[0])

        if any([len_h != len(pixels) for pixels in self.pixels]):
            raise ValueError("Invalid image. Rows and columns have inconsistent sizes")

        # check that the new color is the same type of the pixels
        data_type = type(self.pixels[0][0])

        # This check is not always valid. numpy uses uint8 integers while the user can be in int format
        # The algorithm is still able to run properly

        # color == self.pixels[x][y]
        # if type(color) is not data_type:
        #    raise ValueError("Pixel img and chosen color are of different types: {} and {}"
        #                     .format(type(color), data_type))

        # check that all image pixels have the same type
        for t in self.pixels:
            for y in t:
                if type(y) is not data_type:
                    raise ValueError("Image contains inconsistent data")

class ScanlineOpenCV(Canvas):
    """
        This is a scan line approach as designed by OpenCV. The algorithm is similar to
        the scanline as described above but it uses a different flow. Instead of filling
        from left to right, it starts filling from the center to both horizontal directions.
        It maintains a left and right index which are added to the stack and processed
        at each iteration.
        """

    @timing
    def fill(self, x, y, color):
        self.validate(x, y, color)

        old_color = self.pixels[x][y]

        if old_color == color:
            return  # nothing to do

        self.max_depth = 0
        w = len(self.pixels[0])     #height
        h = len(self.pixels)        #width

        l = y
        r = y

        while (r < w and self.pixels[x][r] == old_color):
            self.pixels[x][r] = color
            r += 1

        l -= 1
        while (l >= 0 and self.pixels[x][l] == old_color):
            self.pixels[x][l] = color
            l -= 1

        l += 1
        r -= 1

        stack = [(x, l, r, r + 1, r, 1)]

        while stack:
            self.max_depth = max(self.max_depth, len(stack))
            yc, l, r, pl, pr, dirz = stack.pop()
            data = [[-dirz, l, r], [dirz, l, pl - 1], [dirz, pr + 1, r]]

            for i in range(0, 3):
                dirz = data[i][0]
                yc_d = yc + dirz
                if yc_d >= h or yc_d < 0:
                    continue

                left = data[i][1]
                right = data[i][2]

                k = left

                while k <= right:
                    if k >= 0 and k < w and self.pixels[yc_d][k] == old_color:
                        self.pixels[yc_d][k] = color
                        j = k

                        j -= 1
                        while j >= 0 and self.pixels[yc_d][j] == old_color:
                            self.pixels[yc_d][j] = color
                            j -= 1

                        k += 1
                        while k < w and self.pixels[yc_d][k] == old_color:
                            self.pixels[yc_d][k] = color
                            k += 1

                        stack.append((yc_d, j + 1, k - 1, l, r, -dirz))

                    k += 1
                    #pass


class ScanlineWikipedia(Canvas):
    """
        This bucket fill solution use stack instead of recurion which is not useful for
        a real canvas that could have huge resolutions.At each iteration the stack is
        increased with new pixels.The idea is to start filling the areas by entire lines,
        stopping when it finds a border pixel (a pixel which does not require filling). While filling
        the line, it also adds to the stack the pixel above and below the beginning of the line.
    """

    @timing
    def fill(self, x, y, color):
        self.validate(x, y, color)

        self.max_depth = 0
        old_color = self.pixels[x][y]

        if old_color == color:
            return  # nothing to do

        stack = [(y, x)]
        w = len(self.pixels[0])
        h = len(self.pixels)

        while stack:
            self.max_depth = max(self.max_depth, len(stack))
            cur_point = stack.pop()
            x1, y1 = cur_point

            while x1 >= 0 and self.pixels[y1][x1] == old_color:
                x1 -= 1
            x1 += 1

            above = False
            below = False

            while x1 < w and self.pixels[y1][x1] == old_color:
                self.pixels[y1][x1] = color

                if not above and y1 > 0 and self.pixels[y1 - 1][x1] == old_color:
                    stack.append((x1, y1 - 1))
                    above = True
                elif above and y1 < h - 1 and self.pixels[y1 - 1][x1] != old_color:
                    above = False

                if not below and y1 < h - 1 and self.pixels[y1 + 1][x1] == old_color:
                    stack.append((x1, y1 + 1))
                    below = True
                elif below and y1 < h - 1 and self.pixels[y1 + 1][x1] != old_color:
                    below = False

                x1 += 1
