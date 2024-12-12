.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_mpr121:

4.3 Electrode Keyboard with MPR121
========================================================

In this lesson, we'll learn how to use the **MPR121 capacitive touch sensor** to create a touch-sensitive keyboard with the Raspberry Pi Pico 2w. The MPR121 allows you to detect touch inputs on up to 12 electrodes, which can be connected to conductive materials like wires, foil, or even fruits like bananas!

* :ref:`cpn_mpr121`

**Required Components**

In this project, we need the following components. 

It's definitely convenient to buy a whole kit, here's the link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ITEMS IN THIS KIT
        - PURCHASE LINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|

You can also buy them separately from the links below.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - COMPONENT INTRODUCTION	
        - QUANTITY
        - PURCHASE LINK

    *   - 1
        - :ref:`cpn_pico_2w`
        - 1
        - |link_pico2w_buy|
    *   - 2
        - Micro USB Cable
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Several
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_mpr121`
        - 1
        - 

**Understanding the MPR121 Sensor**

The **MPR121** is a capacitive touch sensor controller that communicates via the I2C interface. It can handle up to 12 touch inputs, making it ideal for creating interactive projects with multiple touch points.

The MPR121 sensor detects changes in capacitance on its electrodes. When you touch an electrode, the capacitance changes, and the sensor registers a touch.The sensor communicates this information over I2C to the Raspberry Pi Pico 2.


**Schematic**

|sch_mpr121_ar|



**Wiring**

|wiring_mpr121_ar|

* Connect wires or conductive materials to the electrode pins (labeled **E0** to **E11**) on the MPR121.
* You can attach the other ends of the wires to conductive objects like fruits, aluminum foil shapes, or touchpads.

**Writing the Code**

.. note::

    * You can open the file ``4.3_electrode_keyboard.ino`` under the path of ``pico-2w-starter-kit-main/arduino/4.3_electrode_keyboard``. 
    * Or copy this code into **Arduino IDE**.
    * Then select the Raspberry Pi Pico board and the correct port before clicking the Upload button.
    * The ``Adafruit MPR121`` library is used here, you can install it from the **Library Manager**.

      .. image:: img/lib_mpr121.png

.. code-block:: arduino

    #include <Wire.h>
    #include <Adafruit_MPR121.h>

    // Create an instance of the MPR121 sensor
    Adafruit_MPR121 cap = Adafruit_MPR121();

    // Array to hold the touch states of each electrode
    bool touchStates[12] = { false };

    // Variables to store current and last touch states
    uint16_t currtouched = 0;
    uint16_t lasttouched = 0;

    void setup() {
      Serial.begin(115200); // Initialize serial communication at 115200 baud
      while (!Serial);    // Wait for Serial Monitor to open

      // Initialize the MPR121 sensor with I2C address 0x5A
      if (!cap.begin(0x5A)) {
        Serial.println("MPR121 not found, check wiring?");
        while (1);
      }
      Serial.println("MPR121 found!");
    }

    void loop() {
      // Get the currently touched pads
      currtouched = cap.touched();

      // Check if there is a change in touch state
      if (currtouched != lasttouched) {
        // Update the last touched state
        lasttouched = currtouched;

        // Iterate through each electrode
        for (int i = 0; i < 12; i++) {
          // Check if the electrode is touched
          if (currtouched & (1 << i)) {
            touchStates[i] = true;
          } else {
            touchStates[i] = false;
          }
        }

        // Print the touch states as a binary string
        for (int i = 0; i < 12; i++) {
          Serial.print(touchStates[i] ? "1" : "0");
        }
        Serial.println();
      }

      delay(100); // Small delay to stabilize readings
    }

After uploading the code, touch the electrodes connected to the MPR121 sensor. 

* Observe the binary output in the Serial Monitor indicating which electrodes are being touched. 
* For example, touching the first and eleventh electrodes will display ``100000000010``.


**Understanding the Code**

#. Including Libraries:


   * ``Wire.h``: Handles I2C communication.
   * ``Adafruit_MPR121.h``: Provides functions to interact with the MPR121 sensor.

#. Initializing the MPR121 Sensor:

   Creates an instance of the MPR121 sensor.

   .. code-block:: arduino

      Adafruit_MPR121 cap = Adafruit_MPR121();

#. Setup Function:

   * Starts serial communication for debugging.
   * Initializes the MPR121 sensor with the I2C address 0x5A.
   * If the sensor is not found, it prints an error message and halts the program.

   .. code-block:: arduino

      void setup() {
        Serial.begin(115200); // Initialize serial communication
        while (!Serial);    // Wait for Serial Monitor to open

        // Initialize the MPR121 sensor with I2C address 0x5A
        if (!cap.begin(0x5A)) {
          Serial.println("MPR121 not found, check wiring?");
          while (1);
        }
        Serial.println("MPR121 found!");
      }

#. ``loop()`` Function: 

   * Retrieves the current touch state from the MPR121 sensor. Each bit in the ``currtouched`` variable represents the touch state of an electrode (1 for touched, 0 for not touched).

     .. code-block:: arduino
  
        currtouched = cap.touched();

   * Checks if there has been a change in the touch state since the last loop iteration.

     .. code-block:: arduino

        if (currtouched != lasttouched) {
          // Update touch states
        }

   * Iterates through each electrode and updates the ``touchStates`` array based on whether each electrode is touched.

     .. code-block:: arduino

        for (int i = 0; i < 12; i++) {
          if (currtouched & (1 << i)) {
            touchStates[i] = true;
          } else {
            touchStates[i] = false;
          }
        }

   * Prints the touch states as a 12-bit binary string to the Serial Monitor. For example, if the first and eleventh electrodes are touched, it will print 100000000010.

     .. code-block:: arduino

        for (int i = 0; i < 12; i++) {
          Serial.print(touchStates[i] ? "1" : "0");
        }
        Serial.println();

   * Adds a short delay to stabilize the readings and prevent flooding the Serial Monitor.

     .. code-block:: arduino

        delay(100);

**Extending the Electrodes**

You can enhance your project by connecting the electrodes to various conductive materials:

* **Fruits**: Attach wires to bananas, apples, or other fruits to turn them into touch-sensitive inputs.
* **Foil Shapes**: Cut shapes out of aluminum foil and attach them to the electrodes.
* **Conductive Paint**: Draw patterns with conductive ink or paint.

.. note::
    
    If you change the electrodes (e.g., connect different materials), you may need to reset the sensor to recalibrate the baseline values.

**Further Exploration**

* Creating Interactive Projects:

  Build a touch-controlled LED matrix where each electrode controls an individual LED.

* Implementing Key Debouncing:

  Enhance the reliability of touch detection by implementing debouncing techniques to filter out false touches.

* Combining with Other Sensors:

  Integrate the MPR121 with other sensors like temperature or light sensors to create more complex interactive systems.

* Developing a Touch-Based Game Controller:

  Use the touch inputs to control game elements, such as moving characters or selecting options.

**Conclusion**

In this lesson, you've learned how to use the MPR121 capacitive touch sensor with the Raspberry Pi Pico to create a touch-sensitive keyboard. By detecting touch inputs on multiple electrodes, you can build interactive interfaces for your projects, such as custom keypads, control panels, or creative input devices. Understanding how to read and process touch inputs is a valuable skill for developing responsive and user-friendly electronics projects.
