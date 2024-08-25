---
title: ESP32
tags:
  - info/hardware/esp32
---

## Outils de dev pour GNU/Linux

### ESP-IDF

From [this page](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/linux-macos-setup.html) :

```shell
# tools
sudo apt-get install git wget flex bison gperf python3 python3-pip python3-venv cmake ninja-build ccache libffi-dev libssl-dev dfu-util libusb-1.0-0
mkdir -p ~/esp
cd ~/esp
git clone --recursive https://github.com/espressif/esp-idf.git
cd ~/esp/esp-idf
./install.sh esp32
. ./export.sh
# check connection
ls /dev/tty [TAB]
# example
cd /path/to/examples/hello_world
idf.py set-target esp32h2
idf.py menuconfig  # ???
idf.py build  # seulement si pas de flash
idf.py -p /dev/ttyACM0 flash
idf.py -p /dev/ttyACM0 monitor  # Ctrl+] to exit
idf.py -p /dev/ttyACM0 flash monitor  # pour enchainer
```

### Arduino

Pour GNU/Linux, j’ai téléchargé l’appimage puis j’ai eu à `sudo apt install python3-serial`.

## Depuis IDE Arduino

- Fichier/Préférence : URL vers bibli, à séparer avec des virgules  
  `https://dl.espressif.com/dl/package_esp32_index.json`
- Outil/Type de carte : Gestionnaire, chercher ESP32
- Outil/Type de carte : Choisir le module qui devrait apparaître
- Pour avoir le moniteur série avec l’ESP32H2 il faut activer Tools/USB CDC on boot (voir [ici](https://docs.espressif.com/projects/arduino-esp32/en/latest/troubleshooting.html#serial-not-printing))
- exemples :
  - blink
  - touch read
- Pour mon esp32-h2
- Pas eu besoin de :
  - Outil/Port : Trouver le COM qui correspond au module
  - Garder le bouton Boot appuyé pour flasher

Attention certaines bibliothèques n’ont pas été modifiées pour les outils de compilation 3.x, donc dans le board manager il faut rester en 2.0.17. Sauf qu’il n’y a pas de support pour esp32h2 dans ce dernier.

## Hardware

- [nano-ESP32](https://docs.arduino.cc/hardware/nano-esp32/)

## Doc officielle

- [ESP32 modules and boards](https://docs.espressif.com/projects/esp-idf/en/v4.3/esp32/hw-reference/modules-and-boards.html)
- [LED control](https://docs.espressif.com/projects/esp-idf/en/v5.1/esp32h2/api-reference/peripherals/ledc.html)

## Articles et videos intéressantes

- [Premiers tests pour bien débuter](https://www.youtube.com/watch?v=zqwnYuOLvsE) (YT)
- [un gist pour un clavier BT](https://gist.github.com/manuelbl/66f059effc8a7be148adb1f104666467)
- [clavier BT sur Hackaday](https://hackaday.com/2020/02/13/emulating-a-bluetooth-keyboard-with-the-esp32/)
- https://www.instructables.com/DIY-Bluetooth-Macro-Keypad/
- [esp32 as USB keyb](https://www.youtube.com/watch?v=yyn53aIYBg8) on YT
  - video inintéressante mais lien vers code :
    - [parallel](https://github.com/Makerfabs/Makerfabs-ESP32-S3-Parallel-TFT-with-Touch)
    - [SPI](https://github.com/Makerfabs/Makerfabs-ESP32-S3-SPI-TFT-with-Touch)
- https://www.reddit.com/r/esp32/comments/zfgxqi/send_keystroke_with_esp32s3_through_usb/
  - qui pointe vers https://hackaday.com/2021/03/26/usb-comes-to-the-esp32/

## Enquêter

- https://gist.github.com/manuelbl/66f059effc8a7be148adb1f104666467
- https://github.com/tanakamasayuki/EspUsbHost
- https://github.com/asterics/esp32_mouse_keyboard
- https://circuitdigest.com/videos/gesture-controlled-hid-bluetooth-keyboard-using-esp32

