#!/usr/bin/env python3

import influxdb
import json


class CleanInflux(influxdb.InfluxDBClient):
    json_body = []

    def __get__(self):
        return self.json_body

    @staticmethod
    def is_json(data):
        json.loads(data)

    def gen_data(self):
        for i in range(100):
            d, s, r = {}, {}, {}
            d['measurement'] = 'cpu_load_short_{}'.format(str(i))
            s['host'] = 'server0{}'.format(str(i))
            r["region"] = "us-west"
            d['tags'] = {}
            d['tags'].update(s)
            d['tags'].update(r)
            d['time'] = '2009-11-10T23:00:00Z'
            d['fields'] = { 'value' : i}
            CleanInflux.is_json('"'  + str(d) + '"')
            self.json_body.append(d)

    def create_data(self, dbname):
        self.create_database(dbname)
        self.write_points(self.json_body)


if __name__ == "__main__":
    print("Main")
    client = CleanInflux('localhost', 8086, 'root', 'root', 'metrics')
    client.gen_data()
    client.create_data('metrics')
    print(client.json_body)

