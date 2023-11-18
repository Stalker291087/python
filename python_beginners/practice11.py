prism_lenght = int(input("Please type the lenght: "))
prism_width = int(input("Please type the width: "))
prism_height = int(input("Please type the height: "))

def calculateVolume(lenght, width, height):
    result = lenght * width *height
    return str(result)


print("The volume of the rectangular prism is " + calculateVolume(prism_lenght, prism_width, prism_height) + " cubic feet.")
