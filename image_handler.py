import base64
import requests
# import io
# import matplotlib.image as mpimg
# from matplotlib import pyplot as plt
# from skimage.io import imsave


def send_image_to_server(filename):
    img_b64 = encode_image_to_b64_string(filename)
    reply = send_b64_string_to_server(img_b64)


def encode_image_to_b64_string(filename):
    with open(filename, "rb") as image_file:
        b64_bytes = base64.b64encode(image_file.read())
    b64_string = str(b64_bytes, encoding='utf-8')
    return b64_string


def send_b64_string_to_server(b64_string):
    out_data = {"image": b64_string, "net_id": "agg24", "id_no": 1}
    r = requests.post("http://vcm-6764.vm.duke.edu/add_image", json=out_data)
    print(r.status_code)
    print(r.text)


if __name__ == '__main__':
    send_image_to_server("Duke_Chapel.jpg")
