import subprocess
import sys
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Run yt_playlist_to_json.py
result1 = subprocess.run([sys.executable, 'yt_playlist_to_json.py'], cwd=script_dir)
if result1.returncode != 0:
    print('yt_playlist_to_json.py failed. Exiting.')
    sys.exit(result1.returncode)

# Run yt_to_spotify.py
result2 = subprocess.run([sys.executable, 'yt_to_spotify.py'], cwd=script_dir)
if result2.returncode != 0:
    print('yt_to_spotify.py failed.')
    sys.exit(result2.returncode)

print('Both scripts completed successfully.') 