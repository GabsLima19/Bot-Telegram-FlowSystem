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
float teste = 0;
 
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
        }
        else{
          if (LS >= 1.00){
            Serial.println("VAZAMENTO!");
            esp8266.println("VAZAMENTO!");
          }
          else {
            Serial.println(LS);
            esp8266.println(LS);
          }
        }
     }
}
