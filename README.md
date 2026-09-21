Nama : Muhammad Naufal Syarifuddin

NPM : 2506602896

Kelas : PBP F

Website ini merupakan portofolio pribadi saya yang saya kembangkan sebagai proyek untuk tugas 1 PBP Semester Gasal 2026/2027. Portofolio terbagi menjadi 4 bagian. Pertama adalah hook website yang mengandung nama, bio, npm, jurusan, link email, linkedin, dan email. Bagian kedua masuk kedalam riwayat edukasi dari era smp, sma, dan kuliah S1. Bagian ketiga mengandung skills, terbagi menjadi hard dan soft skills. Bagian terakhir merujuk pada proyek, organisasi, dan kepanitian dahulu yang pernah diikuti.

Dalam tugas 3 ini saya tidak menggunakan AI. Saya membangun website ini dari template awal yang tim asdos PBP berikan untuk bagian bio website dan saya gunakan template itu serta w3school dan stack overflow untuk membangun bagian halaman form untuk skills, experience, dan education.

Pertanyaan Refleksi
1. Model form digunakan daripada hardcode html mirip dengan mengapa kita menggunakan model. Modelform lebih aman, lebih dinamis, lebih mudah dimodifikasi, dan sudah integrasi ke django model. {% csrf_token %} perlu ditambahkan agar ada token yang memproteksi dari serangan csrf, yaitu serangan dimana pihak luar memberikan request ke kita dan karena kita tidak tahu itu dari luar, kita isi.

2. JSON digunakan daripada html karena JSON lebih kecil (gak ada tag penutup), lebih cepat (karena dapat diparse menjadi javascript), serta lebih mudah dibaca untuk manusia maupun komputer (karena lebih singkat).

3. Awal alur dimulai dengan show_x (dimana x bisa experience, project, education, atau skills) yang meminta get_x_json. get_x_json mengambil title_query sesuai yang direquest user dan variabel yang merupakan query set berisi semua object dalam 1 modal. Variabel ini difilter agar menghasilkan object yang mengandung title sesuai title_query (semuanya jika title_query kosong) dan mengirimnya ke server melalui httpresponse sebagai json file, yang akhirnya akan dideserialize di show_x. Objects ini perlu diserialize saat pengiriman keserver agar object (yang awalnya query set) menjadi format yang lebih sederhana agar dapat dimengerti browser