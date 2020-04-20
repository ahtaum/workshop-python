- enviromtment pada python merupakan hal yang penting mengigat jika sebuah aplikasi yang dibanguna menggunakan python tentunya harus memperhatikan aspek ini.
- karena Aplikasi Python akan sering menggunakan paket dan modul yang tidak datang sebagai bagian dari pustaka standar. Aplikasi kadang-kadang membutuhkan versi perpustakaan tertentu, karena aplikasi mungkin mensyaratkan bug tertentu telah diperbaiki atau aplikasi dapat ditulis menggunakan versi usang dari antarmuka perpustakaan.
- Ini berarti tidak mungkin bagi satu instalasi Python untuk memenuhi persyaratan setiap aplikasi. Jika aplikasi A membutuhkan versi 1.0 dari modul tertentu tetapi aplikasi B membutuhkan versi 2.0, maka persyaratannya bertentangan dan menginstal versi 1.0 atau 2.0 akan membuat satu aplikasi tidak dapat berjalan.

- Solusi untuk masalah ini adalah membuat lingkungan virtual, pohon direktori mandiri yang berisi instalasi Python untuk versi tertentu dari Python, ditambah sejumlah paket tambahan.

- Aplikasi yang berbeda kemudian dapat menggunakan lingkungan virtual yang berbeda. Untuk menyelesaikan contoh sebelumnya dari persyaratan yang saling bertentangan, aplikasi A dapat memiliki lingkungan virtual sendiri dengan versi 1.0 yang diinstal sementara aplikasi B memiliki lingkungan virtual lain dengan versi 2.0. Jika aplikasi B mengharuskan pustaka ditingkatkan ke versi 3.0, ini tidak akan memengaruhi lingkungan aplikasi A.

- ananconda3 adalah sebuah paket manager pada python dan R yang fungsinya menyederhanakan paket-paket tersebut agar mudah dipakai yang tujuannya untuk keperluan komputasi ilmiah.

- Conda memungkinkan kita untuk membuat lingkungan terpisah yang berisi file, paket, dan dependensinya yang tidak akan berinteraksi dengan lingkungan lain.

- promt conda adalah tools penting yang berfungsi untuk menginstall dan mendowload paket manager.

- 	environtment pada conda diberi nama default yaitu base.kita bisa membuat sebuah environment baru pada conda.caranya dengan menggetikan pada promt conda 'conda create --name snowflakes biopython'