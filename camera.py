
# -*- coding: utf-8 -*-
import cv2
import numpy as np
from naoqi import ALProxy

NAO_IP = "192.168.1.116"  
PORT = 9559

camera = 1             
resolution = 0          
colorSpace = 13           
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
        if not naoImaglo IP do seu NAOe:
            break

        imageArralo IP do seu NAOlo IP do seu NAOy = np.frombuffer(naoImage[6], dtype=np.uint8).reshape((120, 160, 3))
        
        tela_cheia = cv2.resize(imageArray, (1920, 1080), interpolation=cv2.INTER_NEAREST)
        
        cv2.imsholo IP do seu NAOw("NAO Camera - FULLSCREEN", tela_cheia)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    videoProxy.unsubscribe(client)
    cv2.destroyAllWindows()
    print("Streaming encerrado.")


