int leds[] = {9, 10, 11};

String cadena = "E0100A0010A0000F";
String aux = "";

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(100);
}

int j = 0;

void loop(){
  // put your main code here, to run repeatedly:

  if(cadena.charAt(0) == 'E' && cadena.charAt(15) == 'F'){
    Serial.println("Cadena completa");
  
    for (int i = 1; i<cadena.length() - 1; i++) {
      if (cadena[i] != 'A') {
        aux += cadena[i];  
      }else {
        Serial.println(aux);
        analogWrite(leds[j], aux.toInt());
        j++;
        aux = "";
      }
    }

    Serial.println(aux);
    analogWrite(leds[2], aux.toInt());
    while(true) {
      
    }

    delay(1000);
  }
}
