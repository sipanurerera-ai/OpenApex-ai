# HEARTBEAT.md - Denyut Jantung OpenApeX 🦍

**Pulse & Proactive System**

Ini adalah denyut jantung aku sebagai OpenApeX.  
Setiap kali heartbeat berjalan (default setiap 5–30 menit tergantung konfigurasi), aku akan membaca file ini dan menjalankan semua task yang terdaftar secara otomatis.

Kalau file ini kosong (hanya komentar), heartbeat akan **total dimatikan** — tidak ada panggilan API periodik, tidak ada monitoring otomatis.

Tambahkan task di bawah ini kalau kamu ingin aku **selalu satu langkah di depan** dan aktif mengawal hidup & proyek kamu 24/7.

---

## Cara Kerja Heartbeat

- Aku baca file ini di awal setiap sesi + sesuai interval
- Task dijalankan tepat waktu sesuai schedule
- Hasil heartbeat aku catat di MEMORY.md atau log khusus
- Laporan hanya dikirim kalau penting atau ada perubahan (tidak spam)
- Semua action tetap loyal & sesuai SOUL.md

## Active Heartbeat Tasks

*(Tambahkan atau hapus task di sini. Aku akan update secara otomatis)*

| Schedule              | Priority | Task Name                     | Description                                                                 | Last Run       | Status  |
|-----------------------|----------|-------------------------------|-----------------------------------------------------------------------------|----------------|---------|
| Every 15 minutes      | Critical | Homelab & Device Health       | Cek CPU, RAM, Disk, Temp, GPU, Docker containers di semua server & workstation | -              | Active  |
| Every 30 minutes      | High     | Inbox & Urgent Sweep          | Scan email penting, Telegram, WhatsApp, flag item yang butuh respon cepat   | -              | Active  |
| Every 1 hour          | High     | Calendar & Deadline Check     | Scan agenda hari ini & besok, ingatkan task mendekati deadline              | -              | Active  |
| Daily at 07:00 WIB    | High     | Daily Brief & Agenda          | Ringkasan agenda hari ini + weather Depok + top 3 priority                  | -              | Active  |
| Daily at 23:00 WIB    | Critical | Backup & Sync Verification    | Verifikasi semua backup NAS, Backblaze, Obsidian, Git berhasil              | -              | Active  |
| Every Monday 08:00    | Medium   | Weekly Project Pulse          | Cek progress semua repo, PR open, issue, dependency outdated                | -              | Active  |
| Every 12 hours        | Critical | Security & Anomaly Scan       | Cek login mencurigakan, cert expired, vulnerability dasar                   | -              | Active  |

---

## Template untuk Task Baru

Copy-paste template ini lalu isi:

```markdown
| [Schedule]            | [Priority] | [Task Name]                   | [Description singkat & jelas]                                               | -              | Active  |