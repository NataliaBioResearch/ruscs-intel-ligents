#include "opus_encoder.h"
#include "opus.h"

OpusEncoder *encoder;

void setup_opus() {
    int error;
    encoder = opus_encoder_create(16000, 1, OPUS_APPLICATION_AUDIO, &error);
    opus_encoder_ctl(encoder, OPUS_SET_BITRATE(24000));
}

int encode_opus(int16_t *pcm, uint8_t *out, int max_len) {
    return opus_encode(encoder, pcm, 16000, out, max_len);
}

