from PIL import Image

person = Image.open('person.jpg')
person_pix = person.load()
background = Image.open('background.jpg')
background_pix = background.load()
print(person_pix[0,0])
print(person.size)
print(background.size)

for y in range(375):
    for x in range(640):
        if not all(abs(val - ref) <= 68 for val, ref in zip(person_pix[x, y], (118, 218, 148))):
            background_pix[x, y] = person_pix[x, y]

background.save(r"C:\Users\Ryan\Desktop\tungtungtung.png")