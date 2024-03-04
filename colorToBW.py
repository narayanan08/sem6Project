from PIL import Image
import os

def convert_to_black_and_white(input_image_folder,output_image_folder):
    imageFiles=os.listdir(input_image_folder)
    print(imageFiles)
    threshold=128
    for imageFile in imageFiles:
        input_image_path=input_image_folder+"\\"+imageFile
        print(input_image_path)
        original_image=Image.open(input_image_path)
        black_and_white_image=original_image.convert(mode="L")
        black_and_white_image=black_and_white_image.point(lambda x:0 if x<threshold else 255)
        output_image_path=output_image_folder+"\\"+imageFile
        black_and_white_image.save(output_image_path)

input_path="D:\\badriFiles\\6thsem\\ML\\imageDataset\\bars\\colorImages"
output_path="D:\\badriFiles\\6thsem\\ML\\imageDataset\\bars\\bwImages"
convert_to_black_and_white(input_path,output_path)

"D:\badriFiles\6thsem\ML\imageDataset\programs"