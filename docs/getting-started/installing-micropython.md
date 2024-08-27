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

In order to install this new firmware on the microcontroller, we must first boot the Pi to "BOOTSEL" mode, which allows us to transfer a new firmware file to it and overwrite the default.