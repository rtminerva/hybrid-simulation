# import base64
# 
# with open("test.tif", "rb") as imageFile:
#     str = base64.b64encode(imageFile.read())
#     print str
# Source

with open("test.tif", "rb") as imageFile:
  f = imageFile.read()
  b = bytearray(f)

print len(b)