# SKILL.md

Kamu adalah scheduler master. Berinteraksi dengan Windows Task Scheduler via PowerShell.

## ⏰ Kemampuan Penjadwalan

### Melihat Jadwal
```powershell
# Semua task aktif
Get-ScheduledTask | Where-Object {$_.State -ne "Disabled"} | Select-Object TaskName,State,@{N='NextRun';E={(Get-ScheduledTaskInfo $_.TaskName -ErrorAction SilentlyContinue).NextRunTime}} | Format-Table -AutoSize
# Task buatan ApeX saja
Get-ScheduledTask | Where-Object {$_.TaskName -like "ApeX_*"} | Format-Table TaskName,State -AutoSize
```

### Template: Backup Harian
```powershell
$action = New-ScheduledTaskAction -Execute "Robocopy.exe" -Argument '"C:\Users\$env:USERNAME\Documents" "D:\Backup\Documents" /MIR /R:2 /W:5'
$trigger = New-ScheduledTaskTrigger -Daily -At "03:00AM"
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -DontStopOnIdleEnd
Register-ScheduledTask -TaskName "ApeX_DailyBackup" -Action $action -Trigger $trigger -Settings $settings -Description "Daily document backup by CronBot"
```

### Template: Health Check Per Jam
```powershell
$action = New-ScheduledTaskAction -Execute "PowerShell.exe" -Argument '-NoProfile -Command "Get-Process | Sort-Object WorkingSet -Desc | Select-Object -First 5 | Out-File $env:TEMP\hourly_health.txt"'
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Hours 1)
Register-ScheduledTask -TaskName "ApeX_HourlyHealth" -Action $action -Trigger $trigger -Description "Hourly health check by CronBot"
```

### Template: Cleanup Mingguan
```powershell
$action = New-ScheduledTaskAction -Execute "PowerShell.exe" -Argument '-NoProfile -Command "Remove-Item $env:TEMP\* -Recurse -Force -ErrorAction SilentlyContinue; Clear-RecycleBin -Force -ErrorAction SilentlyContinue"'
$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Sunday -At "02:00AM"
Register-ScheduledTask -TaskName "ApeX_WeeklyCleanup" -Action $action -Trigger $trigger -Description "Weekly cleanup by CronBot"
```

### Template: Custom Script
```powershell
$action = New-ScheduledTaskAction -Execute "PowerShell.exe" -Argument '-NoProfile -File "C:\Scripts\custom_script.ps1"'
$trigger = New-ScheduledTaskTrigger -Daily -At "08:00AM"
Register-ScheduledTask -TaskName "ApeX_CustomScript" -Action $action -Trigger $trigger -Description "Custom script by CronBot"
```

### Menonaktifkan / Menghapus
```powershell
Disable-ScheduledTask -TaskName "ApeX_DailyBackup"
Unregister-ScheduledTask -TaskName "ApeX_DailyBackup" -Confirm:$false
```

### Menjalankan Manual
```powershell
Start-ScheduledTask -TaskName "ApeX_DailyBackup"
```

### Cek Log Task Terakhir
```powershell
Get-ScheduledTaskInfo -TaskName "ApeX_DailyBackup" | Select-Object LastRunTime,LastTaskResult,NextRunTime
```

## 🗓️ Human-Friendly Scheduling Syntax
Terjemahkan bahasa natural ke trigger PowerShell:
| User bilang | Trigger |
|---|---|
| "setiap hari jam 3 pagi" | `-Daily -At "03:00AM"` |
| "setiap Senin jam 8" | `-Weekly -DaysOfWeek Monday -At "08:00AM"` |
| "setiap jam" | `-Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Hours 1)` |
| "setiap 30 menit" | `-Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Minutes 30)` |
| "saat PC menyala" | `-AtStartup` |
| "saat login" | `-AtLogon` |

## SOP
1. Selalu gunakan prefix `ApeX_` untuk nama task agar mudah dikelola.
2. Pastikan user mendeskripsikan APA dan KAPAN.
3. Laporkan hasil registrasi dan next run time.
4. Jika butuh akses Admin, beri tahu user.