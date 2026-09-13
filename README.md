Nama : Muhammad Naufal Syarifuddin

NPM : 2506602896

Kelas : PBP F

Website ini merupakan portofolio pribadi saya yang saya kembangkan sebagai proyek untuk tugas 1 PBP Semester Gasal 2026/2027. Portofolio terbagi menjadi 4 bagian. Pertama adalah hook website yang mengandung nama, bio, npm, jurusan, link email, linkedin, dan email. Bagian kedua masuk kedalam riwayat edukasi dari era smp, sma, dan kuliah S1. Bagian ketiga mengandung skills, terbagi menjadi hard dan soft skills. Bagian terakhir merujuk pada proyek, organisasi, dan kepanitian dahulu yang pernah diikuti.

Pembuatan website ini saya menggunakan AI secara minim. Saya membangun website ini dari template awal yang tim asdos PBP berikan untuk bagian bio website dan saya gunakan template itu serta w3school dan stack overflow untuk membangun bagian skills, experience, dan education. Saya juga bertanya dengan gemini dalam pembangunan test tanpa meminta gemini menulis langsung dan menggunakan untuk bug fix soal pws dan models.

Pertanyaan Refleksi
1. Saat pemmbukaan website, website melihat url dan memanggil html berdasarkan url. urls.py bekerja untuk menerima panggilan url dan mencocokan dengan object view yang sesuai. views.py menerima panggilan url dan mencocokan panggilan url dengan model yang sesuai. models.py bekerja untuk menerima panggilan view untuk menampilkan sebuah object dan mengembalikan object dalam data model yang sesuai dengan panggilan views. views.py menggunakan data dari model dan mencocokan data itu kedalam html yang ada di views.py lalu mencocokan data kedalam html sesuai perintah html. urls.py menerima hasil html ini dan mengembalikan html ke browser untuk ditayangkan.

2. Penggunaan model dibanding hard code sangat membantu pembuatan website dalam maintanance dan penambahan data. Dengan data ditambahkan lewat shell, programmer hanya perlu memikirkan soal menulis data baru serta modifikasi data lama jika perlu, data-data yang sudah ada di model yang tidak sedang diotak-atik dapat dibiarkan dan programmer punya keyakinan bahwa display mereka tidak akan terganggu. Tidak memperlukan hardcode juga membantu kode html lebih singkat dan repeateable.

3. Makemigration hanya membuat folders berisi kode tentang instruksi cara membuat sql table tanpa mengeksekusi datanya. Migrate mengeksekusi data agar data muncul di table database. Makemigration digunakan ketika kode model sendiri ada yang diedit sedangkan migrate digunakan ketika data di table ada yang diubah atau ada data baru.