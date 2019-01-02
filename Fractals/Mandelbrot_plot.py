from PIL import Image, ImageDraw
from mandelbrot import mandelbrot, MAX_ITER
from collections import defaultdict
from math import floor, ceil


def linear_interpolation(color1, color2, t):
    return color1 * (1 - t) + color2 * t


# image size in px
WIDTH = 600
HEIGHT = 400

# Plot window
RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1

# palette = []

histogram = defaultdict(lambda: 0)
values = {}

for x in range(0, WIDTH):
    for y in range(0, HEIGHT):
        # convert pixels coordinate to comlex number
        c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                    IM_START + (y / HEIGHT) * (IM_END - IM_START))
        # compute the number of iterations
        m = mandelbrot(c)

        values[(x, y)] = m
        if m < MAX_ITER:
            histogram[floor(m)] += 1

total = sum(histogram.values())
hues = []
h = 0

for i in range(MAX_ITER):
    h += histogram[i] / total
    hues.append(h)
hues.append(h)

im = Image.new('HSV', (WIDTH, HEIGHT), (0, 0, 0))
draw = ImageDraw.Draw(im)

for x in range(0, WIDTH):
    for y in range(0, HEIGHT):
        m = values[(x, y)]
        # the color depends on the number of iterations
        hue = 255 - int(255 * linear_interpolation(hues[floor(m)],
                        hues[ceil(m)],
                        m % 1))
        saturation = 255
        value = 255 if m < MAX_ITER else 0
        # plot the point
        draw.point([x, y], (hue, saturation, value))

im.convert('RGB').save('mandelbrot_plot.png', 'PNG')
