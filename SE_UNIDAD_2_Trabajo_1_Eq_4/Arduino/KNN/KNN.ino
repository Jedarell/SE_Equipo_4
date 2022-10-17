int potenciometros[] = {A0, A1, A2, A3, A4, A5, A6};

void setup() {
  // put your setup code here, to run once:
  Serial.begin (9600);
  Serial.setTimeout(100);
}

String cad_aux = "E";
int valorTemporal;
int n = 0;
void loop() {
  // put your main code here, to run repeatedly:

  for (int i = 0; i < 7; i++){
    valorTemporal = analogRead(potenciometros[i]);
    cad_aux += String(valorTemporal) + "A";
  }
  cad_aux += "F";
  Serial.println(cad_aux);
  delay(1000);
  cad_aux = "E";
}
