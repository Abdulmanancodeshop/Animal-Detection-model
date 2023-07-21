import os
from PIL import Image

data_dir = "E:\\Shared-4060\\AOD\\trainig\\dataset"

# classes = [
#     "Bear", "Brown bear", "Bull", "Butterfly", "Camel", "Canary", "Caterpillar", "Cattle",
#     "Centipede", "Cheetah", "Chicken", "Crab", "Crocodile", "Deer", "Duck", "Eagle",
#     "Elephant", "Fish", "Fox", "Frog", "Giraffe", "Goat", "Goldfish", "Goose", "Hamster",
#     "Harbor seal", "Hedgehog", "Hippopotamus", "Horse", "Jaguar", "Jellyfish", "Kangaroo",
#     "Koala", "Ladybug", "Leopard", "Lion", "Lizard", "Lynx", "Magpie", "Monkey", "Moths and butterflies",
#     "Mouse", "Mule", "Ostrich", "Otter", "Owl", "Panda", "Parrot", "Penguin", "Pig",
#     "Polar bear", "Rabbit", "Raccoon", "Raven", "Red panda", "Rhinoceros", "Scorpion", "Sea lion","Sea turtle"
#     "Seahorse", "Shark", "Sheep", "Shrimp", "Snail", "Snake", "Sparrow", "Spider", "Squid",
#     "Squirrel", "Starfish", "Swan", "Tick", "Tiger", "Tortoise", "Turkey", "Turtle", "Whale",
#     "Woodpecker", "Worm", "Zebra"
# ]

classes = ["Sea turtle", "Seahorse", "Shark", "Sheep", "Shrimp", "Snail", "Snake", "Sparrow", "Spider",
           "Squid", "Squirrel", "Starfish", "Swan", "Tick", "Tiger", "Tortoise", "Turkey", "Turtle",
           "Whale", "Woodpecker", "Worm", "Zebra"]

label_mapping = {label: index + 58 for index, label in enumerate(classes)}
# label_mapping = {label: index for index, label in enumerate(classes)}

for class_name in os.listdir(data_dir):
    class_dir = os.path.join(data_dir, class_name)
    if not os.path.isdir(class_dir):
        continue
    
    label_dir = os.path.join(class_dir, "Label")
    for label_file in os.listdir(label_dir):
        label_path = os.path.join(label_dir, label_file)
        image_path = os.path.join(class_dir, label_file.replace(".txt", ".jpg"))
        
        with open(label_path, "r") as file:
            annotations = file.readlines()
        
        # Read image dimensions
        image = Image.open(image_path)
        img_width, img_height = image.size
        
        updated_annotations = []
        
        for annotation in annotations:
            annotation_parts = annotation.strip().split(" ")
            label = " ".join(annotation_parts[:-4])  # Join the label parts
            
            # Split the remaining parts as before
            x_min, y_min, x_max, y_max = map(float, annotation_parts[-4:])
            
            # Calculate the YOLO format values
            label_index = label_mapping.get(label, -1)
            if label_index == -1:
                continue
            
            width = x_max - x_min
            height = y_max - y_min
            x_center = (x_min + x_max) / 2
            y_center = (y_min + y_max) / 2
            
            # Normalize the values
            x_center /= img_width
            y_center /= img_height
            width /= img_width
            height /= img_height
            
            # Update the annotation in YOLO format
            updated_annotation = f"{label_index} {x_center} {y_center} {width} {height}"
            updated_annotations.append(updated_annotation)
        
        # Write the updated annotations back to the label file
        with open(label_path, "w") as outfile:
            outfile.write("\n".join(updated_annotations))