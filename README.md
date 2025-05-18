# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institute merupakan institusi pendidikan tinggi yang telah beroperasi sejak tahun 2000. Lembaga ini dikenal karena menerima mahasiswa dari beragam latar belakang. Selain itu, Jaya Jaya Institute menawarkan program perkuliahan pagi dan malam, dengan lebih dari 10 pilihan jurusan yang beragam

### Permasalahan Bisnis
Masalah bisnis yang dihadapi oleh Jaya Jaya Institute adalah tingginya angka mahasiswa yang tidak menyelesaikan pendidikannya (dropout rate). Kondisi ini dipengaruhi oleh banyaknya jurusan yang perlu diawasi serta berbagai faktor lainnya. Situasi tersebut mendorong pihak institusi untuk mengidentifikasi penyebab utama tingginya angka dropout, sehingga langkah-langkah pencegahan dapat diambil secara efektif.

### Cakupan Proyek
1. Menganalisis faktor penyebab tingginya dropout rate.
2. Membuat model machine learning dan prediksi sederhana kemudian di-deploy ke streamlit.
3. Membangun dashboard menggunakan Google Data Studio.

### Persiapan

Sumber data: [Link](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

Setup environment:
1. Membuat environment baru bernama newenv dengan perintah python -m venv newenv
2. Aktivasi environment dengan perintah \newenv\Scripts\activate
3. Menginstal package yang dibutuhkan dengan perintah pip install -r requirements.txt

## Business Dashboard
Dashboard bisnis yang dibuat:
1. Record Count menurut Status: Mengetahui distribusi siswa yang Dropout, Enrolled, dan Graduated.
2. Record Count menurut Scholarship Holder: Melihat jumlah siswa penerima beasiswa dan dampaknya terhadap dropout.
3. Educational Special Needs menurut Record Count: Memahami jumlah siswa berkebutuhan khusus untuk dukungan yang lebih baik.
4. Debtor menurut Record Count: Mengidentifikasi jumlah siswa yang memiliki tunggakan untuk mencegah risiko dropout.
5. [link] https://lookerstudio.google.com/s/hiEU1JDrWIU Dashboard

## Menjalankan Sistem Machine Learning
Langkah-langkah menggunakan sistem machine learning berbasis random forest adalah sebagai berikut.
1. Membuka [link] https://kqzyspzttzq8tix3dappa.streamlit.app/
2. Mengisi inputan prediksi, nilai Course tidak boleh 'None' serta terdapat batas minimum dan maksimum pada input numerik, seperti First semester grade dan second semester grade (maksimal 20). Selain itu, pengguna harus menekan enter atau tab agar data numerik tersimpan. terakhir menekan tombol predict
3. Hasil prediksi akan tampil di bagian bawah.
4. penjelasan pemilihan fitur prediksi, alasan mengapa masing-masing fitur dipilih:
    a. Course
        Program studi atau jurusan berpengaruh terhadap tingkat dropout karena perbedaan tingkat kesulitan, minat mahasiswa, dan lapangan pekerjaan yang tersedia. Misalnya, jurusan dengan kurikulum yang lebih berat cenderung memiliki angka dropout yang lebih tinggi.
    b. Admission Grade
        Nilai masuk mencerminkan kemampuan akademik awal siswa. Mahasiswa dengan nilai rendah saat masuk sering kali kesulitan mengikuti perkuliahan, meningkatkan risiko dropout.
    c. Gender
        Beberapa penelitian menunjukkan bahwa terdapat perbedaan dropout rate antara laki-laki dan perempuan, terutama terkait dengan motivasi, dukungan sosial, dan tanggung jawab di luar kampus.
    d. Age at Enrollment
        Usia saat mendaftar memengaruhi komitmen dan tanggung jawab mahasiswa. Mahasiswa yang lebih tua mungkin memiliki tanggung jawab pekerjaan atau keluarga yang mengganggu studi.
    e. Educational Special Needs
        Mahasiswa dengan kebutuhan pendidikan khusus (special needs) kadang memerlukan dukungan ekstra. Ketiadaan dukungan ini dapat meningkatkan risiko tidak menyelesaikan studi.
    f. Debtor
        Mahasiswa yang memiliki tunggakan biaya sering kali kesulitan melanjutkan pendidikan karena masalah finansial.
    g. Tuition Up to Date
        Pembayaran biaya kuliah yang lancar merupakan indikator mahasiswa tersebut mampu secara finansial, sehingga lebih mungkin untuk menyelesaikan studinya.
    h. Scholarship Holder
        Mahasiswa yang mendapatkan beasiswa cenderung lebih termotivasi dan memiliki dukungan finansial yang baik, sehingga risiko dropout lebih rendah.
    i. First Semester Grade
        Nilai semester pertama menjadi indikator awal adaptasi akademik mahasiswa. Jika nilainya rendah, kemungkinan dropout di semester berikutnya lebih tinggi.
    j. Second Semester Grade
        Sama halnya dengan semester pertama, performa di semester kedua mencerminkan keberlanjutan adaptasi akademik.

## Conclusion
1. Biaya pendidikan terbaru menjadi faktor utama yang memengaruhi siswa untuk dropout. Sebanyak 32,2% siswa dengan biaya pendidikan terbaru memutuskan untuk berhenti studi. Hal ini mungkin disebabkan oleh tingginya biaya yang dianggap memberatkan oleh sebagian mahasiswa. Kondisi ini diperparah ketika biaya yang tinggi mendorong siswa untuk berhutang, di mana 22% dari total siswa yang dropout tercatat memiliki hutang.
2. Sebagian besar penerima beasiswa tidak mengalami dropout, dengan tingkat dropout hanya sebesar 10%.
3. Siswa yang mengalami dropout umumnya menunjukkan penurunan nilai dari semester pertama ke semester kedua.
4. Program studi dengan tingkat dropout tertinggi adalah Biofuel Production Technologies (66,67%), diikuti oleh Equinculture (55,32%) dan Informatics Engineering (54,12%).

### Rekomendasi Action Items
1. Mengevaluasi apakah penetapan biaya pendidikan terbaru sudah tepat dan sesuai dengan kondisi mahasiswa.
2. Memantau mahasiswa yang mengalami penurunan prestasi akademik. Selain itu, langkah perbaikan dapat dilakukan dengan menambah jumlah tenaga pengajar agar pemahaman mahasiswa terhadap materi yang disampaikan meningkat, sehingga risiko dropout dapat diminimalisir.
3. Melakukan analisis terhadap setiap program studi, khususnya pada Biofuel Production Technologies yang memiliki jumlah mahasiswa sedikit (12 orang), namun tingkat dropout yang tinggi. Evaluasi dapat mencakup peninjauan terhadap kualitas pengajaran dan materi yang disampaikan. Jurusan Equinculture juga perlu mendapat perhatian, terutama pada mahasiswa laki-laki, karena tingkat dropout yang tinggi (64,52%) meskipun memiliki jumlah mahasiswa yang relatif sedang, yaitu 62 orang. Di jurusan Informatic Engineering, pengawasan khusus diperlukan pada mahasiswa perempuan, mengingat 6 dari 7 mahasiswi di jurusan tersebut mengalami dropout.
4. Menerapkan batasan usia, misalnya maksimal 50 tahun, sebagai syarat pendidikan.
5. Memperluas jumlah penerima beasiswa agar dapat mengurangi risiko mahasiswa berhutang dan meningkatkan peluang mereka untuk menyelesaikan studi.


