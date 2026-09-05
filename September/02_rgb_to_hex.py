import re

def rgb_to_hex(rgb):
    r, g, b = map(int, rgb.strip('rgb()').split(','))
    return f'#{r:02x}{g:02x}{b:02x}'

print(rgb_to_hex('rgb(255, 255, 255)'))