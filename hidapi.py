import hid
import time

h = hid.device()
h.open(0x4d8, 0xdd)

pid = input("enter pid: ")

print("Manufacturer: %s" % h.get_manufacturer_string())
print("Product: %s" % h.get_product_string())
print("Serial No: %s" % h.get_serial_number_string())

# enable non-blocking mode
h.set_nonblocking(1)
# write some data to the device
print("Write the data")
#h.write([0xB0, 0x00])
h.write([0xB1, 0, 00, 18, 136, 111, 85, 240, int(pid), 0])

# wait
time.sleep(0.05)

# read back the answer
print("Read the data")
while True:
  d = h.read(20)
  if d:
    print(d)
  else:
    break

print("Closing the device")
h.close()
