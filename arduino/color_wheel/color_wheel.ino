/*
 * Color Wheel LED
 *
 * Loops a RGB LED attached to pins 9,10,11 through
 * all the "exterior" colors of a Color Wheel
 * 
 * The RGB LED uses a 3 component (red green blue) model which adds light colors to produce 
 * a composite color. But the RGB does not make easy to loop through a more
 * "natural" sequence of colors. The HSV (hue saturation value) model uses a color cylinder
 * in which each color is a point inside the cylinder. 
 * The hue is represented by the angle at which the point is, the saturation represents
 * the length (how close to the center the point is) and the value represent the height at
 * which the point is. 
 *
 * By cycling the hue value from 0 to 360 degrees, and keeping the saturation and value at 1
 * we can represent all the brightest colors of the wheel, in a nice natural sequence.
 *
 * The algorithm to convert a HSV value to a RGB value is taken from Chris Hulbert's blog (splinter)
 *
 * Created 1 January 2011
 * By Eduardo A. Flores Verduzco
 * http://eduardofv.com
 *
 * References:
 * http://en.wikipedia.org/wiki/HSL_and_HSV
 * http://en.wikipedia.org/wiki/Color_wheel
 * http://splinter.com.au/blog/?p=29
 *
 *
 * Modified by cdunham@gmail.com for NeoPixel
 * original at http://eduardofv.com/read_post/179-Arduino-RGB-LED-HSV-Color-Wheel-
 *
 */

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
  pixels.setBrightness(50);
}

void loop() {
  wheel();
}

void test() {
  setLedColorHSV(0, 1, 1);
  delay(1000);
  setLedColorHSV(120, 1, 1);
  delay(100);
  setLedColorHSV(240, 1, 1);
  delay(100);
}

void wheel() {
  //The Hue value will vary from 0 to 360, which represents degrees in the color wheel
  for(int hue=0;hue<360;hue++) {
    setLedColorHSV(hue,1,1); //We are using Saturation and Value constant at 1
    delay(50); //each color will be shown for 10 milliseconds
  }
}

//Convert a given HSV (Hue Saturation Value) to RGB(Red Green Blue) and set the led to the color
//  h is hue value, integer between 0 and 360
//  s is saturation value, double between 0 and 1
//  v is value, double between 0 and 1
//http://splinter.com.au/blog/?p=29
void setLedColorHSV(int h, double s, double v) {
  //this is the algorithm to convert from RGB to HSV
  double r=0; 
  double g=0; 
  double b=0;

  double hf=h/60.0;

  int i=(int)floor(h/60.0);
  double f = h/60.0 - i;
  double pv = v * (1 - s);
  double qv = v * (1 - s*f);
  double tv = v * (1 - s * (1 - f));

  switch (i)
  {
  case 0: //rojo dominante
    r = v;
    g = tv;
    b = pv;
    break;
  case 1: //verde
    r = qv;
    g = v;
    b = pv;
    break;
  case 2: 
    r = pv;
    g = v;
    b = tv;
    break;
  case 3: //azul
    r = pv;
    g = qv;
    b = v;
    break;
  case 4:
    r = tv;
    g = pv;
    b = v;
    break;
  case 5: //rojo
    r = v;
    g = pv;
    b = qv;
    break;
  }

  //set each component to a integer value between 0 and 255
  int red=constrain((int)255*r,0,255);
  int green=constrain((int)255*g,0,255);
  int blue=constrain((int)255*b,0,255);

  setNeoPixelColor(red,green,blue);
}

//Sets the current color for the RGB LED
void setLedColorRGB(int red, int green, int blue) {
  //Note that we are reducing 1/4 the intensity for the green and blue components because 
  //  the red one is too dim on my LED. You may want to adjust that.
  analogWrite(9,red); //Red pin attached to 9
  analogWrite(10,green/3); //Red pin attached to 9
  analogWrite(11,blue/3); //Red pin attached to 9
}

void setNeoPixelColor(uint8_t red, uint8_t green, uint8_t blue) {
  uint32_t color = ((uint32_t)red << 16) | ((uint32_t)green << 8) | (uint32_t)blue;
  pixels.setPixelColor(0, color);
  pixels.show();
}

