#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install qrcode


# In[2]:


import qrcode

data = "https://github.com/Armin-Abdollahi"

qr = qrcode.QRCode(version=1, error_correction = qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color = "White")

img.show(img)
img.save("qrcode.png")

