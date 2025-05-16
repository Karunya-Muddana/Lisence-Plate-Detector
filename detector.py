import cv2

img_path = input("Please provide the file name --> ")

image = cv2.imread(img_path)
if image is None:
    print("Error: Could not open or find the image.")
    exit()

grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(grey, 50, 150)  

contours, _ = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contour_image = image.copy()

plate_found = False
best_plate = None
max_area = 0
best_approx = None

for cnt in contours:
    epsilon = 0.02 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    
    if len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = w / float(h)
        area = cv2.contourArea(cnt)

        if 1.5 < aspect_ratio < 6 and w > 50 and h > 15 and area > max_area:
            height, width = image.shape[:2]
            if x >= 0 and y >= 0 and (x + w) <= width and (y + h) <= height:
                best_plate = image[y:y + h, x:x + w]
                max_area = area
                best_approx = approx

if best_plate is not None:
    cv2.drawContours(contour_image, [best_approx], -1, (0, 255, 0), 3)
    cv2.imshow("Possible Plate", best_plate)
    plate_found = True
else:
    print("No license plate detected.")

cv2.imshow("Contours", contour_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
