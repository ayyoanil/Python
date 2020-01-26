from PIL import Image

test_image1 = Image.open("img.jpg").convert('RGB')
test_image2 = Image.open("new.jpg").convert('RGB')

r1, g1, b1 = test_image1.split()
r2, g2, b2 = test_image2.split()

new_img = Image.merge('RGB', (r2, g1, b2))
new_img.show()

#new_img1 = test_image1.convert('P')
#new_img1.show()

