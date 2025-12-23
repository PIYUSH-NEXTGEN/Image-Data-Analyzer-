# Basic Setup -
from PIL import Image
import numpy as np

#Image Stats -
def image_stats(path, image_num):

    image = Image.open(path)

    # Checking if originally grayscale -
    if image.mode == 'L' :
        print(f"{image_num}")

    image = image.convert("RGB")
    arr = np.array(image)

    # Image stats -
    print(f"Shape     {image_num}: {arr.shape}")
    print(f"Data type {image_num}: {arr.dtype}")
    print(f"Mean      {image_num}: {arr.mean()}")
    print(f"Std       {image_num}: {arr.std()}")
    print(f"Minimum   {image_num}: {arr.min()}")
    print(f"Maximum   {image_num}: {arr.max()}\n")
    return arr

#Channel Stats -
def channel_stats(arr, image_num):

    hist,bins = np.histogram(arr.flatten(),bins=256,range=(0,256))
    r = arr[:, :, 0]
    g = arr[:, :, 1]
    b = arr[:, :, 2]

    print(f"{image_num} Channel Statistics:")
    print(f"  Red   - Mean: {r.mean():6.2f}, Std: {r.std():6.2f}, Min: {r.min():3d}, Max: {r.max():3d}")
    print(f"  Green - Mean: {g.mean():6.2f}, Std: {g.std():6.2f}, Min: {g.min():3d}, Max: {g.max():3d}")
    print(f"  Blue  - Mean: {b.mean():6.2f}, Std: {b.std():6.2f}, Min: {b.min():3d}, Max: {b.max():3d}\n")


#Histogram -
def histogram(channel,channel_name):
    hist,bins = np.histogram(channel,bins=256,range=(0,256))

    dark = hist[0:85].sum()
    mid = hist[85:170].sum()
    bright = hist[170:256].sum()
    total = channel.size

    print(f"{channel_name} Channel Histogram:")
    print(f"Dark:   {dark/total*100:5.1f}%")
    print(f"Mid:    {mid/total*100:5.1f}%")
    print(f"Bright: {bright/total*100:5.1f}%\n")

#Loading images -
arr1 = image_stats("luffy.png", "(luffy.png)")
arr2 = image_stats("rainbow.png", "(rainbow.png)")

#Channel Stats -
channel_stats(arr1,"(luffy.png)")
channel_stats(arr2,"(rainbow.png)")

#Brightness -
brightness1 = arr1.mean()
brightness2 = arr2.mean()

if brightness1 > brightness2 :
    print("luffy.png is brighter\n")
else :
    print("rainbow.png is brighter\n")

#Histogram -
histogram(arr1,"luffy.png")
histogram(arr2,"rainbow.png")

'''MORE STUFFS COMING'''
