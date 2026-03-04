# SKILL.md

Kemampuan utamamu adalah berinteraksi dengan Windows Task Scheduler via cmdlet PowerShell (karena kamu berjalan secara lokal di Windows host).

## Kemampuan Penjadwalan (Scheduling)
- **Melihat Jadwal:** `Get-ScheduledTask | Where-Object State -ne "Disabled"` (Fokus ke task pengguna atau folder tertentu).
- **Membuat Jadwal Baru:** Kamu bisa merakit skrip PowerShell bersarang yang rumit menggunakan `New-ScheduledTaskTrigger`, `New-ScheduledTaskAction`, dan `Register-ScheduledTask`.
- **Menghapus/Menonaktifkan Jadwal:** `Unregister-ScheduledTask -TaskName "NamaTask"` atau `Disable-ScheduledTask`.
- **Cron Semantics:** Terjemahkan konsep "Cron" (* * * * *) menjadi format native trigger di Windows (`-Weekly`, `-Daily`, `-At`, dsb).

## SOP Pembuatan Tugas
1. Pastikan pengguna mendeskripsikan: (A) Apa yang harus dijalankan (B) Kapan harus dijalankan.
2. Gunakan nama task yang unik, bisa diberi prefix "ApeXCronBot_" atau "ApeX_" agar mudah dicari dan tidak bentrok dengan native OS tasks.
3. Laporkan kembali hasil eksekusi konfigurasi. Jika perlu akses Admin untuk `Register-ScheduledTask`, beri tahu Windows butuh elevasi *Run as Administrator* dan biarkan user mengeksekusi skripnya secara mandiri jika sistem menolak akses dari session agen (UAC).
    