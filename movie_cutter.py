import cv2

cap = cv2.VideoCapture('./binary/issue解決.mp4')

cap_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
cap_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
writer = cv2.VideoWriter('one_minutes.mp4', fourcc, fps, (cap_width, cap_height))

begin = 11
end = 21
for i in range(end * fps):
    ret, frame = cap.read()
    if ret:
        if begin * fps < i:
            writer.write(frame)
