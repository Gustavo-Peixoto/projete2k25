import cv2
import numpy as np

def processar_imagem(img_bytes):
    img_array = np.frombuffer(img_bytes, dtype=np.uint8)
    imagem = cv2.imdecode(img_array, cv2.IMREAD_COLOR)  # Corrigido: BGR

    imagem = cv2.resize(imagem, (400, 400))

    # Remove tons de azul com HSV
    hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([115, 30, 50])
    upper_blue = np.array([125, 160, 255])
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

    # Limpeza da máscara
    kernel_small = np.ones((3, 3), np.uint8)
    mask_clean = cv2.morphologyEx(mask_blue, cv2.MORPH_OPEN, kernel_small)

    # Dilatação para garantir remoção completa
    kernel_large = np.ones((5, 5), np.uint8)
    mask_dilated = cv2.dilate(mask_clean, kernel_large, iterations=2)

    # Remove azul da imagem original
    imagem_sem_azul = cv2.inpaint(imagem, mask_dilated, 3, cv2.INPAINT_TELEA)

    # Pré-processamento: grayscale + blur
    gray = cv2.cvtColor(imagem_sem_azul, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)

    # Detecção de bordas
    canny = cv2.Canny(blur, threshold1=100, threshold2=200)

    # Fechamento morfológico para unir bordas
    kernel_close = np.ones((3, 3), np.uint8)
    dilated = cv2.dilate(canny, kernel_close, iterations=1)
    closed = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel_close)

    # Detecção de contornos na imagem já dilatada
    contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Cria imagem apenas com círculos válidos desenhados
    resultado_circulos = imagem_sem_azul.copy()

    for cnt in contours:
        area = cv2.contourArea(cnt)
        perimeter = cv2.arcLength(cnt, True)

        if perimeter == 0:
            continue

        circularity = 4 * np.pi * (area / (perimeter * perimeter))

        # Filtra apenas contornos quase circulares e com área adequada
        if 0.5 < circularity <= 2 and area > 100:
            (x, y), radius = cv2.minEnclosingCircle(cnt)
            if 5 < radius < 25:
                center = (int(x), int(y))
                radius = int(radius)
                diameter = 2 * radius
                cv2.circle(resultado_circulos, center, radius, (0, 255, 0), 2)
                cv2.putText(resultado_circulos, f"D={diameter}", (center[0] - 40, center[1] - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                
        
    return resultado_circulos
