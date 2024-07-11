import cv2
import pyautogui # 15) to move the mouse cursor
import mediapipe as mp  #to detect hand

cap = cv2.VideoCapture(1)
hand_detector = mp.solutions.hands.Hands()
drawing_utils=mp.solutions.drawing_utils # 7) it will draw the landmarks
screen_width, screen_height = pyautogui.size() # 16) store the whole screen size

# 1) video is a continuous process, so we need to use a while loop
pinky_finger_y = 0 # 20) initializing the distance
while True:
    _ , frame = cap.read()
    # 2) _ will print True
    frame=cv2.flip(frame, 1) # 10)flipping the frame in Y axis, 1 for Y
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)  # 3) changing the frame to rgb frame
    frame_height, frame_width, _ = frame.shape # 12) collecting the frame height, width and channel
    output= hand_detector.process(rgb_frame) # 4) detect the hand in rgb frame
    hands = output.multi_hand_landmarks # 5) to detect the landmarks on a hand

    if hands: # 6) if hand is present
        for hand in hands:
            drawing_utils.draw_landmarks(frame,hand) # 8) it will draw the hand in the frame
            landmarks= hand.landmark

            for index,landmark in enumerate(landmarks): # 11) it will take the id and values of landmarks
                x = int(landmark.x *frame_width)  # 13) to convert the distance in pixel
                y=int(landmark.y *frame_height)

                if index == 8: # 14)draw a circle in 8th landmark
                    cv2.circle(img=frame, center=(x,y),radius=10,color=(255,0,127))
                    pinky_finger_x = screen_width/frame_width * x # 17) convert the position of my finger for the whole screen
                    pinky_finger_y = screen_height/frame_height * y
                    pyautogui.moveTo(pinky_finger_x,pinky_finger_y) # 18) Cursor will move along the whole screen

                if index == 4:  # 19) to click we will use landmark 4(Tip of Thumb) and 8(Tip of Pinky finger)
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(255, 0, 127))
                    thumb_finger_x = screen_width / frame_width * x
                    thumb_finger_y = screen_height / frame_height * y

                    if abs(pinky_finger_y-thumb_finger_y) < 20 :
                        pyautogui.click()
                        pyautogui.sleep(1)

    cv2.imshow("Virtual Mouse",frame)
    cv2.waitKey(1) # 9) will display a frame for 1 ms
