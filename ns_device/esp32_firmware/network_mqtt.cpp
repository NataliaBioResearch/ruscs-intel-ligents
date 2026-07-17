#include "network_mqtt.h"
#include <WiFi.h>
#include <PubSubClient.h>

WiFiClient espClient;
PubSubClient client(espClient);

void setup_mqtt() {
    WiFi.begin("SSID", "PASSWORD");
    while (WiFi.status() != WL_CONNECTED) delay(500);

    client.setServer("192.168.1.50", 1883);
    while (!client.connected()) {
        client.connect("ESP32_AUDIO");
        delay(500);
    }
}
void mqtt_publish(const char *topic, uint8_t *data, int len) {
    client.publish(topic, data, len);
}

