import os
import subprocess
import datetime
import random

# --- SETTINGS ---
start_date_str = "2024-08-01"  # --- Change start date ---
start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
end_date = datetime.date.today()
repo_dir = os.getcwd()

# --- GET UNTRACKED FILES (RECURSIVELY) ---
all_files = []
for root, dirs, files in os.walk(repo_dir):
    if '.git' in root:
        continue
    for file in files:
        full_path = os.path.join(root, file)
        relative_path = os.path.relpath(full_path, repo_dir)
        all_files.append(relative_path)

tracked_files = subprocess.check_output(['git', 'ls-files']).decode().splitlines()
untracked_files = list(set(all_files) - set(tracked_files))
random.shuffle(untracked_files)

if not untracked_files:
    print("No untracked files to commit.")
    exit()

# --- PREPARE RANDOMIZED DAILY COMMIT PLAN ---
total_days = (end_date - start_date).days + 1
commit_days = [start_date + datetime.timedelta(days=i) for i in range(total_days)]

# Randomize number of commits per day (some days 0, some days up to 4)
daily_commit_plan = []
remaining_files = len(untracked_files)

for day in commit_days:
    if remaining_files <= 0:
        break
    commits_today = random.randint(0, min(4, remaining_files))
    for _ in range(commits_today):
        hour = random.randint(9, 18)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
        dt = datetime.datetime.combine(day, datetime.time(hour, minute, second))
        daily_commit_plan.append(dt)
        remaining_files -= 1

# Shuffle final commit datetimes so they look natural
daily_commit_plan.sort()
print(f"Total commits planned: {len(daily_commit_plan)}")

# --- MAKE COMMITS ---
for commit_time, file in zip(daily_commit_plan, untracked_files):
    commit_date_str = commit_time.strftime('%Y-%m-%dT%H:%M:%S')
    subprocess.run(["git", "add", file])
    subprocess.run([
        "git", "commit", "-m", f"Add {os.path.basename(file)}"
    ], env={
        **os.environ,
        "GIT_AUTHOR_DATE": commit_date_str,
        "GIT_COMMITTER_DATE": commit_date_str
    })
    print(f"Committed {file} on {commit_date_str}")