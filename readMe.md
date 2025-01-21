#CV Generator
Cv Generator est un programme développé en Python.
Ce projet a été créé dans un but expérimental de manipulation de fichiers Word à l'aide de Python.
Fonctionnement du programme
Ce programme s'exécute dans un terminal. Afin de générer son CV à partir d'un modèle prédéfini, l'utilisateur devra renseigner les champs qui s'affichent à l'écran. Si la saisie est incorrecte, un message d'erreur apparaît et l'utilisateur est invité à saisir de nouveau l'information demandée.
Une fois toutes les informations saisies, l'utilisateur est invité à nommer son fichier pour l'enregistrer.

##Description des fichiers
###main.py
Ce fichier est le fichier principal ; il permet de lancer le programme.

###cv_generator.py
Ce fichier contient les fonctions qui permettent la saisie des informations.


###file_generator.py
Ce fichier contient les fonctions permettant de formater les données saisies et de les copier dans un fichier Word.

###functions.py
Ce fichier contient des fonctions de validation personnalisées pour permettre la validation des données saisies.
##Bibliothèque Python
python-docx


##Installation du projet

###Cloner le projet
git clone

###Vérifier que Python3 est installé
python --version

###Créer un environnement virtuel Python
python3 -m venv env

###Activer l'environnement virtuel
source env/bin/activate

###Importer les bibliothèques
pip install -r requirements.txt

###Lancer le programme
python3 main.py
