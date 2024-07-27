
Individual video : https://www.youtube.com/watch?v=7uR3JFYOa7s&ab_channel=iNeuronIntelligence
Also Part of Freecodecamp 30 hour video : https://www.youtube.com/watch?v=mEsleV16qdo&t=94593s


conda create -n sqlGenerator python=3.10 -y

conda activate venv/

pip install -r requirements.txt

create .env file 
kyes=[GOOGLE_API_KEY:"create from https://aistudio.google.com/app/apikey"]

python sqlite.py

streamlit run app.py

conda info --envs

conda deactivate

conda remove venv/