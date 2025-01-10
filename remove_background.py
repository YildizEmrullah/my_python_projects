from rembg import remove
# firstly you have to install remb and import remove
# and then choose a jpg file for the transformation
input_path = "lion.jpg"
output_path = "output.png"

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input_file = i.read()
        output_file = remove(input_file)
        o.write(output_file)
