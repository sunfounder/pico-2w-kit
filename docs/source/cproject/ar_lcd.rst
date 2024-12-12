.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_lcd:

3.4 Liquid Crystal Display (LCD1602)
=====================================

In this lesson, we will learn how to use a **1602 LCD** with the Raspberry Pi Pico 2w to display text. The LCD1602 is a character-based liquid crystal display that can show 16 characters on 2 lines, making it ideal for projects that need to display information like messages, sensor readings, or status updates.

Connecting an LCD directly to a microcontroller typically requires many GPIO pins, which can limit the functionality of your project. To solve this problem, we can use an LCD1602 module that has an **I2C interface**. The I2C protocol uses only two data lines (SDA and SCL), allowing you to control the LCD with just two GPIO pins, freeing up other pins for additional sensors or devices.

**Understanding I2C on the Raspberry Pi Pico 2**

The Raspberry Pi Pico 2w supports I2C communication through multiple GPIO pins, providing flexibility for your projects. It has two I2C buses, I2C0 and I2C1, and each can be mapped to several sets of pins.

Here's a breakdown of the I2C-capable pins on the Pico 2:

|pin_i2c|

You can choose any matching pair of SDA and SCL pins for either I2C0 or I2C1. This flexibility allows you to avoid pin conflicts with other peripherals in your project.


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
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|

**Schematic**

|sch_lcd_ar|

**Wiring**

|wiring_lcd_ar|

**Writing the Code**

.. note::

    * You can open the file ``3.4_liquid_crystal_display.ino`` under the path of ``pico-2w-kit-main/arduino/3.4_liquid_crystal_display``. 
    * Or copy this code into **Arduino IDE**.
    * Then select the Raspberry Pi Pico board and the correct port before clicking the Upload button.
    * The ``LiquidCrystal I2C`` library is used here, you can install it from the **Library Manager**.

      .. image:: img/lib_i2c_lcd.png

.. code-block:: arduino

  #include <Wire.h>
  #include <LiquidCrystal_I2C.h>

  // Set the LCD I2C address (usually 0x27 or 0x3F)
  #define LCD_ADDRESS 0x27
  #define LCD_COLUMNS 16
  #define LCD_ROWS    2

  // Initialize the library with the I2C address and dimensions
  LiquidCrystal_I2C lcd(LCD_ADDRESS, LCD_COLUMNS, LCD_ROWS);

  void setup() {
    // Initialize the LCD
    lcd.init();
    lcd.backlight();  // Turn on the backlight

    // Print messages to the LCD
    lcd.setCursor(0, 0);  // Column 0, Row 0
    lcd.print("Hello, World!");
    lcd.setCursor(0, 1);  // Column 0, Row 1
    lcd.print("LCD1602 with I2C");
  }

  void loop() {
    // Nothing to do here
  }


After uploading the code to the Raspberry Pi Pico, the LCD should display the following:

* On the first line: "Hello, World!"
* On the second line: "LCD1602 with I2C"

If nothing appears on the screen, try adjusting the contrast by turning the small potentiometer (knob) on the back of the LCD module until the text becomes visible. 

**Understanding the Code**

#. Including Libraries:

   * ``Wire.h``: Handles I2C communication.
   * ``LiquidCrystal_I2C.h``: Simplifies interaction with the I2C LCD.

#. Defining the LCD Parameters:

   * ``LCD_ADDRESS``: The I2C address of the LCD module. Common addresses are 0x27 or 0x3F. If you're unsure, you can use an I2C scanner sketch to find the address.

   .. code-block:: arduino

      #define LCD_ADDRESS 0x27
      #define LCD_COLUMNS 16
      #define LCD_ROWS    2

#. Initializing the LCD:

   .. code-block:: arduino

      LiquidCrystal_I2C lcd(LCD_ADDRESS, LCD_COLUMNS, LCD_ROWS);

