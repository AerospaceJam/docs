---
sidebar_position: 1
---

# Sensors and Reconnaissance

This category assesses a team's ability to integrate sensors, gather data, and perform complex tasks based on that data. For most challenges, points are awarded based on the highest level of difficulty achieved; points for lower levels in the same category are not cumulative. The Payload challenge is an exception, where points are awarded for each completed sub-task.

## Total Possible Reconnaissance Score: 30 Points

| Category | Maximum Points |
| :--- | :--- |
| Basic Sensor Integration | 2 Points |
| Barometric Pressure (BMP180) | Up to 8 Points |
| Accelerometer/Gyro (MPU-6050) | Up to 12 Points |
| LiDAR (TF-Luna) | Up to 15 Points |
| Camera | Up to 10 Points |
| Payload Manipulation | Up to 25 Points (Special) |

:::warning Scoring Rules

- For all challenges except Payload, your team will be awarded points **only for the highest tier you successfully complete**. For example, if you complete Level 2 (4 points) and Level 3 (6 points) of the Barometric Pressure challenge, you will receive 6 points, not 10.
- The Payload challenge is cumulative. You earn points for each sub-task you complete.
- All tasks must be demonstrated to a judge's satisfaction. The drone must perform the action, and the resulting data must be correctly displayed on the base station where applicable.
:::

---

## Basic Sensor Integration (2 Points)

This is a foundational check to ensure your system is working.

| Score | Criteria |
| :--- | :--- |
| **2 Points (Pass)** | The base station successfully receives and displays valid data from at least one sensor on the drone. |
| **0 Points (Fail)** | Communication between the drone and base station is not established, or no valid sensor data is displayed. |

## Barometric Pressure (Up to 8 Points)

Demonstrate use of the BMP180 sensor for atmospheric and altitude measurements.

| Score | Level | Criteria |
| :--- | :--- | :--- |
| **2 Points** | 1 | Read and display the current ambient barometric pressure. |
| **4 Points** | 2 | Fly to a designated target position and read the ambient barometric pressure at that location. |
| **6 Points** | 3 | Use the pressure reading to calculate and display the drone's approximate height above sea level. |
| **8 Points** | 4 | Track and log changes in the drone's height over time during flight. |

## Accelerometer/Gyro (Up to 12 Points)

Demonstrate use of the MPU-6050 for motion tracking.

| Score | Level | Criteria |
| :--- | :--- | :--- |
| **2 Points** | 1 | Get and display a single, valid acceleration and gyroscope reading during flight. |
| **4 Points** | 2 | Log and display multiple acceleration and gyroscope readings over a period of time. |
| **8 Points** | 3 | Log and **graph** the acceleration and gyroscope readings on the base station in real-time. |
| **12 Points**| 4 | Log, graph, and **integrate** readings over time to estimate the drone's absolute position and rotation throughout its flight. |

:::tip What is "Integration"?
Don't worry if you haven't taken calculus! In this context, "integration" is just a fancy word for **repeatedly adding up small changes over time**.

- Your accelerometer gives you **acceleration** (how quickly speed is changing).
- If you multiply acceleration by a tiny amount of time (like the time between sensor readings), you get a small change in **velocity**. If you keep a running total of these small changes, you can estimate your drone's current velocity.
- If you do the same thing with velocity (velocity × time), you get a small change in **position**. Keep a running total of *those* changes, and you can estimate your drone's position!

This process allows you to go from relative sensor readings (like "I'm accelerating forward") to an absolute estimate (like "I am 5 meters in front of where I started"). The same logic applies to the gyroscope to find the drone's absolute rotation.
:::

## LiDAR (Up to 15 Points)

Demonstrate use of the TF-Luna LiDAR sensor for distance measurement and mapping.

| Score | Level | Criteria |
| :--- | :--- | :--- |
| **3 Points** | 1 | Land at a target location and accurately read the distance to a single designated object. |
| **6 Points** | 2 | Land, read the distance to a target, spin 180°, read the distance to a second target, and correctly add the two values in your code. |
| **9 Points** | 3 | Land and spin continuously to map the surface, displaying the raw data on the base station. |
| **12 Points**| 4 | Land, spin, and map the surface, **graphing** the result as a 2D map on the base station. |
| **15 Points**| 5 | Land, spin, and create a graphed 2D map that uses gyroscope data to improve the map's accuracy. |

## Camera (Up to 10 Points)

Demonstrate the ability to capture and transmit image data.

| Score | Level | Criteria |
| :--- | :--- | :--- |
| **3 Points** | 1 | Land on a target and transmit a clear picture of the surface below the drone. |
| **5 Points** | 2 | **Hover** over a target and transmit a clear picture of the surface below the drone. |
| **8 Points** | 3 | Transmit a real-time video stream from the drone to the base station at a rate less than 12 frames per second (fps). |
| **10 Points**| 4 | Transmit a real-time video stream from the drone to the base station at a rate of 12 fps or greater. |

## Payload Manipulation (Up to 35 Points - Cumulative)

This special challenge assesses your ability to interact with and transport a payload. Points are cumulative.

| Score | Task | Criteria |
| :--- | :--- | :--- |
| **+5 Points** | Grab | Land on the payload cage and successfully attach a payload to your drone's magnet for at least 5 seconds. |
| **+5 Points** | Remove | Successfully lift the payload and remove it from the payload cage. |
| **+5 Points** | Transport | Fly to and land at a designated target location while still carrying the payload. |
| **+10 Points**| Drop & Land | Successfully drop the payload into a designated target box and then land the drone safely in a final target location. |
| **+10 Points**| Fancy Maneuvers... | Fly with the payload through a loop approximately 1.5m off the ground, drop the payload into a designated target box, and then land teh drone safely in a final target location. |

:::tip
If you drop a payload, you can always get another.
:::

:::note
We don't actually expect anyone to complete the last one... if you do - good on you! But it isn't included in the total possible maximum for this category since we don't think anyone will actually pull it off.
:::