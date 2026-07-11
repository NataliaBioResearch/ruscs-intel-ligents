import time

# -----------------------------
# funció auxiliar per enviar alertes
# (pots substituir per Telegram, email, MQTT...)
# -----------------------------
def send_alert(message):
    print(f"[ALERTA] {message}")


# -----------------------------
# alertes de pes
# -----------------------------
def alert_weight(pes):
    if pes is None:
        return

    # caiguda sobtada → possible enjambrament o robatori
    if pes < 5:  # llindar configurable
        send_alert("Pes molt baix detectat — possible enjambrament o robatori.")


# -----------------------------
# alertes de temperatura interna
# -----------------------------
def alert_temp_internal(temp_int):
    if temp_int is None:
        return

    if temp_int < 32:
        send_alert("Temperatura interna baixa — possible problema de cria.")
    elif temp_int > 38:
        send_alert("Temperatura interna alta — possible sobreescalfament del rusc.")


# -----------------------------
# alertes de temperatura externa
# -----------------------------
def alert_temp_external(temp_ext):
    if temp_ext is None:
        return

    if temp_ext < -5:
        send_alert("Temperatura externa molt baixa — risc per a l’activitat.")
    elif temp_ext > 40:
        send_alert("Temperatura externa molt alta — risc de deshidratació.")


# -----------------------------
# alertes de humitat externa
# -----------------------------
def alert_humidity(hum_ext):
    if hum_ext is None:
        return

    if hum_ext < 20:
        send_alert("Humitat externa baixa — risc de sequera.")
    elif hum_ext > 90:
        send_alert("Humitat externa molt alta — risc de fongs o malalties.")


# -----------------------------
# funció principal d’alertes
# -----------------------------
def check_alerts(pes=None, temp_int=None, temp_ext=None, hum_ext=None):
    alert_weight(pes)
    alert_temp_internal(temp_int)
    alert_temp_external(temp_ext)
    alert_humidity(hum_ext)
