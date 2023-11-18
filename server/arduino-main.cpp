#include <Ethernet.h>
#include <EthernetUdp.h>
#include <SPI.h>
#include <Servo.h>

byte mac[] = {0x90, 0xA2, 0XDA, 0x00, 0x4A, 0xE0};    // Direccion MAC 
IPAddress ip(192,168,2,55);                           // Direccion IP
char packetBuffer[UDP_TX_PACKET_MAX_SIZE];            // Array para guardar los datos recividos
String receivedData;   // String para guardar los datos recibidos
String sendData = "";
int packetSize;       // Variabl para guardar el tamano del paquete recibido
EthernetUDP UDP;      // UDP Objeto

// Servo motor
Servo myservo;

void setup(){
  Ethernet.begin(mac,ip); // Inicializamos Ethernet
  UDP.begin(5000);  // Inicializamos UDP en el puerto 5000
  myservo.attach(9);
  delay(1500);
}

void loop(){
  packetSize = UDP.parsePacket(); // Obtiene el tamaño del paquete recibido
  if (packetSize > 0) {
    UDP.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE); // leer los datos via UDP
    receivedData = String(packetBuffer);  // convertir la data a string
    if (receivedData == "0") { // Corrección: compara con una cadena en lugar de un carácter
      myservo.write(0);
      sendData = "cerrando...";
    }else if (receivedData == "1") { // Corrección: compara con una cadena en lugar de un carácter
      myservo.write(180);
      sendData = "abriendo...";
    }else{
      sendData = "Dato no valido.";
    }

    UDP.beginPacket(UDP.remoteIP(), UDP.remotePort()); // inicializar paquete para enviar
    UDP.print(sendData);  // enviar el string de vuelta a Python
    UDP.endPacket();  // terminar el paquete
  }
  memset(packetBuffer, 0, UDP_TX_PACKET_MAX_SIZE); // vaciar los valores del array a 0
}