'''
Data Logger for IoT Sensor:
Processing daily sensor data

Tasks:

- Parse each string to extract date, temp, status
- Find the average temp using loop
- Create function analyze_temperature(temp) that return the status based on temp
- Count how many days with 'critical' status (>30C)
- Formatted string for output

This deploys strings, lists, loops, conditionals, functions
'''

# Data format: "2024-01-15,25.3,normal"
sensor_data = [
    "2024-01-15,25.3,normal",
    "2024-01-16,28.7,high", 
    "2024-01-17,22.1,normal",
    "2024-01-18,31.2,critical",
    "2024-01-19,26.8,normal"
]

#Parse setiap string untuk extract tanggal, suhu, status
def split_data(sensor_data):
    data_tanggal = []
    data_suhu = []
    data_status = []

    for data in sensor_data:
        daftar_data = data.split(',')
        data_tanggal.append(daftar_data[0])
        data_suhu.append(daftar_data[1])
        data_status.append(daftar_data[2])
    return data_tanggal, data_suhu, data_status

#Hitung rata-rata suhu menggunakan loop
def hitung_average_suhu(data_suhu):
    count = 0
    nilai_suhu = 0
    for data in data_suhu:
        nilai_suhu = float(data) + nilai_suhu
        count += 1
    average_suhu = float(nilai_suhu / count)
    return average_suhu

#Buat function analyze_temperature(temp) yang return status berdasarkan suhu
def analyze_temperature(data_suhu):
    status_temp = []
    for temp in data_suhu:
        if float(temp) <= 28:
            status_temp.append('Normal')
        elif 28 < float(temp) <= 30:
            status_temp.append('High')
        else:
            status_temp.append('Critical')
    return status_temp

#Count berapa hari status "critical" (>30°C)
def critical_count(data_suhu):
    jumlah_critical = 0
    for data in data_suhu:
        if float(data) > 30.0:
            jumlah_critical += 1
    return jumlah_critical

data_tanggal, data_suhu, data_status = split_data(sensor_data)
print(data_tanggal)
print(data_suhu)
print(data_status)

rata_rata_suhu = hitung_average_suhu(data_suhu)
print(rata_rata_suhu)

display_status = analyze_temperature(data_suhu)
print(display_status)

total_jumlah_critical = critical_count(data_suhu)
print(f'Jumlah suhu yang critical adalah {total_jumlah_critical} kali')

i = 0
for data in sensor_data:
    print(f'Date: {data_tanggal[i]} | Suhu: {data_suhu[i]} | Status: {data_status[i]}')
    i += 1
