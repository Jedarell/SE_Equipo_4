int leds[] = {10, 11, 12};
//String cadena = "95A240A0";

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(100);
}

String cadena = "95A240A0";
//cadena = "XAYAZ"; //X,Y,Z 
//pueden ser cualquier valor en 0 y 255

String cad_aux= "";
void loop() {
  // put your main code here, to run repeatedly 

  if(Serial.available()>0){
      cadena = Serial.readString();
    }
  cadena.remove(16);
  //"E0095A0240A0000F"  // 0095  0240 0000
  //"E0195A0140A0080F"  // 0195  0140 0080
  if(cadena.charAt(0) == 'E' && cadena.charAt(15)=='F'){
    Serial.println("Cadena Completa");
    
    for(int i=1; i<cadena.length() - 1; i++){
        if(cadena[i]!='A'){
          cad_aux += cadena[i]; 
        }
        else{ //caracter leido  = 'A'
          Serial.println(cad_aux);
          cad_aux = "";
        }  
    }//fin for
    Serial.println(cad_aux);
    Serial.println(cadena.length());
    cad_aux = "";
    cadena = "";
  }//fin if que comprueba que la cadena sea completa
  delay(1000);
}//fin del loop
