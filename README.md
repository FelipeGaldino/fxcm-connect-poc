# fxcm-connect-poc
Connect in FXCM

# Create virtual .venv
virtualenv -p="/Library/Frameworks/Python.framework/Versions/3.10/bin/python3" .venv

# Inicia Ambiente
source .venv/bin/activate

# Install requirements
pip3 install -r requirements.txt

# Freeze with libraries used 
pip3 freeze > requirements.txt

# In file "fxcm.cfg" insert your TOKEN of demo or real account.