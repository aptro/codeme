from collections import namedtuple

Info = namedtuple('Info', 'start height')

def max_rectangle_area(histogram):
    """Find the area of the largest rectangle that fits entirely under
    the histogram.

    """
    stack = []
    top = lambda: stack[-1]
    max_area = 0
    pos = 0 # current position in the histogram
    for pos, height in enumerate(histogram):
        start = pos # position where rectangle starts
        while True:
            if not stack or height > top().height:
                stack.append(Info(start, height)) # push
            elif stack and height < top().height:
                max_area = max(max_area, top().height*(pos-top().start))
                start, _ = stack.pop()
                continue
            break # height == top().height goes here

    pos += 1
    for start, height in stack:
        max_area = max(max_area, height*(pos-start))

    return max_area