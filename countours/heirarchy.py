import cv2

img = cv2.imread('h_img.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# to get proper edges(not a necesssary step)
edges = cv2.Canny(gray, 10, 50)

#new variable=>hirearchy
contours, hierarchy = cv2.findContours(
    edges,
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

cv2.imshow("Edges Mask", edges)
cv2.imshow("Contours", img)

cv2.waitKey(0)
cv2.destroyAllWindows()