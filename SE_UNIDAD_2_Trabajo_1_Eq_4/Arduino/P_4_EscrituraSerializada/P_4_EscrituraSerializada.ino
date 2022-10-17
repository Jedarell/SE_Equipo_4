int leds [] = {10, 11, 12};
int actuadores [] = {A0, A1, A2};//potenciometro
//String cadena = "95A240A0";

void setup() {
  // put your setup code here, to run once:
  Serial.begin (9600);
  Serial.setTimeout(100);
}

String cad_aux = "";
char c;
String valorTemporal;

void loop() {
  // put your main code here, to run repeatedly:
  valorTemporal = analogRead (actuadores[0]);
  cad_aux += String (valorTemporal) + "A";

  valorTemporal = analogRead (actuadores[1]);
  cad_aux += String (valorTemporal) + "A";

  valorTemporal = analogRead (actuadores[2]);
  cad_aux += String (valorTemporal) + "F";

  Serial.println(cad_aux);
  cad_aux= "";

  delay(1000);

}
