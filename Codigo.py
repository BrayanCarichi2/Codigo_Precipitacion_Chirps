import os
import requests

direccion = 'Direccion'

chirps_files = []
for year in range(1981, 2023):
  for month in range(1, 13):
    file_name = f"chirps-v2.0.{year}.{month:02d}.tif.gz"
    url = f"https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_monthly/tifs/{file_name}"
    chirps_files.append(url)

for file_url in chirps_files:
  response = requests.get(file_url, stream=True)
  if response.status_code == 200:
    file_path = os.path.join(direccion, os.path.basename(file_url))
    with open(file_path, 'wb') as file:
      for chunk in response.iter_content(chunk_size=1024):
        if chunk:
          file.write(chunk)
    print(f"Archivo {os.path.basename(file_url)} obtenido correctamente")
  else:
    print(f"Problemas..favor de revisar {os.path.basename(file_url)}. Error: {response.status_code}")