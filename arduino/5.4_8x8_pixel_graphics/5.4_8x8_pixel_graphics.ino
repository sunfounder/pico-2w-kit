const int STcp = 19;  // Pin connected to ST_CP (latch pin) of 74HC595
const int SHcp = 20;  // Pin connected to SH_CP (clock pin) of 74HC595
const int DS = 18;    // Pin connected to DS (data pin) of 74HC595

// Data array representing the 'X' shape on an 8x8 LED matrix
byte datArray[] = {0x7E, 0xBD, 0xDB, 0xE7, 0xE7, 0xDB, 0xBD, 0x7E};

void setup() {
  // Set pins as outputs
  pinMode(STcp, OUTPUT);
  pinMode(SHcp, OUTPUT);
  pinMode(DS, OUTPUT);
}

void loop()
{
  for(int num = 0; num <8; num++)
  {
    digitalWrite(STcp,LOW); //ground ST_CP and hold low for as long as you are transmitting
    shiftOut(DS,SHcp,MSBFIRST,datArray[num]);
    shiftOut(DS,SHcp,MSBFIRST,0x80>>num);    
    //return the latch pin high to signal chip that it 
    //no longer needs to listen for information
    digitalWrite(STcp,HIGH); //pull the ST_CPST_CP to save the data
  }
}
