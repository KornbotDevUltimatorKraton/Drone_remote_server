import requests 
from flask import Flask,render_template,url_for,redirect,url_for,request,jsonify
import bluetooth

app = Flask(__name__)
# the address of the remote device
#server_address = '8C:F7:10:C2:E5:62' # replace with the address of the remote device
#server_address = 'DC:A6:32:F3:2A:35'
# Define the port number to use for the connection
#port = 1

# Connect to the Bluetooth device
#sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
#sock.connect((server_address, port))
@app.route("/command_drone",methods=['GET','POST'])
def command_drone():
            input_json = request.get_json(force=True) 
            header = list(input_json)[0]
            commander = input_json.get(header)  
            # the address of the remote device
            server_address = 'DC:A6:32:F3:2B:9A' # replace with the address of the remote device
            #server_address = 'DC:A6:32:F3:2A:35'
            # Define the port number to use for the connection
            port = 1
            # Connect to the Bluetooth device
            sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            sock.connect((server_address, port))
            # Send a message to the device
            message = commander
            sock.send(message)
            # Receive a message from the device
            data = sock.recv(1024)
            print(f'Received message: {data}')
            # Close the connection
            #sock.close()
            return jsonify(input_json)

if __name__ == "__main__":
 
            app.run(debug=True,threaded=True,host="0.0.0.0",port=5978)