#. In ``setup()`` Function:

   .. code-block:: arduino

      lcd.init();         // Initializes the LCD
      lcd.backlight();    // Turns on the backlight

#. Displaying Text:

   .. code-block:: arduino

      lcd.setCursor(0, 0);  // Sets cursor to column 0, row 0
      lcd.print("Hello, World!");

      lcd.setCursor(0, 1);  // Sets cursor to column 0, row 1
      lcd.print("LCD1602 with I2C");

**Using Serial Input to Display Text on LCD**

We can enhance the program to read input from the Serial Monitor and display it on the LCD.

* Modified Code:

  .. code-block:: arduino

    #include <Wire.h>
    #include <LiquidCrystal_I2C.h>

    #define LCD_ADDRESS 0x27
    #define LCD_COLUMNS 16
    #define LCD_ROWS    2

    LiquidCrystal_I2C lcd(LCD_ADDRESS, LCD_COLUMNS, LCD_ROWS);

    void setup() {
      lcd.init();
      lcd.backlight();

      Serial.begin(115200);
      lcd.setCursor(0, 0);
      lcd.print("Enter text:");
    }

    void loop() {
      if (Serial.available() > 0) {
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("You typed:");

        String inputText = Serial.readStringUntil('\n');
        lcd.setCursor(0, 1);
        lcd.print(inputText);
      }
    }

  After uploading the code, type a message and press ``Enter``. The message will be displayed on the LCD.

* Explanation: 

  * Reading Serial Input: Checks if data is available on the Serial port. Reads the input string until a newline character is encountered.


   .. code-block:: arduino

      if (Serial.available() > 0) {
        String inputText = Serial.readStringUntil('\n');
        // ...
      }
    

  * Displaying Serial Input on LCD:

    .. code-block:: arduino

      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("You typed:");
      lcd.setCursor(0, 1);
      lcd.print(inputText);

**Troubleshooting**

* No Display on LCD:

  * Adjust the contrast potentiometer on the back of the LCD module.
  * Verify the wiring connections.
  * Make sure the correct I2C address is used. You can scan for devices on the I2C bus. If your I2C LCD1602 is connected correctly, the address will be displayed. The default address is usually 0x27, but in some cases, it could be 0x3F.
  
  .. code-block:: arduino

      #include <Wire.h>

      void setup() {
          Wire.begin();
          Serial.begin(115200);
          while (!Serial); // Wait for the serial connection to be established
          Serial.println("\nI2C Scanner");
      }

      void loop() {
          byte error, address;
          int nDevices;

          Serial.println("Scanning...");

          nDevices = 0;
          for (address = 1; address < 127; address++) {
              Wire.beginTransmission(address);
              error = Wire.endTransmission();

              if (error == 0) {
                  Serial.print("I2C device found at address 0x");
                  if (address < 16) {
                      Serial.print("0");
                  }
                  Serial.println(address, HEX);

                  nDevices++;
              }else if (error == 4) {
                  Serial.print("Unknown error at address 0x");
                  if (address < 16) {
                      Serial.print("0");
                  }
                  Serial.println(address, HEX);
              }
          }
          if(nDevices == 0) {
              Serial.println("No I2C devices found\n");
          }else {
              Serial.println("done\n");
          }
          delay(5000); // Wait 5 seconds before scanning again
      }

* Incorrect Characters Displayed:

  * Check for loose connections.
  * Verify that the LCD is properly initialized.

**Further Exploration**

* Custom Characters:

  Create and display custom characters or symbols on the LCD.

* Sensor Data Display:

  Read data from sensors (e.g., temperature, humidity) and display the readings on the LCD.

* Multiple I2C Devices:

  Connect multiple I2C devices to the Pico and manage them simultaneously.

**Conclusion**

In this lesson, you've learned how to use an I2C LCD1602 display with the Raspberry Pi Pico to display text. By utilizing the I2C interface, we've minimized the number of GPIO pins required, allowing for more complex projects with additional sensors and peripherals.

