import os

def rename_image_files(directory):
    count=1
    for filename in os.listdir(directory):
        # Specify the full path of the file
        old_path = os.path.join(directory, filename)
        
        # Split the filename and extension
        name, extension = os.path.splitext(filename)
        
        # Check if the file is an image (you can add more extensions as needed)
        if extension.lower() in ['.jpg', '.jpeg', '.png', '.gif','.webp']:
            # Specify the new name for the file
            new_name = str(count)+extension
            count+=1
            # Specify the full path of the new file
            new_path = os.path.join(directory, new_name)
            
            # Rename the file
            if new_path!=old_path:
                os.rename(old_path, new_path)
            print(f"Renamed {filename} to {new_name}")

# Example usage:
directory = r"D:\badriFiles\6thsem\ML\imageDataset\mangalsutra\colorImages"
rename_image_files(directory)

