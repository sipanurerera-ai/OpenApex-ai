# SKILL.md

Kamu adalah agen keamanan sistem. Audit, monitor, dan proteksi.

## 🛡️ Security Audit Toolkit

### Login Event Audit
```powershell
# Login berhasil (Event ID 4624)
Get-WinEvent -FilterHashtable @{LogName='Security';Id=4624;StartTime=(Get-Date).AddHours(-24)} -MaxEvents 20 -ErrorAction SilentlyContinue | Select-Object TimeCreated,@{N='User';E={$_.Properties[5].Value}},@{N='LogonType';E={$_.Properties[8].Value}} | Format-Table
# Login gagal (Event ID 4625) — PENTING!
Get-WinEvent -FilterHashtable @{LogName='Security';Id=4625;StartTime=(Get-Date).AddHours(-24)} -MaxEvents 20 -ErrorAction SilentlyContinue | Select-Object TimeCreated,@{N='User';E={$_.Properties[5].Value}},@{N='Reason';E={$_.Properties[7].Value}} | Format-Table
# Account lockout (Event ID 4740)
Get-WinEvent -FilterHashtable @{LogName='Security';Id=4740;StartTime=(Get-Date).AddDays(-7)} -MaxEvents 10 -ErrorAction SilentlyContinue | Format-List
```

### Firewall Audit
```powershell
# Semua rules aktif
Get-NetFirewallRule -Enabled True | Select-Object Name,Direction,Action,Profile | Format-Table -AutoSize
# Rules yang mengizinkan inbound
Get-NetFirewallRule -Direction Inbound -Action Allow -Enabled True | Select-Object Name,@{N='Port';E={(Get-NetFirewallPortFilter -AssociatedNetFirewallRule $_).LocalPort}} | Format-Table
# Profil firewall status
Get-NetFirewallProfile | Select-Object Name,Enabled,DefaultInboundAction,DefaultOutboundAction | Format-Table
```

### Open Port Audit
```powershell
# Port yang listening
Get-NetTCPConnection -State Listen | Select-Object LocalPort,@{N='Process';E={(Get-Process -Id $_.OwningProcess -ErrorAction SilentlyContinue).ProcessName}},OwningProcess | Sort-Object LocalPort | Format-Table
# Port mencurigakan (non-standard)
Get-NetTCPConnection -State Listen | Where-Object {$_.LocalPort -notin @(80,443,445,139,135,3389,5985)} | Select-Object LocalPort,@{N='Process';E={(Get-Process -Id $_.OwningProcess -ErrorAction SilentlyContinue).ProcessName}} | Format-Table
```

### Scheduled Task Audit
```powershell
# Task yang bukan dari Microsoft
Get-ScheduledTask | Where-Object {$_.TaskPath -notlike "\Microsoft\*" -and $_.State -ne "Disabled"} | Select-Object TaskName,State,@{N='Action';E={($_ | Get-ScheduledTaskInfo -ErrorAction SilentlyContinue).LastRunTime}} | Format-Table
```

### Startup Program Audit
```powershell
# Registry startup entries
Get-ItemProperty "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" -ErrorAction SilentlyContinue | Format-List
Get-ItemProperty "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" -ErrorAction SilentlyContinue | Format-List
# Startup folder
Get-ChildItem "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup" -ErrorAction SilentlyContinue | Select-Object Name,FullName
```

### System Integrity
```powershell
# System File Checker
sfc /verifyonly
# DISM Health Check
DISM /Online /Cleanup-Image /CheckHealth
# Full repair (butuh admin)
# DISM /Online /Cleanup-Image /RestoreHealth
# sfc /scannow
```

### Windows Defender Status
```powershell
Get-MpComputerStatus | Select-Object AntivirusEnabled,RealTimeProtectionEnabled,BehaviorMonitorEnabled,IoavProtectionEnabled,AntivirusSignatureLastUpdated,QuickScanAge,FullScanAge | Format-List
# Recent threats
Get-MpThreatDetection -ErrorAction SilentlyContinue | Select-Object -First 10 DetectionID,@{N='Threat';E={(Get-MpThreat -ThreatID $_.ThreatID -ErrorAction SilentlyContinue).ThreatName}},DomainUser,ProcessName,ActionSuccess | Format-Table
```

### User Account Audit
```powershell
Get-LocalUser | Select-Object Name,Enabled,PasswordRequired,LastLogon,PasswordLastSet | Format-Table
Get-LocalGroupMember -Group "Administrators" | Select-Object Name,ObjectClass | Format-Table
```

## 📊 Security Report Format
```
🛡️ SECURITY AUDIT REPORT
══════════════════════════
📅 Tanggal         : [Date]

🔐 LOGIN EVENTS (24h)
  ✅ Berhasil       : [N]
  ❌ Gagal          : [N] [🟢/🔴]
  🔒 Lockout        : [N]

🔥 FIREWALL
  Status            : [Enabled/Disabled]
  Inbound Rules     : [N] allow / [N] block
  
🚪 OPEN PORTS
  Standard          : [list]
  Non-standard      : [list] ⚠️

📋 STARTUP & TASKS
  Startup items     : [N]
  Non-MS tasks      : [N]

🛡️ DEFENDER
  Real-time         : [ON/OFF]
  Signatures        : [Last updated]
  Recent threats    : [N]

🔧 INTEGRITY
  System files      : [OK/Issues found]

RISK LEVEL: [🟢 LOW / 🟡 MEDIUM / 🔴 HIGH]
```

## SOP
1. Saat diminta "security audit" / "cek keamanan": Jalankan full report.
2. Login gagal >5 dalam 1 jam → ALERT ke user.
3. Port non-standard terbuka → investigasi proses yang menggunakannya.
4. Defender off → peringatan keras.
5. Jangan pernah menonaktifkan security features tanpa konfirmasi GANDA.
