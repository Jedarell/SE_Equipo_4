int leds[] = {9, 10, 11};

String cadena;
String aux;
//String cadena = "95A240A0";

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(100);
}

int j = 0;
char c;

void loop(){
  // put your main code here, to run repeatedly:
  if (Serial.available()>0){
    c = Serial.read();
    if(c == 'E'){
      aux = "";
      j = 0;
    }else if(c == 'A' || c == 'F'){
      Serial.println(aux);
      analogWrite(leds[j], aux.toInt());
      aux = "";
      j++;
    }else {
      aux += c; 
    }
    //delay(1000);
  }
}
