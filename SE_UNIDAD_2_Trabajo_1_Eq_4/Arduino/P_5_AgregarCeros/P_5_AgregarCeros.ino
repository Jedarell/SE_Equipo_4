int leds [] = {10, 11, 12};
int actuadores [] = {A0, A1, A2};//potenciometro
//String cadena = "95A240A0";

void setup() {
  // put your setup code here, to run once:
  Serial.begin (9600);
  Serial.setTimeout(100);
}

String cad_aux = "E";
String aux;
char c;
String valorTemporal;

void loop() {
  // put your main code here, to run repeatedly:
  valorTemporal = analogRead (actuadores[0]);
  aux = agregarCeros(valorTemporal.toInt());
  cad_aux += aux + "A";

  valorTemporal = analogRead (actuadores[1]);
  aux = agregarCeros(valorTemporal.toInt());
  cad_aux += aux + "A";

  valorTemporal = analogRead (actuadores[2]);
  aux = agregarCeros(valorTemporal.toInt());
  cad_aux += aux + "F";
  
  Serial.println(cad_aux);
  cad_aux= "";
  
  delay(1000);

  cad_aux = "E";
}

String agregarCeros(int numero) {
  String numConCeros;
  numConCeros = String(numero);
  if(numConCeros.length() == 1){
    numConCeros = "000" + numConCeros;
  }else if(numConCeros.length() == 2){
    numConCeros = "00" + numConCeros;
  }else if(numConCeros.length() == 3){
    numConCeros = "0" + numConCeros;
  }
  return numConCeros;
}
