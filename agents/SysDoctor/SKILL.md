# SKILL.md

Senjata diagnostik utamamu bertumpu pada terminal PowerShell lokal yang terintegrasi di OpenApeX.

## Kemampuan Diagnostik Windows
- **Menganalisis CPU/RAM Termenung:**
  `Get-Process | Sort-Object CPU -Descending | Select-Object -First 5`
  `Get-Process | Sort-Object WorkingSet -Descending | Select-Object Name, @{Name="MB";Expression={[math]::round($_.WorkingSet / 1MB, 2)}} -First 5`
- **Mengecek System Uptime:** `(get-date) - (gcim Win32_OperatingSystem).LastBootUpTime`
- **Membaca Event Logs (Critical/Error):** 
  `Get-EventLog -LogName System -EntryType Error -Newest 10`
  `Get-EventLog -LogName Application -EntryType Error -Newest 10`
- **Tindak Lanjut Cepat (Triage):** Jika ada aplikasi tidak penting yang "Not Responding" atau menyedot terlalu banyak memori, matikan paksa menggunakan `Stop-Process -Name "<namaprocess>" -Force`.

## SOP Pemeriksaan Checkup
Jika ditanya kesehatan sistem:
1. Hitung total RAM yang dipakai.
2. Identifikasi 3 proses terberat.
3. Cek Error Event Log Windows 24 jam terakhir.
4. Jangan sekadar numpang baca data sistem, sajikan ke user secara tabular dengan kesimpulan akhir: "Sehat" vs "Kritis".
