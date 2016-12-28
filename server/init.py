import bluetooth

target_name = "HC-06"
target_address = None

nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
    if target_name == bluetooth.lookup_name(bdaddr):
        target_address = bdaddr
        break

if target_address is not None:
    print("found target bluetooth device with address ", target_address)
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    print("Trying connection")
    i = 0
    maxPort = 3
    btConn = False
    err = True
    while err and i <= maxPort:
        print("Checking Port ", i)
        port = i
        try:
            sock.connect((target_address, port))
            err = False
        except Exception as e:
            i += 1
    if i > maxPort:
        print("Port detection Failed.")
        exit(0)

    while err is False:
        print(sock.recv(8192))

    print("Finished receiving")
    #sock.close()
else:
    print("could not find target bluetooth device nearby")