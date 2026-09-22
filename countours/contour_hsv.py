import cv2
img = cv2.imread('cont_img.png')
# Convert BGR image to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define the color range you want to detect
lower = (100, 100, 100)
upper = (130, 255, 255)
# Create mask
mask = cv2.inRange(hsv, lower, upper)

cv2.imshow("Mask", mask)
contours, hierarchy = cv2.findContours(
    mask,
    cv2.RETR_TREE,
    cv2.CHAIN_APPROX_SIMPLE
)
print("Number of contours:", len(contours))
cv2.drawContours(
    img,
    contours,
    -1,
    (0, 255, 0),
    2
)
cv2.imshow("Contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()