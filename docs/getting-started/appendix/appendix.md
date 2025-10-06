---
sidebar_position: 8
description: Additional information to aid you on your journey.
---

# Appendix

This page contains information that didn't fit anywhere else in this documentation, but is still extremely important.

:::danger

You should read this page in its entirety before trying to fly your drone.

:::

## "Fly Mode"

On some controllers included with older MINDS-I drone kits (namely the Flysky `FS-i6S`), there exists a mostly undocumented mode called "Fly Mode". If your controller has this mode, it will be visible quite plainly on the home screen:

![Fly Mode](flymode.png)

Although it may seem intuitive to enable this mode, ***ABSOLUTELY DON'T***. If Fly Mode is enabled the drone will behave erratically and has been known to take off at high speeds in random directions.

## Arming a Drone

In order to arm your drone, you must pull the throttle stick (on the left) down and to the right (towards the center).

![Arming](arming.png)

This will cause your drone's motors to spin to life, and allow you to pilot your drone as normal.

## Disarming (Stopping) a Drone

If you're ever flying your drone and crash, or otherwise land and need to shut off your drone urgently, pull the throttle stick (on the left) all the way down and to the left.

![Disarming](disarming.png)

This will immediately stop all function of the drone's motors and will require you to disconnect and re-connect the battery in order to resume flight again. Remember to ask the judges presiding over your field time for permission before entering the net to perform this operation.

## I2C issues with the PiSugar power supply

Some sensors use a protocol called I2C, which requires two reserved pins on your Raspberry Pi. However, when left in its default mode, the PiSugar power supply that we use for Aerospace Jam wil interfere with this protocol and use these two pins for its own purposes, which we don't want. In order to disable it, make sure that the switch on the PiSugar is ***NOT*** set to "auto", and is instead off, as shown in the below picture:

![pisugar switch](../first-sensor/image.png)
