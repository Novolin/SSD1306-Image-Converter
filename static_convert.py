from PIL import Image

def choose_output_pixel(pix)->bool:
    '''Outputs a 1 or 0 depending on if a pixel should be on or off'''
    if pix[0] > 128 or pix[1] > 128 or pix[2] > 128: # tweak values once you get more comfortable with this.
        return 1
    return 0

def get_image_bitstream(image_file:str):
    as_px = [] # will be pixel-by-pixel 1s and 0s
    newframe = bytearray() # what we will output
    col_count = 0 # index of the column we're on
    with Image.open(image_file) as img:
        imgdata = list(img.getdata())
        for i in imgdata:
            as_px.append(choose_output_pixel(i))

    while col_count < 1024:
        col_byte = 0 # byte that will hold our column data
        for row in range(8):
            col_byte |= as_px[col_count + (128 * row)] << row
        newframe.append(col_byte)
        col_count += 1
    return newframe


        

test = get_image_bitstream("test.png")
