---
sidebar_position: 2
description: A guide to install MicroPython on your Pi.
---

# Installing MicroPython

## Prerequisites

For this guide, you'll need:

- A Micro-USB cable
- A computer with file management capabilities (A school Chromebook might work, but it also might not)
- The MicroPython firmware for the Pico W - Download from [here](https://micropython.org/download/rp2-pico-w/rp2-pico-w-latest.uf2)
- Your Raspberry Pi Pico W (which is included in your competition kit)

## Entering BOOTSEL

In order to install this new firmware on the microcontroller, we must first boot the Pi to `BOOTSEL` mode, which allows us to transfer a new firmware file to it and overwrite the default. To do so:

- Look at the top of your Pi and find the white button labeled `BOOTSEL`.
- Hold down this button, and keep it held down while you plug in the Pi.
- Plug the Micro-USB cable into the Pi, and wait for a new USB device to show up in your computer's file manager.
- Once it does, you can release the button.

## Flashing Firmware

Now, open the USB device, which should be called `RPI-RP2`, and copy the MicroPython firmware file over to it. The file will take a few seconds to copy, and the light on the Pi will flash rapidly while the operation is in progress. Once it completes, the USB device will disappear, and you will be ready to proceed to the next step.
