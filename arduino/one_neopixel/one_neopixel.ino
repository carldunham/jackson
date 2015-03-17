// Testing a single neopixel

#include <Adafruit_NeoPixel.h>
#ifdef __AVR_ATtiny85__ // Trinket, Gemma, etc.
 #include <avr/power.h>
#endif

#define PIN 0

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(1, PIN);


uint8_t color = 0;

uint32_t wheel(uint8_t color) {
  uint32_t ret = 0;
  uint32_t pos = color;
  
  if (pos < 85) {
    ret = ((pos*3) << 24) | ((255 - (pos*3)) << 16);
  }
  else if (pos < 170) {
    pos -= 85;
    ret = ((255 - (pos*3)) << 24) | (pos*3);
  }
  else {
    pos -= 170;
    ret = ((pos*3) << 16) | (255 - (pos*3));
  }
  return ret;
}

uint32_t xwheel(uint8_t color) {
  uint32_t ret = 0;
  uint32_t col = color;
  
  ret = (0x00ff00 << col*2);
 
  if (col > 85) {
    ret |= ((0xff<<((85-col)*2)) & 0xff);
  }
  return ret;
}

void setup() {
#ifdef __AVR_ATtiny85__ // Trinket, Gemma, etc.
  if(F_CPU == 16000000) clock_prescale_set(clock_div_1);
#endif
  pixels.begin();
  pixels.setBrightness(85); // 1/3 brightness
}

void loop() {
  pixels.setPixelColor(0, wheel(color++));
  pixels.show();
  
  delay(50);
}
