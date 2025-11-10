
What I learned 

 how to install and configure WSL2 on Windows.

 how to set up  a Linux development environment with essential tools:Git, Python, pip, and build utilities 

 how to generate an SSH key in WSL, add it to Github, and autheticate securely.

 how to clone a Github repo via SSH and work it inside WSL

 how to create and activate a Python virtual environment for isolated project dependencies 

 how to use VS Code Remote - WSL to edit and run Linux-based project directly from Windows 


Challenges face 

Initial issues with SSH connection, including wrong key usage and a typo in the host (guthub.com instead of github.com).

Installing Python packages (python3-pip and python3-venv) required enabling the universe repository and updating package lists.

Understanding how WSL interacts with Windows, and ensuring VS Code was using the WSL environment instead of the Windows Python environment.


Tips & Recommendations

Always double-check hostnames and paths when working with SSH. Typos can break connections.

Keep your SSH keys organized if you have multiple keys (e.g., system vs WSL).

Use a virtual environment for every project — it avoids conflicts between system and project packages.

Familiarize yourself with WSL and VS Code integration, it’s powerful for Linux development on Windows.

Document your steps — it helps for future setups or sharing knowledge with teammates.
