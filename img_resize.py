from PIL import Image

for i in range(1,208):
    try:
        img=Image.open("./rat_images/%s.jpg"%(i))
        img=img.resize((480,480))
        img.save("./new_rat/%s.jpg"%(i))
    except:
        print("Skipped ",i)
        continue
