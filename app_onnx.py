import cv2
import serial
from serial.tools import list_ports
import numpy as np
from ultralytics import YOLO

# YOLO 모델 로드
model = YOLO('yolo/weights/best.onnx')

def find_arduino_port():
    ports = list_ports.comports()
    for port in ports:
        if 'Arduino' in port.description:
            return port.device
    raise Exception("아두이노 포트를 찾을 수 없습니다.")

def setup_arduino():
    try:
        arduino_port = find_arduino_port()
        baud_rate = 9600
        return serial.Serial(arduino_port, baud_rate)
    except Exception as e:
        print(e)
        exit()

def process_frame(frame, model):
    # 프레임이 유효한지 검사
    if frame is None or frame.size == 0:
        print("유효하지 않은 프레임입니다.")
        return np.array([])
    
    # 추론 수행
    results = model(frame)
    boxes = results[0].boxes.data.cpu().numpy()
    return boxes

def main():
    # arduino = setup_arduino()
    
    cap = cv2.VideoCapture(0) 
    
    if not cap.isOpened():
        print("카메라를 열 수 없습니다.")
        exit()
    
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    ret, test_frame = cap.read()
    if not ret or test_frame is None:
        print("ERROR: Failed to initialize camera stream")
        cap.release()
        exit()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("ERROR: Failed to capture frame")
            break

        boxes = process_frame(frame, model)
        
        if len(boxes) == 0:
            helmet_detected = False
        else:
            helmet_detected = np.any(boxes[:, 5] == 0)

        for box in boxes:
            x1, y1, x2, y2, conf, cls = box
            color = (0, 255, 0) if int(cls) == 0 else (0, 0, 255)
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)

        if helmet_detected:
            print("INFO: Helmet detected")
            # arduino.write(b'O')
        else:
            print("WARNING: No helmet detected")
            # arduino.write(b'X')

        cv2.imshow("Helmet Detection", frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    # arduino.close()

if __name__ == "__main__":
    main()