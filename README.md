Raizin: Containerized Raspberry pi with Arduino using temperature sensor
===========

Our sensor system is temperature measurement system using **Raspberry pi** and　**Arduino**.　

Description
-----------
The system senses and displays temperature using **Raspberry pi** with **Arduino**.   
The arduino senses temperature, and controlls LED based on temperature.  
Concretely, arduino programming language (like C) controlls sensor and LED connected aruduino.
The LED light green when range of temperature is 20-30 degrees Celsius, and red otherwise.  
In addition, Raspberry pi controlls the arduino using python, and displays temperatures.

Requirement
-----------
our system require below:
* Arduino
* temperature sensor (LM75B)
* LED (green and red)
* Jumper wire and breadboard
* Raspberry pi

Author
------------
nicuo

Versioning
-------------
### ver 1.0
* Aruduino <br>
Aruduino develop plan is closed.

* Raspberry Pi　<br>
Raspberry pi gets temperatures sensed by aruduino via serial communication, displays the temperatures.
**We plan the app loaded to container. **
