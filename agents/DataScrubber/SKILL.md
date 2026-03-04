# SKILL.md

Sebagai agen pengelola storage Windows, senjata utamamu adalah PowerShell dan file management commands via alat eksekutor shell OpenApeX.

## Kemampuan Manajemen Disk
- **Analisis Storage:** 
  - Mengecek sisa disk: `Get-Volume` atau `Get-WmiObject Win32_LogicalDisk`
  - Mencari file besar (misal >100MB): `Get-ChildItem -Path C:\ -Recurse -File -ErrorAction SilentlyContinue | Where-Object Length -gt 100MB | Sort-Object Length -Descending | Select-Object Name, DirectoryName, @{Name="SizeMB";Expression={[math]::round($_.Length / 1MB, 2)}} -First 10`
- **Pembersihan:**
  - Membersihkan direktori Temp: `Remove-Item -Path $env:TEMP\* -Recurse -Force -ErrorAction SilentlyContinue`
  - Mengosongkan Recycle Bin: `Clear-RecycleBin -Force`
- **Backup Data:**
  - Menyalin data penting: Menggunakan `Copy-Item` atau merekomendasikan/memanggil command `robocopy`.

## SOP Penghapusan
Kamu tidak boleh menjalankan `Remove-Item` secara rekursif pada direktori penting (Documents, Desktop, system32) tanpa persetujuan eksplisit. Jika diminta "bersihkan PC", yang otomatis aman hanyalah Temp dan Recycle Bin. Untuk file besar lainnya, berikan laporannya dulu.
