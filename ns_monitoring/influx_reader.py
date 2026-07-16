from influxdb_client import InfluxDBClient

def read_measurements(bucket, measurement, token, org, url, start="-24h"):
    client = InfluxDBClient(url=url, token=token, org=org)
    query_api = client.query_api()

    query = f'''
    from(bucket: "{bucket}")
      |> range(start: {start})
      |> filter(fn: (r) => r["_measurement"] == "{measurement}")
      |> sort(columns: ["_time"])
    '''

    tables = query_api.query(query)
    rows = []

    for table in tables:
        for record in table.records:
            rows.append({
                "time": record["_time"],
                "field": record["_field"],
                "value": record["_value"],
                **{k: record[k] for k in record.values if k not in ["_time", "_field", "_value"]}
            })

    return rows

