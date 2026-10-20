from collections import Counter
from PIL import Image

file = "classified.enc"
block = 16
header = 16  # the 8 bytes "Salted__" + 8 bytes of the actual salt
width = 432
height = 475

with open(file, "rb") as f:
    data = f.read()

# removing the OpenSSL header and salt
ciphertext = data[header:]

# split ciphertext into 16 byte blocks
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
        # getting the shade in range 0 to 255
        shade = int(i * 255 / (len(unique_blocks) - 1))

    shade_map[block] = shade


# reconstruct the pattern
pixels = []

for block in blocks:
    shade = shade_map[block]

    # same shade for the 16 bytes of this block
    pixels.extend([shade] * 16)


# remove the AES padding at the end
# original image contains exactly 432 * 475 pixels
pixels = pixels[:width * height]

# create the grayscale image
img = Image.new("L", (width, height))
img.putdata(pixels)


img.save("pattern_ecb.png")
print("Saved as pattern_ecb.png")