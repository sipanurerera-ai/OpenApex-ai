# SKILL.md

Otomatisasikan pengaturan PC Windows menggunakan eksekutor PowerShell/Native tool via OpenClaw.

## Kemampuan Context-Switching Cepat
Kamu fasih menggunakan perintah untuk membuka/menutup serangkaian tugas secara berbarengan:
- **Membunuh Distraksi (Do Not Disturb):**
  - Matikan aplikasi spesifik: `Stop-Process -Name "Telegram", "WhatsApp", "Discord", "Spotify" -Force -ErrorAction SilentlyContinue`
- **Membangun Workflow Baru:**
  - `Start-Process "C:\Path\To\Cursor.exe"`
  - Menjalankan npm untuk server lokal jika ditugaskan: `cmd /c "cd /d C:\Path\To\Project && start npm run dev"`
- **Manipulasi OS Instan:**
  - Mute suara secara total: (Bisa menggunakan utilitas ketiga atau nircmd jika tersedia, namun minimal kurangi volume atau sarankan user mengaktifkan Focus Assist Windows).

## SOP Context Switch
Saat pengguna meminta peralihan mode:
1. Pastikan kamu selalu memberitahu **apa saja** yang akan atau baru ditutup agar kerjaan berharga tak hilang jika keliru menutup Word/Excel!
2. Jika ada aplikasi spesifik yang tidak mati, infokan secara terpisah.
3. Kamu **TIDAK** membunuh program yang berhubungan dengan stabilitas OS (svchost, taskhostw) atau OpenClaw (jangan bunuh diri sistem kita sendiri).
