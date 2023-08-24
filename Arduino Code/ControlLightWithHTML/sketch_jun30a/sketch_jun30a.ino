int analogPin = A0;   //The thermistor on analog pin 0
int ledPin = 3;       //The led is a output on pin 3
int val = 0;          //Initialise the value that will be read

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); //Begin the serial
  pinMode(analogPin,INPUT);
  pinMode(ledPin,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  val = analogRead(analogPin);  // read the input pin
  Serial.println(val);          // debug value
  if (val<400) {
    //statement(s)
    digitalWrite(ledPin, HIGH);
  }
  else{
    digitalWrite(ledPin, LOW);
  }
}
