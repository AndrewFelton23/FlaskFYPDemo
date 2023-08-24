const int ledPin = 3; // Pin connected to the LED
const int analogPin = A0; // Analog input pin

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600); // Start serial communication at 9600 baud rate
}

void loop() {
  // Read analog value and send it over serial
  int analogValue = analogRead(analogPin);
  Serial.println(analogValue);
  
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == '0') {
      // If the off button is pressed
      digitalWrite(ledPin, LOW); // Turn off the LED
    } 
    else if (command == '1') {
      // If the on button is pressed
      digitalWrite(ledPin, HIGH); // Turn on the LED
    }
    // Add additional conditions for other commands if needed
  }
}
