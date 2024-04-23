import cv2


image1 = cv2.imread("./no padding/anomaly_3.png")
image2 = cv2.imread("./with padding/anomaly_3.png")

if image1.shape[0] != image2.shape[0]:
    print("can not")
    exit()
else:

    combined_image = cv2.hconcat([image1, image2])


    cv2.imshow("Combined Image", combined_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
