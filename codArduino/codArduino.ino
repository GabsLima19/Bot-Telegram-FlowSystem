//Bibliotecas do arduino
#include <SoftwareSerial.h>

//RX pino 2, TX pino 3
SoftwareSerial esp8266(2, 3);

//Variaveis do Sensor de fluxo
int X;
int Y;
int X2;
int Y2;
float TIME = 0;
float TIME2 = 0;
float FREQUENCY = 0;
float FREQUENCY2 = 0;
float WATER = 0;
float WATER2 = 0;
float TOTAL = 0;
float TOTAL2 = 0;
float LS = 0;
float LS2 = 0;
const int input = A0;
const int input2 = A1;
 
void setup(){
  Serial.begin(9600);
  esp8266.begin(9600);
  pinMode(input,INPUT);
  pinMode(input2,INPUT);
}

void loop()
{
  // Conexão e configuracao fluxo ou vazao (1)
    X = pulseIn(input, HIGH);
    Y = pulseIn(input, LOW);

    X2 = pulseIn(input2, HIGH);
    Y2 = pulseIn(input2, LOW);

    //Calculo o tempo, a frequência, a agua e a quantidade de agua em L/s (1)
    TIME = X + Y;
    TIME2 = X2 + Y2;
    FREQUENCY = 1000000/TIME;
    FREQUENCY2 = 1000000/TIME2;
    WATER = FREQUENCY/7.5;
    WATER2 = FREQUENCY2/7.5;
    LS = WATER/60;
    LS2 = WATER2/60;
   
    // Enviando resultados para o serial
    if(FREQUENCY >= 0){
        if(isinf(FREQUENCY)){
        }
        else{
            Serial.print(LS);
            Serial.print(",");

            esp8266.print(LS);
            esp8266.print(",");
          }
        }

    if(FREQUENCY2 >= 0){
        if(isinf(FREQUENCY2)){
        }
        else{
            Serial.print(LS2);
            Serial.print(";");
            
            esp8266.print(LS2);
            esp8266.print(";");
          }
        }
}
    

        
     
  
