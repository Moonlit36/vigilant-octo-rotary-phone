# Preparing

## On Windows

Grab a copy of the blog repository, and put it in the "priority-blog" directory:

```bash
git clone git@github.com:miniBill/priority-blog.git
```

## On Linux/macOS

```bash
python3 -m venv .venv
git update-index --skip-worktree .venv/pyvenv.cfg
echo .venv >> .git/info/exclude
source ./.venv/bin/activate
pip install -r requirements.txt
git clone git@github.com:miniBill/priority-blog.git
```

# Running the program

If you get an error that says `Please log in via your web browser`, visit https://www.google.com/accounts/DisplayUnlockCaptcha while logged in with the account you want to use.

## Windows

Doubleclick `start.bat` (don't eat it).

## Linux

```bash
source ./.venv/bin/activate
python blogemailthing.py
```
