import folium
import pandas as pd

# 导入包，创建一副世界地图

# define the world map
world_map = folium.Map()

# define world map
world_map

# 输入经纬度，尺度
# 旧金山（37.7749°N，122.4194°W）
# San Francisco latitude and longitud values
latitude = 37.77
longitude = -122.42

# Create map and display it
san_map = folium.Map(location=[latitude, longitude], zoom_start=12)

# Display the map of San Francisco
san_map