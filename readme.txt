1) Installer python3
2) Installer pip
3) pip install requests
4) Prendre un vps ubuntu
5) Mettre tous les fichiers dans le vps
6) Mettre les permissions à tous les fichiers :
chmod +x nom_du_fichier
chmod 777 nom_du_fichier
7) Installer tmux :
sudo apt install tmux
8) Créer une session tmux :
tmux new -s cracker
9) Lancer le cracker dedans :
./cracker
500
10) Quitter la session:
CTRL B + D
11) Attendez les url dans le fichier hits.txt
12) Une fois qu'il y en a beaucoup, les mettre dans list.txt
13) Lancer le main.py :
py main.py
14) Mettre 5 threads
15) Attendre
16) Aller dans le dossier results
17) Aller dans le fichier concerné et prenez le smtp ou le sender sms




( penser à bien mettre all permission ) 
à la créations du vps , installer tmux 
tmux new -s nom
( pour s'y re connecter plus tard : tmux attach-session -t nom )
./cracker
500