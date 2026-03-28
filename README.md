# get-youtube-vedio / YouTube Video Downloader

**个人使用 YouTube 视频/音频下载工具**（仅供个人学习与备份使用）

*This is a simple YouTube video/audio downloader for **personal use only** (learning and backup).*

---

## 功能 / Features

- `get_vedio_only.py`：仅下载视频（无音频）  *Download video only (no audio)*
- `get_audio.py`：仅下载音频并转为 mp3  *Download audio only and convert to mp3*

**注意**：YouTube 防护机制经常更新，建议定期运行 `yt-dlp -U` 更新工具。  
**Note**： *YouTube's protection mechanisms are frequently updated; it is recommended to run the `yt-dlp -U` update tool regularly.*

---

## 系统要求与安装 *System Requirements & Installation*

在使用前需要安装 **yt-dlp** 和 **FFmpeg** 两个工具。

### Linux（推荐 Ubuntu/Debian）

```bash
sudo apt update
sudo apt install -y yt-dlp ffmpeg
yt-dlp -U                    # 更新到最新版 / Update to the latest version
```
### macOS
```bash
# 安装 Homebrew（如果尚未安装）/ Install Homebrew (if you don't already have it installed).
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

brew install yt-dlp ffmpeg
yt-dlp -U
```
### Windows

```bash
# 以管理员身份打开 PowerShell 执行以下命令安装 Chocolatey（若未安装）/ Open PowerShell as administrator and execute the following command to install Chocolatey (if it is not already installed).
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

choco install yt-dlp ffmpeg -y
yt-dlp -U
```
### 其他 Windows 方式： *Other Windows methods:*

使用 winget：winget install yt-dlp ffmpeg
使用 Scoop：scoop install yt-dlp ffmpeg

## 使用方法 / Usage

1.Clone 或下载本仓库到本地。*Clone or download this repository to your local machine.*  
2.修改脚本中的 url 为你想要下载的 YouTube 链接（每个脚本都需要手动修改）。*Modify the URL in the script to the YouTube link you want to download (this needs to be done manually for each script).*  
3.在终端进入脚本所在目录，运行对应脚本。 *Navigate to the directory containing the script in the terminal and run the corresponding script.*

### 示例命令 *Example Commands*
```bash
# 仅下载视频 / Video only
python get_vedio_only.py

# 仅下载音频 / Audio only
python get_audio.py

```

### 设置代理 / Use Proxy（如果需要 *if needed*）：
代理的端口需要确认自己的设备端口 *The proxy port needs to be confirmed with your device's port settings.*  
```bash
# Linux / macOS
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890

# Windows
set http_proxy=http://127.0.0.1:7890
set https_proxy=http://127.0.0.1:7890
```

## 免责声明 / Disclaimer

- 本项目仅供个人学习、研究和备份使用。*This project is for personal study, research and backup purposes only.*  
- 请遵守 YouTube 的服务条款，不要用于商业用途或大规模下载。*Please comply with YouTube's Terms of Service and do not use this for commercial purposes or for large-scale downloads.*  
- 作者不对因使用本脚本产生的任何问题负责。*The author is not responsible for any problems arising from the use of this script.*


欢迎提交 Issue 或 Pull Request 一起改进！*We welcome submissions of Issues or Pull Requests to help us improve the system!*
