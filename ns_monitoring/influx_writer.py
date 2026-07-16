from influxdb_client import InfluxDBClient, Point, WritePrecision

def write_measurement(bucket, token, org, url, measurement, fields, tags=None):
    """
    Escriu una mesura a InfluxDB.

    Args:
        bucket (str): Nom del bucket.
        token (str): Token d'accés.
        org (str): Organització d'InfluxDB.
        url (str): URL del servidor InfluxDB.
        measurement (str): Nom del measurement.
        fields (dict): Diccionari de camps (valors numèrics o strings).
        tags (dict): Diccionari de tags (opcionales).
    """

    client = InfluxDBClient(url=url, token=token, org=org)
    write_api = client.write_api(write_options=None)

    point = Point(measurement)

    if tags:
        for k, v in tags.items():
            point = point.tag(k, v)

    for k, v in fields.items():
        point = point.field(k, v)

    point = point.time(None, WritePrecision.NS)

    write_api.write(bucket=bucket, record=point)
