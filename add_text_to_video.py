import cv2
import datetime

cap = cv2.VideoCapture(0)

# default frame width and height
print('width = ', cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print('height = ', cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# set frame width and height
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

# checking frame width and height after setup
print('width = ', cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print('height = ', cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while cap.isOpened():
    ret, frame = cap.read()

    if ret:

        # add datetime on frame
        datet = str(datetime.datetime.now())

        # add frame width and height on frame

        font = cv2.FONT_HERSHEY_COMPLEX
        text = 'Width:{0} Height:{1}'.format(cap.get(cv2.CAP_PROP_FRAME_WIDTH),cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        frame = cv2.putText(frame, datet, (10,50), font, 1, (255,255,255), 1, cv2.LINE_AA)
        frame = cv2.putText(frame, text, (10, 100), font, 1, (255, 255, 255), 1, cv2.LINE_AA)

        cv2.imshow('video',frame)
        k = cv2.waitKey(1)

        if k == ord('q'):
            cap.release()
            cv2.destroyAllWindows()

    else:
        break

cap.release()
cv2.destroyAllWindows()