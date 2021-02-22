from PIL import Image
import os
import random


# Read the two images

def create_puzzle(image1_path, image2_path, image3_path, image4_path, dest_name):

    image1 = Image.open(f"images/people/{image1_path}").convert("RGB")
    image2 = Image.open(f"images/people/{image2_path}").convert("RGB")
    image3 = Image.open(f"images/people/{image3_path}").convert("RGB")
    image4 = Image.open(f"images/people/{image4_path}").convert("RGB")
    image1_size = image1.size
    image2_size = image2.size
    image3_size = image3.size
    image4_size = image4.size
    image2.resize((image1_size[0], image1_size[1]))
    image3.resize((image1_size[0], image1_size[1]))
    image4.resize((image1_size[0], image1_size[1]))
    new_image = image1
    current = 0
    increment = 10
    while current < image1_size[0]:
        region = image2.crop((current, 0, current + increment, image2_size[1]))
        new_image.paste(region, (current, 0))
        current += increment * 4
    current = increment
    while current < image1_size[0]:
        region = image3.crop((current, 0, current + increment, image3_size[1]))
        new_image.paste(region, (current, 0))
        current += increment * 4
    current = increment * 2
    while current < image1_size[0]:
        region = image4.crop((current, 0, current + increment, image4_size[1]))
        new_image.paste(region, (current, 0))
        current += increment * 4

    new_image.convert('RGB').save(f"images/dest/{dest_name}.jpg", "JPEG")
    new_image.show()


if __name__ == "__main__":
    onlyimages = [f for f in os.listdir("images/people") if f.endswith(".jpg")]
    image1, image2, image3, image4 = random.sample(onlyimages, 4)
    create_puzzle(image1, image2, image3, image4, f"{image1}-{image2}-{image3}-{image4}")
