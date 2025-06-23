import cv2
import numpy as np
from naoqi import ALProxy

NAO_IP = "192.168.1.116"  
PORT = 9559

camera = 1             
resolution = 0        
colorSpace = 11        
fps = 30
clientName = "python_client"

try:
    videoProxy = ALProxy("ALVideoDevice", NAO_IP, PORT)
    client = videoProxy.subscribeCamera(clientName, camera, resolution, colorSpace, fps)
    
    cv2.namedWindow("NAO Camera - FULLSCREEN", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("NAO Camera - FULLSCREEN", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    
    print("Pressione 'Q' para sair...")
    while True:
        naoImage = videoProxy.getImageRemote(client)
        if not naoImage:
            break

        width = naoImage[0]
        height = naoImage[1]
        imageArray = np.frombuffer(naoImage[6], dtype=np.uint8).reshape((height, width, 3))

        tela_cheia = cv2.resize(imageArray, (1920, 1080), interpolation=cv2.INTER_LINEAR)
    
        cv2.imshow("NAO Camera - FULLSCREEN", tela_cheia)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except Exception as e:
    print("Erro:", e)
finally:
    if 'videoProxy' in locals() and 'client' in locals():
        videoProxy.unsubscribe(client)
    cv2.destroyAllWindows()
    print("Streaming encerrado.")
