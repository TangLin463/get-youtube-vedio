
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 该代码只下载视频，不包括音频 
# This code only downloads the video, not the audio.
import subprocess, sys, os

# You need to customize the following two lines of code.
url = "https://www.youtube.com/shorts/D9h9cEvc0GU" # Enter the link to the video you want to download here.
output = "video_v2.mp4" # This is the output file name; it will be saved to the current folder by default.

proxy = os.environ.get('http_proxy', '').replace('http://', '') # If you can connect directly to YouTube, you can ignore this command. If not, please enable a proxy.

# 获取直接链接 
# get link
result = subprocess.run(['yt-dlp', '-g', url], capture_output=True, text=True)

if result.returncode != 0:
    print("❌ 获取失败") # failed to get
    sys.exit(1)

direct_url = result.stdout.strip().split('\n')[0]
print(f"✅ 获取链接成功\n下载中...") # Downloading...

# FFmpeg 下载（修复代理格式） 
# FFmpeg download (fix proxy format)
subprocess.run([
    'ffmpeg',
    '-http_proxy', f'http://{proxy}',  # 确保有 http:// 前缀  (Ensure http:// prefix)
    '-i', direct_url,
    '-c', 'copy',
    '-y', output
])
