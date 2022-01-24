import cv2
import numpy as np
img = cv2.imread("/home/mahesh/Pictures/funnel 2/Screenshot from 2022-01-09 09-34-36.png")
h, w, c = img.shape

# create zeros mask 2 pixels larger in each dimension
mask = np.zeros([h + 2, w + 2], np.uint8)

# do floodfill
result = img.copy()
cv2.floodFill(result, mask, (0,0), (0,0,0), (3,151,65), (3,151,65), flags=8)
cv2.floodFill(result, mask, (38,313), (0,0,0), (3,151,65), (3,151,65), flags=8)
cv2.floodFill(result, mask, (363,345), (0,0,0), (3,151,65), (3,151,65), flags=8)
cv2.floodFill(result, mask, (619,342), (0,0,0), (3,151,65), (3,151,65), flags=8)

# write result to disk
cv2.imwrite("soccer_floodfill.jpg", result)

# display it
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()