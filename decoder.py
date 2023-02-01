from PIL import Image

img=Image.open('obrsospr.png')
pixx=img.load()

def img_to_bin(img):
    bin_msg=[]
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            pixel=pixx[j, i]
            pix_blue=pixel[2]
            bin_blue=bin(pix_blue)[-1]
            bin_msg.append(bin_blue)
    return bin_msg

def real_bin(img:list):
    bin=img_to_bin(img)
    bin_msg=[]
    bin_cis=''
    for i in range(len(bin)//8):
        for j in range(8):
            bin_cis += bin[8*i+j]
        bin_msg.append(bin_cis)
        bin_num = ''
    return bin_msg

def message(binary:list):
    msg_list=real_bin(binary)
    msg=''
    pismeno=''
    for i in msg_list:
        if pismeno != '#':
            ord=int(i,2)
            pismeno=chr(ord)
            msg+=pismeno
        else:
            break
    print(msg)
message(img)
