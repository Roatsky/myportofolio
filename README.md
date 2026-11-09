Nama : Muhammad Naufal Syarifuddin

NPM : 2506602896

Kelas : PBP F

Website ini merupakan portofolio pribadi saya yang saya kembangkan sebagai proyek untuk tugas 1 PBP Semester Gasal 2026/2027. Portofolio terbagi menjadi 5 bagian. Pertama adalah hook website yang mengandung nama, bio, npm, jurusan, link email, linkedin, dan email. Bagian kedua merujuk pada organisasi, dan kepanitian dahulu yang pernah diikuti. Bagian ketiga merujuk pada proyek-proyek yang pernah saya buat. Bagian keempat masuk kedalam riwayat edukasi dari era smp, sma, dan kuliah S1. Bagian terakhir mengandung skills, terbagi menjadi hard dan soft skills.

Dalam tugas 45 ini saya tidak menggunakan AI. Saya membangun website ini dari template awal yang tim asdos PBP berikan dan saya gunakan template itu serta w3school dan stack overflow untuk membangun rest API kedalam website serta implementasi javascript dan viewsnya dalam repository.

Tugas Refleski:
1. REST API adalah sebuah interface yang memungkinkan dua atau lebih sistem komputer saling berkomunikasi dan bertukar data melalui jaringan berbasis web. Mengembalikan JSON hanya memenuhi serialisasi namun belum memenuhi namun belum memenuhi kriteria REST lain seperti stateless, cacheable, uniform, dll. Put bekerja memperbarui secara seluruh (contoh mengisi ulang semua field) vs patch hanya memperbarui sebagian (contoh mengganti 1 field).

2. Serializer berguna untuk sebagai validasi data yang terpusat, deserialisasi json mentah menjadi objek yang dapat dibaca, menangani relasi antar modal (manytomany atau foreign key), dan menghasilkan serializer.errors yang konsisten. Dari keuntungan yang sudah disebut, bisa dilihat serializer lebih bagus daripada dictionary manual karena dengan validasi terpusat di serializer; consistency, security, dan maintanance lebih mudah dijaga.

3. Autentikasi adalah proses pembuktian siapa itu user sedangkan otorisasi adal proses penentuan user memiliki kuasa apa. Kedua permission ini wajib diadakan dalam server karena jika menutupi tombol, maka itu hanya menghilangkan UI tanpa mencegah pemberian data. Hacker tetap dapat memasuki data lewat backend agar memanipulasi situs dengan cara yang sengaja dilarang dengan autentikasi dan otorisasi.

4. Pentingnya CSRF dalam API adalah SessionAuthentication belum cukup untuk melindungi user. SessionAuthentication hanya mengecek apakah sesi yang sedang berjalan merupakan sesi valid. Jika sesinya valid, situs tidak mengecek apakah input dalam sesi tersebut valid. CSRF digunakan untuk setiap input untuk memastikan input user itu valid. force_authenticate juga tidak cukup untuk membuktikan lindungan CSRF karena lindungan middleware dan autentikasi dilewati, maka CSRF tidak dieksekusi.