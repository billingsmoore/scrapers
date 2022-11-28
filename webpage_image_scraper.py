import requests
from bs4 import BeautifulSoup
import shutil
import os

# get specifications
url = input("Enter url for scraping: ")
dir_name = input("Enter desired folder name: ")
file_name = input("Enter desired filename: ")
num_of_images = int(input("Enter number of desired images: "))

# get page info
page = requests.get(url)
html = BeautifulSoup(page.content, 'html.parser')

# print connection status
print("status code: " + str(page))
print("connected to: " + str(page.url))


# get image data from webpage
images = html.select('img')
    
#download images
img_number = 0
os.mkdir(dir_name)
while img_number < num_of_images:
    url = images[img_number].get('src') # get image source

    curr_file_name = file_name+str(img_number) # update file name
    
    res = requests.get(url, stream=True)
    
    if res.status_code  == 200: # ensure successful connection and download
        with open(dir_name+'/'+curr_file_name, 'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image successfully Downloaded: ', curr_file_name)
    else:
        print("Image couldn't be retrieved.")
    
    img_number += 1