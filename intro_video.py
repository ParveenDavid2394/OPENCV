import cv2

cap = cv2.VideoCapture(0)

# save the video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():

    ret, frame = cap.read()

    if ret:

        cv2.imshow('video', frame)

        # variable to change from colored to gray
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        key = cv2.waitKey(1)

        # if key == ord('g'):
        #     cv2.destroyWindow('video')
        #     cv2.imshow('gray_video', gray)

        out.write(frame)

        if key == 27:
            break

cap.release()
out.release()
cv2.destroyAllWindows()