from sense_hat import SenseHat
import random

sense = SenseHat()

text_colour = (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))

rgb = random.randrange(0, 256)
back_colour = (rgb, rgb, rgb)

while True:
    sense.show_message("Spider Bot!", text_colour=text_colour, back_colour=back_colour, scroll_speed=0.05)
    text_colour = (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
    back_colour = (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))