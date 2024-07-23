import cv2

def test_camera(device):
    cap = cv2.VideoCapture(device)
    if not cap.isOpened():
        print(f"No se puede abrir el dispositivo de video: {device}")
        return

    print(f"Dispositivo de video {device} abierto correctamente")

    while True:
        ret, frame = cap.read()
        if not ret:
            print(f"No se puede recibir la imagen del dispositivo de video: {device}")
            break

        cv2.imshow(f'Dispositivo de video {device}', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

for i in range(10):
    test_camera(f"/dev/video{i}")
    print(i)
