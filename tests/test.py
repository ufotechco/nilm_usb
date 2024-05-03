from NILM import NILM

nilm = NILM("/Users/juanp/Dev/NILM_IMAGES/output/model.keras")

image_path = "/Users/juanp/Dev/NILM_IMAGES/Test/Fridge_Test/Fridge_Test_2.png"

a, b = nilm.predict(image_path)
print (a, b)