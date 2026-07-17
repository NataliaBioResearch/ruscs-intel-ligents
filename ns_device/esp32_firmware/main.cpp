#include "i2s_config.h"
#include "opus_encoder.h"
#include "network_mqtt.h"

uint8_t opus_buffer[4000];

void setup() {
    setup_i2s();
    setup_opus();
    setup_mqtt();
}

void loop() {
    int16_t pcm_buffer[16000];
    size_t bytes_read;

    // Captura 1 segon d'àudio
    i2s_read(I2S_NUM_0, pcm_buffer, sizeof(pcm_buffer), &bytes_read, portMAX_DELAY);

    // Codifica a Opus
    int opus_len = encode_opus(pcm_buffer, opus_buffer, sizeof(opus_buffer));

    // Envia via MQTT
    mqtt_publish("rusc/audio", opus_buffer, opus_len);

    delay(10);
}

