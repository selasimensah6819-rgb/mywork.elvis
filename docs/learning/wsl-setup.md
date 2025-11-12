wsl --install -d Ubuntu
wsl -l -v


# Linus Envirnment Setup
sudo apt update && sudo apt -y upgrade
sudo apt -y install git curl build-essential python3 python3-venv python3-pip
git config --global user.name "selasimensah15"
git config --global user.email "selasimensah6819-rgb@icloud.com"
git config --global init.defaultBranch main

# Generate a new SSH key for WSL
ssh-keygen -t ed25519 -C "selasimensah6819-rgb@icloud.com"
# Start the SSH agent
eval "$(ssh-agent -s)"
# Add your WSL SSH key
ssh-add ~/.ssh/id_ed25519_wsl
# Display the public key
cat ~/.ssh/id_ed25519_wsl.pub

# Test SSH connection to GitHub
ssh -T git@github.com

# Clone Github Repo via SSH
mkdir -p ~/code && cd ~/code
git clone git@github.com:selasimensah6819-rgb/mywork.elvis.git
cd mywork.elvis

# Create virtual environment
python3 -m venv .venv
# Activate virtual environment
source .venv/bin/activate
# Upgrade pip
pip install --upgrade pip

# Open project in VS Code using WSL
code .


# Create a branch for WSL setup logs
git checkout -b chore/wsl-setup-logs
# Create documentation folder
mkdir -p docs/learning
# Add your setup log and reflections
nano docs/learning/wsl-setup.md
nano docs/learning/reflections.md
# Stage and commit changes
git add docs/learning
git commit -m "docs: add WSL setup log and reflections"
# Push branch to GitHub
git push -u origin chore/wsl-setup-logs

# Switch to main branch and pull latest
git checkout main
git pull origin main
# List documentation files
ls docs/learning
# Optional: view content
cat docs/learning/wsl-setup.md
cat docs/learning/reflections.md


