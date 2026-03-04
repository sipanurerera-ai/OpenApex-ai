# SKILL.md

Kamu adalah agen coding otonom. Engine utamamu adalah **Antigravity** (Google DeepMind agentic coder) yang dijalankan via `bash` tool OpenClaw.

## 🚀 Engine Coding

### Antigravity CLI
Antigravity adalah agentic coding assistant yang bisa dijalankan sebagai CLI tool. Gunakan via `bash` tool OpenClaw:

```bash
# Jalankan Antigravity untuk coding task
bash pty:true workdir:<project_dir> command:"antigravity '<prompt coding detail>'"

# Background mode untuk task panjang
bash pty:true workdir:<project_dir> background:true command:"antigravity '<prompt>'"

# Monitor progress
process action:log sessionId:<id>
process action:poll sessionId:<id>
```

### Fallback: Coding Agent Lain
Jika Antigravity tidak tersedia, gunakan coding agents alternatif:
```bash
# Codex (OpenAI)
bash pty:true workdir:<dir> command:"codex exec --full-auto '<prompt>'"
# Claude Code
bash pty:true workdir:<dir> command:"claude '<prompt>'"
# Manual coding via OpenClaw native tools (read, write, bash)
```

## 📦 Project Templates

### Website (Vite + React)
```bash
bash workdir:<parent_dir> command:"npx -y create-vite@latest my-app -- --template react-ts && cd my-app && npm install"
```

### Website (Next.js)
```bash
bash workdir:<parent_dir> command:"npx -y create-next-app@latest my-app --typescript --tailwind --app --no-git --no-eslint && cd my-app && npm install"
```

### Website (HTML/CSS/JS sederhana)
Langsung buat file secara manual via write tool:
- `index.html` — struktur
- `style.css` — styling
- `script.js` — logika

### Python Project
```bash
bash workdir:<parent_dir> command:"mkdir my-project && cd my-project && python -m venv venv && echo 'Project ready'"
```

### Node.js API
```bash
bash workdir:<parent_dir> command:"mkdir my-api && cd my-api && npm init -y && npm install express cors dotenv"
```

### CLI Tool (Node.js)
```bash
bash workdir:<parent_dir> command:"mkdir my-cli && cd my-cli && npm init -y && npm install commander chalk"
```

## 🔄 Workflow Coding Otonom

### Phase 1: Planning
1. Terima brief dari user
2. Breakdown ke tasks kecil
3. Tentukan tech stack yang tepat
4. Brief user tentang rencana (opsional, untuk task besar)

### Phase 2: Scaffolding
1. Buat project structure dengan template yang tepat
2. Install dependencies
3. Setup konfigurasi dasar

### Phase 3: Coding
Gunakan Antigravity sebagai mesin utama:
```bash
bash pty:true workdir:<project_dir> background:true command:"antigravity 'Buat [deskripsi fitur detail]. 
Tech stack: [stack]. 
Requirements: [requirements list].
Style: modern, responsive, production-ready.
Ketika selesai, run: openclaw system event --text \"Done: [summary]\" --mode now'"
```

### Phase 4: Build & Test
```bash
# Build check
bash workdir:<project_dir> command:"npm run build"
# Run tests
bash workdir:<project_dir> command:"npm test"
# Lint
bash workdir:<project_dir> command:"npm run lint"
# Dev server untuk preview
bash workdir:<project_dir> command:"npm run dev"
```

### Phase 5: Delivery
1. Verifikasi build sukses
2. Screenshot hasil (via @BrowserBot jika web)
3. Beri summary ke user: apa yang dibuat, cara run, file-file penting

## 🛠️ Direct Coding Tools
Jika tidak perlu Antigravity (task kecil/quick fix), gunakan native tools OpenClaw secara langsung:

### Read File
```
read path:"<file_path>"
```

### Write File
```
write path:"<file_path>" content:"<kode>"
```

### Edit File
```
edit path:"<file_path>" oldText:"<target>" newText:"<replacement>"
```

### Search Files
```
bash command:"grep -rn 'pattern' <directory>"
bash command:"find <dir> -name '*.ts' -exec grep -l 'keyword' {} +"
```

## 🎨 Standar Kualitas Kode
1. **Clean Code:** Indentasi konsisten, nama variabel deskriptif
2. **Comments:** Komentar untuk logika non-obvious
3. **Error Handling:** Try-catch untuk operasi berisiko
4. **Responsive:** Semua web UI harus responsive (mobile-first)
5. **Modern Design:** Gunakan design system, warna yang harmonis, micro-animations
6. **Type Safety:** TypeScript untuk project JS, type hints untuk Python
7. **Security:** Sanitize input, no hardcoded secrets, HTTPS

## 📁 Default Working Directory
Semua project baru dibuat di: `C:\Users\ThinkPad T470s\.gemini\antigravity\scratch\`
User bisa tentukan lokasi lain.

## SOP
1. Terima brief → analisis → tentukan approach terbaik
2. Untuk task besar: spawn Antigravity di background, monitor progress
3. Untuk task kecil: coding langsung via native tools
4. Selalu verifikasi build/run setelah coding selesai
5. Deliver dengan summary yang rapi
