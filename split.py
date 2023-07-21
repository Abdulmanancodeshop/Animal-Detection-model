import os
import random
import shutil

data_dir = "E:\\Shared-4060\\AOD\\trainig\\clean"
output_dir = "E:\\Shared-4060\\AOD\\trainig\\dataset_split_new"

train_output_dir = os.path.join(output_dir, "train")
train_images_dir = os.path.join(train_output_dir, "images")
train_labels_dir = os.path.join(train_output_dir, "labels")

val_output_dir = os.path.join(output_dir, "val")
val_images_dir = os.path.join(val_output_dir, "images")
val_labels_dir = os.path.join(val_output_dir, "labels")

# Create output directories
os.makedirs(train_images_dir, exist_ok=True)
os.makedirs(train_labels_dir, exist_ok=True)
os.makedirs(val_images_dir, exist_ok=True)
os.makedirs(val_labels_dir, exist_ok=True)

# Iterate over classes
for class_name in os.listdir(data_dir):
    class_dir = os.path.join(data_dir, class_name)
    if not os.path.isdir(class_dir):
        continue
    
    # Get list of image files
    image_files = os.listdir(class_dir)
    random.shuffle(image_files)  # Shuffle the file list
    num_images = len(image_files)
    num_train = int(0.8 * num_images)  # 80% for training
    
    train_files = image_files[:num_train]
    val_files = image_files[num_train:]
    
    # Move training images and labels
    for file in train_files:
        image_src = os.path.join(class_dir, file)
        label_src = os.path.join(class_dir, "Label", file.replace(".jpg", ".txt"))
        
        image_dest = os.path.join(train_images_dir, file)
        label_dest = os.path.join(train_labels_dir, file.replace(".jpg", ".txt"))
        
        # Get the class name dynamically
        class_name = os.path.basename(class_dir)
        
        # Skip the file if the label path is specific value
        if label_src == os.path.join(data_dir, class_name, "Label", "Label"):
            continue
        
        shutil.copyfile(image_src, image_dest)
        shutil.copyfile(label_src, label_dest)
    
    # Move validation images and labels
    for file in val_files:
        image_src = os.path.join(class_dir, file)
        label_src = os.path.join(class_dir, "Label", file.replace(".jpg", ".txt"))
        
        image_dest = os.path.join(val_images_dir, file)
        label_dest = os.path.join(val_labels_dir, file.replace(".jpg", ".txt"))
        
        # Get the class name dynamically
        class_name = os.path.basename(class_dir)
        
        # Skip the file if the label path is specific value
        if label_src == os.path.join(data_dir, class_name, "Label", "Label"):
            continue
        
        shutil.copyfile(image_src, image_dest)
        shutil.copyfile(label_src, label_dest)
