#include <Bridge.h>
#include <YunServer.h>
#include <YunClient.h>
#include <Process.h>

YunServer server;

int pirPin = 13;
int minbetweenSQLinserts = 1; // min between SQL Inserts
//int msbetweenSQLinserts = minbetweenSQLinserts * 60 * 1000; //convert min to ms

#define beta 4090 //the beta of the thermistor
#define resistance 10 //the value (kilo-ohms) of the pull-down resistor

void setup()
{
  pinMode(pirPin, OUTPUT);
  Bridge.begin();
// Bridge.put("D13","0");
  server.listenOnLocalhost();
  server.begin();
}

void loop()
{
        Bridge.put("D13", "1");
        long a = analogRead(A0);
        //the calculating formula of temperature in C
        float tempC = beta /(log((1025.0 * 10 / a - 10) / 10) + beta / 298.0) - 273.0;
        float tempF = tempC * 1.8 + 32; //convert C to F
        Bridge.put("A0", String(tempF));
        Process p;
        p.runShellCommand("python /usr/lib/python2.7/bridge/bee_insert.py");
        delay(600000);
}

