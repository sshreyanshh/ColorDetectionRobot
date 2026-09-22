import cv2

img = cv2.imread('cont_img.png')

# Original image
cv2.imshow('Original Image', img)

# Grayscale conversion
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", gray)

# Placing windows side by side

# Converting to grayscale for simplicity
# Grayscale pixel values => 0 to 255
# 0 = black, 255 = white

#creation of binary mask
_, mask = cv2.threshold(
    gray,                #name of the image paasing
    80,                  # threshold value 
    255,                 # end pixel value(higher limit)
    cv2.THRESH_BINARY    #thresholding type, here binary 
)
#0-80=>0=>black
#80-255=>255=>white
#dash coz we dont want the first returned value which is threshold val
cv2.imshow("binary mask", mask)
cv2.moveWindow("Original Image", 0, 100)
cv2.moveWindow("Grayscale Image", 500, 100)
cv2.moveWindow("binary mask",500, 100 )
cv2.waitKey(0)
cv2.destroyAllWindows()

#finding contours
#dash eliminating hireacrhy 
contours, _ = cv2.findContours(
    mask,
    cv2.RETR_EXTERNAL, #tells opencv to take only external contours
    cv2.CHAIN_APPROX_SIMPLE #removes noise/unnecessary points
)
#will return list of countours detected
print()
print("Number of contours:", len(contours))

# Process every contour
for contour in contours:

    area = cv2.contourArea(contour)

    print("Area:", area)

    # Ignore small regions
    if area > 100:

        cv2.drawContours(
            img,#image
            [contour],#list of countours
            -1,#index after which you gotta start the drwaing
            (0, 255, 0),#color
            3#width
        )

cv2.imshow("Contours", img)

cv2.waitKey(0)
cv2.destroyAllWindows()