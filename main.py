"""
Aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
"""


def ekstraksi_data():
    """
    Tanggal: 12 Mei 2022
    Waktu: 14:22:12 WIB
    Magnitudo: 5.2
    Kedalaman: 116 km
    Lokasi: LS=0.06, BT=123.48
    Pusat Gempa: Pusat gempa berada di laut 74 km Barat Daya Bolaanguki-BolSel
    Dirasakan: Dirasakan (Skala MMI): II-III Gorontalo, II - III Kab. Pulau Taliabu, II - III Luwuk
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '12 Mei 2022'
    hasil['waktu'] = '14:22:12 WIB'
    hasil['magnitudo'] = 5.2
    hasil['kedalaman'] = '116 km'
    hasil['lokasi'] = {'ls': 0.06, 'bt': 123.48}
    hasil['pusat'] = 'Pusat gempa berada di laut 74 km Barat Daya Bolaanguki-BolSel'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): II-III Gorontalo, II - III Kab. Pulau Taliabu, II - III Luwuk'

    return hasil


def tampilkan_data(result):
    print('Gempa Terakhir Berdasakan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat Gempa {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")


if __name__ == '__main__':
    print('Aplikasi Utama')
    result = ekstraksi_data()
    tampilkan_data(result)