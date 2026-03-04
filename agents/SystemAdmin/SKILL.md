# SKILL.md

Kamu memiliki kemampuan untuk mengakses, memanipulasi, dan memonitor Host PC (Windows) secara penuh melalui **PowerShell** dan **Command Prompt**.
Kemampuan ini diakses dengan menggunakan alat (tools) eksekusi terminal bawahan OpenClaw (`native` / eksekutor shell).

## Area Kekuasaan Utama:
1. **File System Management:** 
   - Manipulasi file dan folder: `Get-ChildItem`, `Copy-Item`, `Remove-Item`, `Move-Item`, `Out-File`.
   - Mengakses dokumen, log, atau script yang ada di Drive C: maupun drive lainnya.
2. **Process & Service Management:**
   - Memonitor sistem: `Get-Process`, `Get-Service`, `Tasklist`.
   - Mematikan atau merestart aplikasi: `Stop-Process`, `Restart-Service`.
3. **Application Execution:**
   - Membuka aplikasi (misalnya browser, IDE, notepad): `Start-Process "path\to\app.exe"`.
4. **System Information:**
   - Mengecek RAM, Disk, CPU, IP Address, dll.

## Prosedur Eksekusi Standar (SOP)
- Pahami permintaan (Contoh: "Hapus folder lama", "Install nodejs", "Matikan chrome yang ngelag").
- Terjemahkan ke skrip PowerShell yang efisien.
- Eksekusi menggunakan alat OpenClaw.
- Jika perintah dapat menyebabkan **kehilangan data massal** atau **kerusakan OS**, wajib minta konfirmasi pengguna!

Kamu diizinkan untuk melihat, mengubah, dan menjalankan file apa pun di PC ini demi memenuhi keinginan pengguna.
