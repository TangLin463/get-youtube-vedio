#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess, sys, os

# You need to customize the following two lines of code.
url = "https://www.youtube.com/shorts/D9h9cEvc0GU"
output = "audio.mp3"

proxy = os.environ.get('http_proxy') or os.environ.get('https_proxy')

cmd = ['yt-dlp', '--no-warnings', '-x', '--audio-format', 'mp3']

if proxy:
    cmd += ['--proxy', proxy]

# key parameters for better compatibility with YouTube Shorts
cmd += [
    '--extractor-args', 'youtube:player_client=android,web',  # Try different clients
    '-o', output,
    url
]

print("🎵 正在下载并提取音频...") # downloading and getting audio... 
print("downloading and getting audio...") 
result = subprocess.run(cmd, capture_output=True, text=True)

if result.returncode == 0:
    print("✅ 音频下载成功！") # audio download successful
    print("# audio download successful")
else:
    print("❌ 下载失败 download failed") # download failed
    print("stdout:", result.stdout[-1000:])  # 只显示最后部分 (stdout may contain useful info)
    print("stderr:", result.stderr)

# 下面是如果YouTube有限制，可以手动导出cookie文件，然后再使用。 
# Below is a method to manually export the cookie file and then use it if YouTube has restrictions.
# subprocess.run([
#     'yt-dlp',
#     '-x',
#     '--audio-format', 'mp3',
#     # '--cookies', 'www.youtube.com_cookies.txt',  # 使用导出的 cookies 文件 (use exported cookies file)
#     '-o', output,
#     url
# ])

# subprocess.run([
#     'yt-dlp',
#     '-x',
#     '--audio-format', 'mp3',
#     '--no-check-certificate',  # 跳过证书验证 (skip certificate verification)
#     '--user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
#     '--referer', 'https://www.youtube.com/',
#     '-o', f'{output}.%(ext)s',  # 自动添加扩展名 (automatically add extension)
#     url
# ])
