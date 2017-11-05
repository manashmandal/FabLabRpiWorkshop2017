---
title: Interfacing PiCam with Raspberry Pi 3
permalink: /docs/picam/
---

## Connecting PiCamera with Raspberry Pi 3

![picam](https://i.imgur.com/imwCHBR.jpg)

## Configuring Pi for Camera

1. Go to terminal, enter this command `sudo raspi-config` 
2. Use the cursor keys to move to the camera option, and select `enable`.

## Using Terminal to take a photo

To test that the system is installed and working, try the following command:

```bash
raspistill -v -o test.jpg
```

## Python Code for Taking a Photo

Enter the following code in a `picam.py` file then run it. 

```python
import picamera
camera = picamera.PiCamera()
camera.capture('test.jpg')
```

The code can also be found [here](https://github.com/manashmndl/FabLabRpiWorkshop2017/tree/codes/RpiCamera). 
