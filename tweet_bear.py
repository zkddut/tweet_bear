from picamera import PiCamera
from datetime import datetime
from gpiozero import Button, LED
from time import sleep
from tweeter import *

def photoTweet():
  tweetTextPhoto('Bear tweet from rasp', photoCapture());


def photoCapture():
  filename = "{0:%Y}-{0:%m}-{0:%d}-{0:%H}-{0:%M}-{0:%S}".format(datetime.now())

  camera = PiCamera()
  camera.start_preview(alpha=190)
  sleep(1)
  path2file = '/home/pi/Desktop/' + filename + '.jpg'
  camera.capture(path2file)
  camera.stop_preview()
  camera.close()
  print("photo capture done")
  return path2file

def main():
  print("python main function")
  btn = Button(17)
  while(1):
   btn.when_pressed = photoTweet
   sleep(1)

if __name__ == '__main__':
    main()

