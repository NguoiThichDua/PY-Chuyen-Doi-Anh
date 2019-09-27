# goi thu vien cv2
import cv2

# ham chuyen anh nhi phan tu anh xam
def convert_to_binary(img_grayscale, thresh):
    # threshold(anh_xam, nguong_anh, maxvalue, type)
    thresh, img_binary = cv2.threshold(img_grayscale, thresh, maxval=255, type=cv2.THRESH_BINARY)
    return img_binary


if __name__ == "__main__":
    # doc anh va chuyen thanh anh xam
    img_grayscale = cv2.imread('Son.jpg', cv2.IMREAD_GRAYSCALE)

    # luu anh xam
    cv2.imwrite('AnhXam_Son.jpg', img_grayscale)
    print('Anh xam da duoc luu')

    # luu anh quang pho
    #hsv_img = cv2.cvtColor(cv2.imread('Son.jpg',1), cv2.COLOR_BGR2HSV)
    #cv2.imwrite('AnhQuangPho_Son.jpg', hsv_img)
    #print('Anh quang pho da duoc luu')

    # luu anh nhi phan tu anh xam
    img_binary = convert_to_binary(img_grayscale, 100)
    cv2.imwrite('AnhNhiPhan_Son.jpg', img_binary)
    print('Anh nhi phan da duoc luu')