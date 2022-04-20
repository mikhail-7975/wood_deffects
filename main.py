import cv2
import time
#
# stitcher = cv2.Stitcher_create()
# foo = cv2.imread("1.png")
# bar = cv2.imread("1.png")
# result = stitcher.stitch((foo,bar))
#
# cv2.imwrite("result11.jpg", result[1])


# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture('sample.mp4')

# Check if camera opened successfully
if (cap.isOpened()== False):
  print("Error opening video stream or file")

result = None

stitcher = cv2.Stitcher_create()
while cap.isOpened():
    ret, frame = cap.read()
    if frame.mean() > 127:
        result = frame.copy()
        print("start")
        time.sleep(1)
        print(".")
        break

ret, frame = cap.read()
frame_prev = frame.copy()

# Read until video is completed
while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:
        # Display the resulting frame
        print((frame - frame_prev).mean())
        if (frame - frame_prev).mean() > 83:

            frame_prev = frame.copy()
            # time.sleep(1)
            print(frame.shape, result.shape)
            _, s = stitcher.stitch((result, frame))
            # print(s)
            # if s:
            if not _:
                result = s.copy()
            # if stitched:
            #     print(stitched.shape)
            #     result = stitched.copy()
        cv2.imshow('result',result)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

  # Break the loop
    else:
        break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()