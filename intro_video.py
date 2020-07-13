import cv2

cap = cv2.VideoCapture(0)

# save the video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))  # 20.0 is frames per sec

while cap.isOpened():

    ret, frame = cap.read()

    # if true
    if ret:

        # method to get width and height of video
        print('width = ',cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print('height = ',cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        cv2.imshow('video', frame)

        # variable to change from colored to gray
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        key = cv2.waitKey(1)

        # if key == ord('g'):
        #     cv2.destroyWindow('video')
        #     cv2.imshow('gray_video', gray)

        out.write(frame)

        if key == ord('q'):
            cap.release()
            out.release()
            cv2.destroyAllWindows()


    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
