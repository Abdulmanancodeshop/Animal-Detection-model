import os

def rename_images_and_labels(root_dir, category):
    category_dir = os.path.join(root_dir, category)
    if os.path.isdir(category_dir):
        image_dir = os.path.join(category_dir)
        label_dir = os.path.join(category_dir, 'Label')

        if not os.path.exists(image_dir) or not os.path.exists(label_dir):
            return

        image_files = os.listdir(image_dir)
        label_files = os.listdir(label_dir)

      


        for i, (image_file, label_file) in enumerate(zip(image_files, label_files), start=1):
            image_name, image_ext = os.path.splitext(image_file)
            new_image_name = f"{category}_{i}{image_ext}"
            new_image_path = os.path.join(image_dir, new_image_name)
            old_image_path = os.path.join(image_dir, image_file)

            try:
                os.rename(old_image_path, new_image_path)
            except Exception as e:
                print(f"Error occurred while renaming image '{image_file}': {e}")

            label_name, label_ext = os.path.splitext(label_file)
            new_label_name = f"{category}_{i}{label_ext}"
            new_label_path = os.path.join(label_dir, new_label_name)
            old_label_path = os.path.join(label_dir, label_file)

            try:
                os.rename(old_label_path, new_label_path)
            except Exception as e:
                print(f"Error occurred while renaming label '{label_file}': {e}")

# Example usage
root_directory = "E:\\Shared-4060\\AOD\\trainig\\dataset"
category_name = "Cheetah"
rename_images_and_labels(root_directory, category_name)
