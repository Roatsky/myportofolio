Nama : Muhammad Naufal Syarifuddin

NPM : 2506602896

Kelas : PBP F

Website ini merupakan portofolio pribadi saya yang saya kembangkan sebagai proyek untuk tugas 1 PBP Semester Gasal 2026/2027. Portofolio terbagi menjadi 5 bagian. Pertama adalah hook website yang mengandung nama, bio, npm, jurusan, link email, linkedin, dan email. Bagian kedua merujuk pada organisasi, dan kepanitian dahulu yang pernah diikuti. Bagian ketiga merujuk pada proyek-proyek yang pernah saya buat. Bagian keempat masuk kedalam riwayat edukasi dari era smp, sma, dan kuliah S1. Bagian terakhir mengandung skills, terbagi menjadi hard dan soft skills.

Dalam tugas 45 ini saya menggunakan AI secara minim. Saya membangun website ini dari template awal yang tim asdos PBP berikan dan saya gunakan template itu serta w3school dan stack overflow untuk membangun javascript serta view, url, dan modal untuk akomodasi AJAX. Saya menggunakan AI untuk bug fixing dan pembeneran html agar javascriptnya berjalan tanpa bug.

Tugas Refleski:
1. Debouncing ngecancel panggilan ajax jika ada input baru selama delay yang diberikan. Tujuan ini agar server tidak menerima beberapa input sekaligus dan tidak menganggkat kondisi race

2. Await digunakan sebelum fetch agar kode selanjutnya tidak jalan sebelum fetch selesai proses. Bahaya await dihilangkan adalah ketika kode selanjutnya memperlukan hasil fetch namun fetch belum selesai proses, hasilnya kode selanjut bisa gagal/error tanpa membaca apakah fetch gagal/error atau tidak

3. Cross Site Scripting adalah serangan keamanan web yang bertujuan untuk menyisipkan skrip berbahaya ke website agar data sensitif user dapat diambil. XSS lebih mungkin terjadi menggunakan javascript karena innerHTML dalam java script langsung membaca html yang diberikan sedangkan template django konversikan html yang diberikan agar lebih tidak menggandung karakter sensitif 