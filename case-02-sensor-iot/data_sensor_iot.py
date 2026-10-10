import random
import time


def generator_suhu(jumlah_data=15):
    """Menghasilkan data suhu secara bertahap."""
    for _ in range(jumlah_data):
        suhu = round(random.uniform(15.0, 38.0), 2)
        yield suhu


def kategorisasi_suhu(suhu):
    if suhu < 20.0:
        return "Dingin"
    elif 20.0 <= suhu <= 30.0:
        return "Normal"
    else:
        return "Panas"


def jalankan_streaming_sensor():
    jumlah_data = 15
    data_sensor = generator_suhu(jumlah_data)

    print("SISTEM STREAMING DATA SENSOR IoT")
    print("Pemantauan Suhu Lingkungan")
    print("-" * 43)
    print(f"{'No.':<6}{'Suhu (°C)':<15}{'Kategori Status'}")
    print("-" * 43)

    nomor = 1

    while nomor <= jumlah_data:
        suhu = next(data_sensor)
        status = kategorisasi_suhu(suhu)

        print(f"{nomor:<6}{suhu:<15.2f}{status}")

        nomor += 1
        time.sleep(0.3)

    print("-" * 43)
    print("Aliran data sensor telah selesai.")
    print(f"Total pembacaan: {jumlah_data}")
    print()


if __name__ == "__main__":
    jalankan_streaming_sensor()