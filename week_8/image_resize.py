import PIL
import os 
from PIL import Image
def Size(img):
    wid, hgt = img.size
    print(str(wid)+ "X" +str(hgt))
    
# img = PIL.Image.open("C:\\Users\\ishup\\OneDrive\\Desktop\\Guru Charan Sir\\python-exercises\\week_8\\images\\42.jpg")
# Size(img)

# img_resized = img.resize((500, 500))
# img1 = 'C:\\Users\\ishup\\OneDrive\\Desktop\\Guru Charan Sir\\python-exercises\\week_8\\image_resized\\aamir1.jpg'
# img_resized.save(img1)
# Size(PIL.Image.open(img1))



def list_files_in_folder(folder_path):
    try:
        # Get the list of all files and directories
        files = os.listdir(folder_path)
        
        print(f"Files in '{folder_path}':")
        i=1
        for file in files:
            print(file)
            image_path = folder_path + "\\" + file
            img = PIL.Image.open(image_path)
            img_resized = img.resize((500, 500))
            img1 = 'C:\\Users\\ishup\\OneDrive\\Desktop\\Guru Charan Sir\\python-exercises\\week_8\\image_resized\\aamir'+str(i)+'.jpg'
            img_resized.save(img1)
            Size(PIL.Image.open(img1))
            i=i+1
    except FileNotFoundError:
        print(f"The folder '{folder_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
        

folder_path = "C:\\Users\\ishup\\OneDrive\\Desktop\\Guru Charan Sir\\python-exercises\\week_8\\images"
list_files_in_folder(folder_path)