# GHOSTPUSH
⏳ Backdated GitHub Commits — Project Upload Guide

This project demonstrates how to add a local project to GitHub with backdated commit history. It uses a Python script that automatically commits files one by one, simulating activity over a period of time.

The end result is a visually unusual GitHub commit graph with ups and downs, even if the work was done offline or previously. You can set your desired start date and control how the activity shows up on your profile — great for showcasing legacy work or building commit history naturally.

---

## 🛠️ How to Use

### 🔄 Steps:

1. Download this repo’s files (especially `script.py`).

2. Create a new local folder for your project:

    ```bash
    mkdir your-project-name
    cd your-project-name
    git init
    ```

3. Move `script.py` into this folder.

4. Ignore `script.py` and commit `.gitignore` with a past date:

    ```bash
    echo script.py >> .gitignore
    git add .gitignore
    GIT_AUTHOR_DATE="2023-05-31T12:00:00" GIT_COMMITTER_DATE="2023-05-31T12:00:00" git commit -m "Add .gitignore"
    ```

5. Move all your actual project files into this folder.

6. Open `script.py` and update the `start_date` (line 7) to when you want your commit history to begin.

7. Run the script:

    ```bash
    python script.py
    ```

8. Create a GitHub repo online (do not initialize it with README or license).

9. Link your local folder to GitHub:

    ```bash
    git remote remove origin
    git remote add origin https://github.com/your-username/your-repo.git
    git push -u origin main
    ```

---

## 📈 Result

Once pushed, your GitHub profile will reflect the full commit history with dates in the past — creating a realistic and varied contribution graph. Useful for uploading and showcasing offline work as if it were done consistently over time!

---

## 💫 Support

If you found this helpful, please consider **starring ⭐ this repo** or giving a **follow** — your support helps me keep building cool stuff. Thank you! 🙌
