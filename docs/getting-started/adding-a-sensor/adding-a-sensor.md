---
sidebar_position: 6
description: Now that we have our WebUI up and running, we can add a sensor's data to the stream.
---

# Adding a Sensor to the WebUI

## Prerequisites

For this guide, you'll need:

- A computer with the tools from previous parts of this guide installed, and your project folder based on the template WebUI
- Thonny opened on the computer and connected to your Pi
- A sensor connected to the Pi with functioning code

## Understanding the Template WebUI

:::tip

Remember that you don't have to neccesarily use the template provided, or keep the internals of it unmodified. If you can improve it (or even rewrite it), go for it! That kind of initive or coding expertise will be recognized in the scoring process. 

:::

```py
from aerospacejam import AerospaceJamServer
import time

WIFI_CONFIG = {
    'ssid': 'CHANGEME_AerospaceJam', # You should change these two lines!
    'password': 'CHANGEME_password',
    'static_ip': '192.168.4.1',
    'subnet_mask': '255.255.255.0',
    'gateway': '192.168.4.1',
    'dns': '192.168.4.1'
}

# Initialize the server with your Wi-Fi configuration
pico_server = AerospaceJamServer(WIFI_CONFIG)

# Register a sensor - this is a dummy sensor
pico_server.register_sensor("dummy", lambda: 25 + (time.time() % 10))

# Start the web server
pico_server.run()
```

- First, we import the `aerospacejam` module. This was written for the convenience of the teams competing this year, but you can feel free to modify it if you need to.
- Then, we import `time` to be able to check the current timestamp for the dummy sensor.
- Then, we initialize the webserver and hotspot with a configuration, and register a dummy sensor.
- How is the dummy sensor defined?
  - It's a *lambda*, which is a way to define a function compactly.

## Adding a Sensor

Now, let's see an example of code to register the [thermometer](/challenges/thermometer):

```py
# trimmed for brevity...
def get_temp(unit: str="F") -> float:
    """
    Gets the temperature from the thermometer.

    Parameters:
    - unit: The unit of temperature to get the temperature in. Can be "F", "C", or "tuple". "tuple" causes a return value of (tempC, tempF).
    """
    global roms, ds_sensor
    ds_sensor.convert_temp()
    if unit not in ["F", "C", "tuple"]:
        raise ValueError(f"Invalid unit: {unit}")
    tempC = ds_sensor.read_temp(roms[0])
    tempF = temp * (9/5) + 32
    if unit == "tuple":
        return tempC, tempF
    elif unit == "C":
        return tempC
    elif unit == "F":
        return tempF

pico_server.register_sensor("Thermometer (degrees F)", get_temp)
```

You can see that we pass the function as an argument - sometimes, functions can be treated as variables and can be passed to functions, too, just like any other value. If you ever need to pass *arguments* to a function, you can register it like this, with a lambda:

```py
pico_server.register_sensor("Thermometer (degrees C)", lambda: get_temp("C"))
```