# coding=utf-8
import os, sys
import cv2

# hàm trả về ảnh nhị phân dựa trên ảnh xám (paramater: ảnh xám , ngưỡng ảnh)
def convert_to_binary(img_grayscale, thresh=100):
    # cv2.threshold(hình ảnh, ngưỡng ảnh, giá trị tối đa, kiểu THRESH_BINARY)
    thresh, img_binary = cv2.threshold(img_grayscale, thresh, maxval=255, type=cv2.THRESH_BINARY)
    return img_binary


if __name__ == "__main__":
    assert len(sys.argv) == 2, '[USAGE] $ python ChuyenAnh.py img_5.jpg'
    input_image_path = sys.argv[1]
    img_grayscale = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)

    # ghi lại ảnh xám
    cv2.imwrite('grey_%s' % input_image_path, img_grayscale)
    print('Ảnh xám đã được lưu với tên: grey_%s' % input_image_path)

    # ghi lại ảnh nhị phân bằng hàm đã được định nghĩa
    img_binary = convert_to_binary(img_grayscale, thresh=100)
    cv2.imwrite('binary_%s' % input_image_path, img_binary)
    print('Ảnh nhị phân đã được lưu với tên: binary_%s' % input_image_path)

# Ngưỡng nhị phân là ngưỡng "either or" đơn giản, ở đó các điểm ảnh là 255 hoặc 0
# imread đọc ảnh
# imwrite ghi lại ảnh
# input_image_path: img_5.jpg