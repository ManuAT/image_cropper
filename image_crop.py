from PIL import Image,ImageDraw,ImageFont
import imagehash
import image_slicer

tiles =  image_slicer.slice('levels/level0.png', 49,save=False)

# we have 5 component so needed to check all of it(;)

hash1 = imagehash.average_hash(Image.open("comp/solid2_2.png"))
hash2 = imagehash.average_hash(Image.open("comp/empty2_2.png"))
hash3 = imagehash.average_hash(Image.open("comp/player2_2.png"))
hash4 = imagehash.average_hash(Image.open("comp/crate2_2.png"))
hash5 = imagehash.average_hash(Image.open("comp/target2_2.png"))

cutoff = 10  # maximum bits that could be different between the hashes.
# string
for tile in tiles:
    hash0 = imagehash.average_hash(tile.image) 
    #soild aka walls
    # print(tile.number)
    if hash0 - hash1 < cutoff:
        print('#', end="")
    elif hash0 - hash2 < cutoff:
        print(' ', end="")
    elif hash0 - hash3 < cutoff:
        print('P', end="")
    elif hash0 - hash4 < cutoff:
        print('B', end="")
    elif hash0 - hash5 < cutoff:
        print('*', end="")
    
    if tile.number%7 == 0:
        print()






# https://stackoverflow.com/questions/52736154/how-to-check-similarity-of-two-images-that-have-different-pixelization

# https://stackoverflow.com/questions/5953373/how-to-split-image-into-multiple-pieces-in-python

# https://image-slicer.readthedocs.io/en/latest/examples.html

# https://stackoverflow.com/questions/58468944/image-object-has-no-attribute-read