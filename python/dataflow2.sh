wget https://www.python.org/ftp/python/3.7.8/Python-3.7.8.tar.xz
tar xvf Python-3.7.8.tar.xz
cd Python-3.7.8
./configure
sudo make altinstall
cd ..
python3.7 -m venv env
source env/bin/activate


pip3 install -r requirement.txt

python3 test.py --runner=DataFlowRunner --project=named-inn-349004 --temp_location=gs://named-inn-349004/temp --region=us-central1 --job_name test
