from collections import Counter
from PIL import Image

file = "classified_cbc.enc"
block = 16
header = 16

width = 432
height = 475


with open(file, "rb") as f:
    data = f.read()


# remove OpenSSL header and salt
ciphertext = data[header:]


# split ciphertext into 16 byte AES blocks
blocks = [ciphertext[i:i + block]for i in range(0, len(ciphertext), block)if len(ciphertext[i:i + block]) == block]

# count identical blocks
counts = Counter(blocks)


# assign the same grayscale value to identical blocks
unique_blocks = list(dict.fromkeys(blocks))
shade_map = {}

for i, block in enumerate(unique_blocks):

    if len(unique_blocks) == 1:
        shade = 0
    else:
        shade = int(i * 255 / (len(unique_blocks) - 1))

    shade_map[block] = shade


# reconstruct visualization
pixels = []

for block in blocks:
    shade = shade_map[block]
    pixels.extend([shade] * 16)


# remove AES padding
pixels = pixels[:width * height]


# create grayscale image
img = Image.new("L", (width, height))
img.putdata(pixels)

img.save("pattern_cbc.png")
print("Saved as pattern_cbc.png")