import requests 
res = requests.post("http://192.168.50.201:5978/command_drone",json={"Tello":"command'})  #takeoff tello command on pdf SDK 2.0
