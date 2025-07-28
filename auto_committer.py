import schedule
import subprocess
import time
import os
from pathlib import Path
from datetime import datetime

SCRIPT_PATH = Path("Path(__file__).parent/staged_commit.sh")

def log(msg: str):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

def auto_commit():
    log("🔄 Triggered auto_commit()")

    # 1. Show Current Working Directory
    cwd = os.getcwd()
    log(f"📁 Current working directory: {cwd}")

    # 2. Check if script exists
    if not SCRIPT_PATH.exists():
        log(f"❌ Script not found at: {SCRIPT_PATH}")
        return
    else:
        log(f"✅ Found script at: {SCRIPT_PATH}")

    # 3. Print environment for safety
    log(f"🛠️ Bash path (env SHELL): {os.environ.get('SHELL', 'Not set')}")
    log(f"🛠️ Bash version (from subprocess):")
    try:
        subprocess.run(["bash", "--version"], check=True)
    except Exception as e:
        log(f"⚠️ Failed to get bash version: {e}")

        # 4. Attempt to run the script
    try:
        log(f"🚀 Executing: bash {SCRIPT_PATH}")
        result = subprocess.run(
            f"bash {SCRIPT_PATH}",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        log(f"📤 Exit Code: {result.returncode}")
        log("✅ Auto-commit executed successfully.")
        log(f"🧾 STDOUT:\n{result.stdout}")
        if result.stderr:
            log(f"⚠️ STDERR:\n{result.stderr}")

        if result.returncode == 3:
            log("📦 No more files left to commit. Exiting.")
            exit(0)

    except subprocess.CalledProcessError as e:
        log(f"❌ CalledProcessError: {e}")
        log(f"Return code: {e.returncode}")
        log(f"Output: {e.output if hasattr(e, 'output') else 'N/A'}")
    except Exception as e:
        log(f"⚠️ Unexpected error: {e}")
# 5. Schedule + run
schedule.every(5).minutes.do(auto_commit)
log("🟢 Auto-committer started. Watching every 5 minutes...")
auto_commit()  # 🔁 Run once immediately

while True:
    schedule.run_pending()
    time.sleep(10)