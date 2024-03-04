from PIL import Image
import os

def convert_to_jpeg(input_folder,output_folder):
    os.makedirs(output_folder,exist_ok=True)
    files=os.listdir(input_folder)
    print(files)
    
    for file in files:
        input_path=os.path.join(input_folder,file)
        output_path=os.path.join(output_folder,os.path.splitext(file)[0]+'.jpeg')

        try:
            with Image.open(input_path) as img:
                img.convert('RGB').save(output_path,'JPEG')
                print(f"Converted{file} to JPEG")
        except Exception as e:
            print(f"Error converting {file}: {e}")
input_folder="D:\\badriFiles\\6thsem\\ML\\imageDataset\\bar\\needles\\wepng"
output_folder="D:\\badriFiles\\6thsem\ML\\imageDataset\\bar\\needles\\jpegimages"
convert_to_jpeg(input_folder,output_folder)