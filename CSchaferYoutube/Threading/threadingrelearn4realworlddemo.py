# thread relearn 4

# for the real world application

# say i wanna download different HD images at the same time


import requests
import time
import concurrent.futures


"""
img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]
"""
img_urls = [
    'https://imgs.aixifan.com/newUpload/684889_1630185554600',
    'https://imgs.aixifan.com/newUpload/684889_1630184816427',
    'https://imgs.aixifan.com/newUpload/13781504_1630163682277',
    'https://imgs.aixifan.com/newUpload/13781504_1630163683707',
    'https://imgs.aixifan.com/newUpload/13781504_1630163685279',
    'https://imgs.aixifan.com/newUpload/13781504_1630163779059',
    'https://imgs.aixifan.com/newUpload/13781504_1630163781772',
    'https://imgs.aixifan.com/newUpload/13781504_1630163839349',
    'https://imgs.aixifan.com/newUpload/13781504_1630163840599',
    'https://imgs.aixifan.com/newUpload/13781504_1630163780476',
    'https://imgs.aixifan.com/newUpload/13781504_1630163837783',
    'https://imgs.aixifan.com/newUpload/13781504_1630163955678',
    'https://imgs.aixifan.com/newUpload/13781504_1630163955678'
]

t1 = time.perf_counter()


def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[4]
    img_name = f'{img_name}.jpg'
    with open (img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print (f'{img_name} was downloaded...')


with concurrent.futures.ThreadPoolExecutor () as executor:
    executor.map(download_image, img_urls)


t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')



