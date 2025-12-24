# Bash script to reproduce the analyses conducted
# From repo directory 
sudo apt install python3-pip -y
python3 -m venv .venv
source .venv/bin/activate

pip install pandas numpy seaborn matplotlib scipy
python 01_load_clean_data.py
python 02_data_viz.py
python 03_stat_analysis.py