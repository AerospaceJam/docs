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

## On installing packages with `mip`

When running command in the shell to connect to a Wi-Fi network, you **must** connect to a network with Internet access. `mip` may or may not work with school/district Wi-Fi, depending on the blocking/security filters placed on it.

**Do not change the SSID and password to those of your Pi's hotspot.** Remember that the Pi is acting as a Wi-Fi network, and when you're connected to it over USB, you're telling it what to do, not running code directly on your host computer - you're not connecting your computer to the Wi-Fi network, you're connecting the Pi's Wi-Fi chip itself.