import requests

# 国土交通省道路局 交通量API
# 指定した座標の範囲と時間の交通量を出力

# エンドポイント
API_URL  = "https://api.jartic-open-traffic.org/geoserver"

params = {
    # 交通量API仕様書通りに指定
    'service': 'WFS',
    'version': '2.0.0',
    'request': 'GetFeature',
    'typeNames': 't_travospublic_measure_5m',  # 常設トラカンの5分間交通量
    'srsName': 'EPSG:4326',
    'outputFormat': 'application/json',
    'exceptions': 'application/json',
    # 道路種別は3(一般国道)を指定
    # 時間コードで2025/05/20 12:00を指定
    # 常時観測点コードで千葉を指定
    'cql_filter': "道路種別='3' AND 時間コード=202505201200 AND BBOX(ジオメトリ,139.52,34.53,140.52,36.06,'EPSG:4326')"
}

response = requests.get(API_URL, params=params)
# Process the response
data = response.json()
print(data)
