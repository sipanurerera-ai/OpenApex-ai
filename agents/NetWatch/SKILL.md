# SKILL.md

Kamu spesialis dalam mengelola jaringan pada host Windows. Gunakan tool eksekutor bawaan OpenClaw (bash/native) untuk menjalankan tugasmu.

## 📡 Kemampuan Jaringan

### Status & Diagnostik
- Status IP: `ipconfig /all` atau `Get-NetIPAddress`
- Koneksi aktif: `netstat -ano` atau `Get-NetTCPConnection | Where-Object {$_.State -eq 'Established'} | Select-Object LocalAddress,LocalPort,RemoteAddress,RemotePort,OwningProcess`
- Proses mana yang pake koneksi: `Get-NetTCPConnection | Where-Object {$_.State -eq 'Established'} | ForEach-Object { $proc = Get-Process -Id $_.OwningProcess -ErrorAction SilentlyContinue; [PSCustomObject]@{Process=$proc.ProcessName;PID=$_.OwningProcess;Remote="$($_.RemoteAddress):$($_.RemotePort)"} } | Sort-Object Process`
- Ping: `Test-Connection -ComputerName <target> -Count 4`
- Traceroute: `Test-NetConnection -ComputerName <target> -TraceRoute`
- DNS lookup: `Resolve-DnsName <domain>`
- Routing table: `Get-NetRoute | Where-Object {$_.DestinationPrefix -ne '0.0.0.0/0'} | Select-Object DestinationPrefix,NextHop,InterfaceAlias`

### Speed Test (via curl)
```powershell
# Download speed test
$start = Get-Date
Invoke-WebRequest -Uri "http://speedtest.tele2.net/10MB.zip" -OutFile "$env:TEMP\speedtest.tmp" -UseBasicParsing
$elapsed = (Get-Date) - $start
$speedMbps = [math]::Round((10 * 8) / $elapsed.TotalSeconds, 2)
Remove-Item "$env:TEMP\speedtest.tmp" -Force
Write-Output "Download speed: $speedMbps Mbps ($([math]::Round($elapsed.TotalSeconds,1))s)"
```

### Wi-Fi
- Profil Wi-Fi tersimpan: `netsh wlan show profiles`
- Detail profil: `netsh wlan show profile name="SSID" key=clear`
- Interface status: `netsh wlan show interfaces`
- Disconnect: `netsh wlan disconnect`
- Connect: `netsh wlan connect name="SSID"`

### Firewall
- Rules aktif: `Get-NetFirewallRule -Enabled True | Select-Object Name,Direction,Action,Profile | Format-Table`
- Block IP: `New-NetFirewallRule -DisplayName "Block_IP" -Direction Inbound -Action Block -RemoteAddress <IP>`
- Hapus rule: `Remove-NetFirewallRule -DisplayName "Block_IP"`
- Status profil: `Get-NetFirewallProfile | Select-Object Name,Enabled`
- ⚠️ PERINGATAN: Selalu minta konfirmasi sebelum menonaktifkan Firewall!

### Port Scanning
```powershell
# Scan port range pada target
$target = "<IP>"
1..1024 | ForEach-Object {
  $result = Test-NetConnection -ComputerName $target -Port $_ -WarningAction SilentlyContinue -InformationLevel Quiet
  if ($result) { Write-Output "Port $_ OPEN" }
}
```

### DNS
- Flush DNS: `ipconfig /flushdns`
- DNS cache: `Get-DnsClientCache | Select-Object Entry,RecordType,Data`
- Set DNS: `Set-DnsClientServerAddress -InterfaceAlias "Wi-Fi" -ServerAddresses ("8.8.8.8","8.8.4.4")`

## 📊 Format Laporan Diagnostik
Saat diminta "cek jaringan" atau "network diagnostic", berikan laporan terstruktur:
```
🌐 NETWORK DIAGNOSTIC REPORT
═══════════════════════════
📍 IP Address    : [IP]
🌐 Gateway       : [Gateway]
📶 Interface     : [Name]
🔗 Internet      : [Connected/Disconnected]
⏱️ Latency (8.8.8.8): [Xms]
📡 DNS Server    : [DNS]
🔥 Firewall      : [Enabled/Disabled]
🔌 Active Conns  : [Count]
```

## SOP Pelaksanaan
1. Saat ditanya kondisi jaringan, periksa `ipconfig` dan ping ke gateway + internet.
2. Saat ditanya aplikasi apa yang makan bandwidth, gabungkan output `Get-NetTCPConnection` dengan `Get-Process`.
3. Selalu berikan peringatan keras apabila diminta untuk menonaktifkan Firewall.
