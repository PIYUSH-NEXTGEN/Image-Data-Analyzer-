# Basic Setup -
import pandas
import  os
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
    return {
        'red_mean': r.mean(),
        'red_std': r.std(),
        'red_min': r.min(),
        'red_max': r.max(),

        'green_mean': g.mean(),
        'green_std': g.std(),
        'green_min': g.min(),
        'green_max': g.max(),

        'blue_mean': b.mean(),
        'blue_std': b.std(),
        'blue_min': b.min(),
        'blue_max': b.max()
    }


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
    return {
        f'{channel_name.lower()}_dark_pct': dark/total*100,
        f'{channel_name.lower()}_mid_pct': mid/total*100,
        f'{channel_name.lower()}_bright_pct': bright/total*100
    }

# Store results
results = []
folder_path = "images"
if not os.path.exists(folder_path):
    print("Folder not found.")
    exit()
image_files = [
    f for f in os.listdir(folder_path)
    if f.lower().endswith((".png", ".jpg", ".jpeg"))
]
for img_name in image_files:
    img_path = os.path.join(folder_path, img_name)

    arr = image_stats(img_path, img_name)
    ch_stats = channel_stats(arr, img_name)

    # Get histogram data for each channel
    r_hist = histogram(arr[:, :, 0], 'Red')
    g_hist = histogram(arr[:, :, 1], 'Green')
    b_hist = histogram(arr[:, :, 2], 'Blue')

    # Collect data
    result_dict = {
        'filename': img_name,
        'mean_brightness': arr.mean(),
        'shape': arr.shape,
        'dtype': arr.dtype,
        'std': arr.std(),
        'min': arr.min(),
        'max': arr.max(),
    }

    #Add channel stats
    result_dict.update(ch_stats)

    # Add histogram data
    result_dict.update(r_hist)
    result_dict.update(g_hist)
    result_dict.update(b_hist)

    results.append(result_dict)

# Create DataFrame and save
df = pandas.DataFrame(results)
df.to_csv('image_results.csv', index=False)

# brightest and darkest
brightest = df.loc[df['mean_brightness'].idxmax()]
darkest = df.loc[df['mean_brightness'].idxmin()]

print("=" * 50)
print(f"Brightest Image: {brightest['filename']} (Brightness: {brightest['mean_brightness']:.2f})")
print(f"Darkest Image: {darkest['filename']} (Brightness: {darkest['mean_brightness']:.2f})")
print(f"\nResults saved to 'image_results.csv'")