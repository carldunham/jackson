#include <Adafruit_NeoPixel.h>
#ifdef __AVR_ATtiny85__ // Trinket, Gemma, etc.
 #include <avr/power.h>
#endif

#define PIN 0

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(1, PIN);

void setup() {
#ifdef __AVR_ATtiny85__ // Trinket, Gemma, etc.
  if(F_CPU == 16000000) clock_prescale_set(clock_div_1);
#endif
  pixels.begin();
  pixels.setBrightness(85); // 1/3 brightness
}

void flash() {
  
  for (int i=0; i<3; i++) {
    pixels.setPixelColor(0, 0);
    pixels.show();
    delay(50);
    pixels.setPixelColor(0, 0xffffff);
    pixels.show();
    delay(50);
  }
}

void loop() {
  pixels.setPixelColor(0, 0xff0000);
  pixels.show();
  delay(1000);
  pixels.setPixelColor(0, 0x00ff00);
  pixels.show();
  delay(2000);
  pixels.setPixelColor(0, 0x0000ff);
  pixels.show();
  delay(3000);
  
  flash();

  uint32_t color = 0xff0000;
  
  for (int i=0; i<=24; i++) {
    pixels.setPixelColor(0, color);
    pixels.show();
    delay(200);
    color >>= 1;
  }
  
  flash();
}

