# Temperature-Activated Fan Controller

This project enables automatic fan control based on temperature thresholds using a 2N2222 transistor.

## Functionality:
- The circuit acts as a switch, activating the fan when the temperature exceeds a set threshold value.
- Ensure your GPIO pins are appropriately configured to handle the transistor and fan current requirements.

## Usage:
- Modify the temperature threshold value in the code to suit your needs.
- Run the script on your Raspberry Pi or compatible platform to monitor and control the fan automatically.

## Components Required:
- 2N2222 transistor
- GPIO pins on a Raspberry Pi or similar device

## Setup Instructions:
1. **Transistor Connections:**
   - **Collector:** Connect to the ground of the fan.
   - **Base:** Connect to GPIO PIN 12.
   - **Emitter:** Connect to the ground (GND) of the GPIO.

2. **Fan Connections:**
   - **Positive:** Connect to the 5V pin of the GPIO.
   - **Ground:** Connect to the collector of the transistor.

# Side Note
I haven't had the opportunity to write a comprehensive guide or documentation for this project. However, if you're seeking detailed information, you can check out my friend's repository [here](https://github.com/0xHaru/Raspberry-Pi-Fan-Controller).
