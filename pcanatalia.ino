//Bibliotecas do arduino
#include <SoftwareSerial.h>

//RX pino 2, TX pino 3
SoftwareSerial esp8266(2, 3);

//Variaveis do Sensor de fluxo
int X;
int Y;
float TIME = 0;
float FREQUENCY = 0;
float WATER = 0;
float TOTAL = 0;
float LS = 0;
const int input = A0;
 
void setup()
{
  Serial.begin(9600);
  esp8266.begin(9600);
  pinMode(input,INPUT);
}
 
void loop()
{
  // Conexão e configuracao fluxo ou vazao
    X = pulseIn(input, HIGH);
    Y = pulseIn(input, LOW);

    //Calculo o tempo, a frequência, a agua e a quantidade de agua em L/s
    TIME = X + Y;
    FREQUENCY = 1000000/TIME;
    WATER = FREQUENCY/7.5;
    LS = WATER/60;
    
    // Enviando resultados para o serial
    if(FREQUENCY >= 0){
        if(isinf(FREQUENCY)){
            Serial.println(" ");
            Serial.print("TOTAL:");
            Serial.print( TOTAL);
            Serial.print(" L");
        }
        else{
            TOTAL = TOTAL + LS;
            Serial.println("VOL.:");
            Serial.print(WATER);
            Serial.print("L/M ");
            Serial.println("TOTAL: ");
            Serial.print( TOTAL);
            Serial.print("L ");
        }
     }

     if(FREQUENCY >= 0){
        if(isinf(FREQUENCY)){
            esp8266.print("VOL. :0.00");
            esp8266.print("TOTAL:");
            esp8266.print( TOTAL);
            esp8266.print(" L");
        }
        else{
            TOTAL = TOTAL + LS;
            esp8266.println("VOL.:");
            esp8266.print(WATER);
            esp8266.print("L/M ");
            esp8266.println("TOTAL: ");
            esp8266.print( TOTAL);
            esp8266.print("L ");
        }
     }
}
