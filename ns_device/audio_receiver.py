import socket
import opuslib
import numpy as np
from ns_acoustic.pipeline import run_acoustic_pipeline

class AudioReceiver:
    """
    Rep àudio codificat en Opus via UDP i el processa amb el pipeline acústic.
    """

    def __init__(self, host="0.0.0.0", port=9001, sample_rate=16000, channels=1):
        self.host = host
        self.port = port
        self.sample_rate = sample_rate
        self.channels = channels

        # Decodificador Opus
        self.decoder = opuslib.Decoder(sample_rate, channels)

        # Socket UDP
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((host, port))

    def receive_packet(self):
        """
        Rep un paquet UDP amb dades Opus.
        """
        data, addr = self.sock.recvfrom(4096)
        return data

    def decode_opus(self, opus_data):
        """
        Descomprimeix dades Opus → PCM.
        """
        pcm = self.decoder.decode(opus_data, frame_size=320)
        return np.frombuffer(pcm, dtype=np.int16)

    def process_audio(self, rusc_id="R1", meteo=None):
        """
        Rep, descomprimeix i processa àudio en temps real.
        """
        opus_data = self.receive_packet()
        pcm = self.decode_opus(opus_data)

        # Pipeline acústic complet
        result = run_acoustic_pipeline(
            audio=pcm.astype(float),
            rusc_id=rusc_id,
            meteo=meteo
        )

        return result

