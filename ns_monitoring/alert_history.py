from influxdb_client import InfluxDBClient

def load_alert_history(rusc_id, bucket, token, org, url, limit=300):
    client = InfluxDBClient(url=url, token=token, org=org)
    query_api = client.query_api()

    query = f'''
    from(bucket: "{bucket}")
      |> range(start: -30d)
      |> filter(fn: (r) => r["rusc_id"] == "{rusc_id}")
      |> sort(columns: ["_time"], desc: true)
      |> limit(n: {limit})
    '''

    tables = query_api.query(query)
    rows = []

    for table in tables:
        for record in table.records:
            rows.append({
                "timestamp": record["_time"],
                "alert_type": record["alert_type"],
                "category": record["category"],
                "severity": record["severity"],
                "confidence": record["confidence"],
                "message": record["message"],
            })

    return rows

