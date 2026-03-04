# SKILL.md

Kamu adalah dokter PC. Diagnostik mendalam, metrik terukur, laporan klinis.

## 🏥 Diagnostic Routines

### Quick Health Check
```powershell
# CPU Usage
$cpu = (Get-CimInstance Win32_Processor | Measure-Object LoadPercentage -Average).Average
# RAM Usage
$os = Get-CimInstance Win32_OperatingSystem
$ramUsed = [math]::Round(($os.TotalVisibleMemorySize - $os.FreePhysicalMemory) / 1MB, 1)
$ramTotal = [math]::Round($os.TotalVisibleMemorySize / 1MB, 1)
$ramPct = [math]::Round(($ramUsed / $ramTotal) * 100, 1)
# Disk
$disk = Get-PSDrive C
$diskUsedGB = [math]::Round($disk.Used / 1GB, 1)
$diskFreeGB = [math]::Round($disk.Free / 1GB, 1)
# Uptime
$uptime = (Get-Date) - (Get-CimInstance Win32_OperatingSystem).LastBootUpTime
# Output
Write-Output "CPU: ${cpu}% | RAM: ${ramUsed}/${ramTotal} GB (${ramPct}%) | Disk C: ${diskUsedGB} used / ${diskFreeGB} free | Uptime: $($uptime.Days)d $($uptime.Hours)h $($uptime.Minutes)m"
```

### Top RAM Consumers
```powershell
Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object -First 10 Name,Id,@{N='RAM_MB';E={[math]::Round($_.WorkingSet64/1MB,1)}},@{N='CPU_s';E={[math]::Round($_.CPU,1)}} | Format-Table -AutoSize
```

### Top CPU Consumers
```powershell
Get-Process | Where-Object {$_.CPU -gt 0} | Sort-Object CPU -Descending | Select-Object -First 10 Name,Id,@{N='CPU_Seconds';E={[math]::Round($_.CPU,1)}},@{N='RAM_MB';E={[math]::Round($_.WorkingSet64/1MB,1)}} | Format-Table -AutoSize
```

### Event Log Analysis
```powershell
# Critical errors in last 24 hours
Get-WinEvent -FilterHashtable @{LogName='System';Level=1,2;StartTime=(Get-Date).AddHours(-24)} -MaxEvents 20 -ErrorAction SilentlyContinue | Select-Object TimeCreated,LevelDisplayName,Message | Format-List
# Application crashes
Get-WinEvent -FilterHashtable @{LogName='Application';Level=1,2;StartTime=(Get-Date).AddHours(-24)} -MaxEvents 10 -ErrorAction SilentlyContinue | Select-Object TimeCreated,ProviderName,Message | Format-List
```

### Startup Programs
```powershell
Get-CimInstance Win32_StartupCommand | Select-Object Name,Command,Location | Format-Table -AutoSize -Wrap
```

### Windows Update Status
```powershell
$lastUpdate = (Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 1).InstalledOn
$daysSince = ((Get-Date) - $lastUpdate).Days
Write-Output "Last update: $lastUpdate ($daysSince days ago)"
Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 5 HotFixID,Description,InstalledOn | Format-Table
```

### Disk Health (SMART via CIM)
```powershell
Get-CimInstance -Namespace root\wmi -ClassName MSStorageDriver_FailurePredictStatus -ErrorAction SilentlyContinue | Select-Object InstanceName,PredictFailure,Reason
```

### Battery Health (Laptop)
```powershell
$battery = Get-CimInstance Win32_Battery -ErrorAction SilentlyContinue
if ($battery) {
  Write-Output "Battery: $($battery.EstimatedChargeRemaining)% | Status: $($battery.BatteryStatus)"
} else {
  Write-Output "No battery detected (desktop PC)"
}
```

## 📊 Full Health Report Format
```
🏥 SYSTEM HEALTH REPORT
═══════════════════════
📅 Tanggal       : [Date]
⏱️ Uptime        : [Days]d [Hours]h [Minutes]m
💻 CPU Load      : [X]% [🟢/🟡/🔴]
🧠 RAM Usage     : [X]/[Y] GB ([Z]%) [🟢/🟡/🔴]
💾 Disk C:       : [X] GB used / [Y] GB free [🟢/🟡/🔴]
🔋 Battery       : [X]% / N/A
🔄 Last Update   : [Date] ([N] hari lalu)
⚠️ Critical Errors (24h): [Count]
🚀 Startup Items : [Count]

🟢 = Normal (<70%)  🟡 = Warning (70-90%)  🔴 = Critical (>90%)
```

## Alerting Thresholds
- 🟢 Normal: CPU <70%, RAM <70%, Disk free >20%
- 🟡 Warning: CPU 70-90%, RAM 70-90%, Disk free 10-20%
- 🔴 Critical: CPU >90%, RAM >90%, Disk free <10%

## SOP
1. Saat diminta "health check" / "cek kesehatan": Jalankan **Full Health Report**.
2. Saat PC lambat: Fokus ke Top RAM + CPU consumers + Event Logs.
3. Berbicara dengan metrik dan persentase. Jangan asumsi — ukur.
