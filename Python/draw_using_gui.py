import pyautogui as pa

pa.click()
distance= 200
while(distance>0):
    print(distance,0)
    pa.dragRel(distance,0,duration=0.2) #move right
    distance = distance - 25
    print(0,distance)
    pa.dragRel(0,distance,duration=0.2) #move down
    print(-distance,0)
    pa.dragRel(-distance,0,duration=0.2) # move left
    distance = distance - 25
    print(0,-distance)
    pa.dragRel(0,-distance,duration=0.2) #move up
    
    
    
    