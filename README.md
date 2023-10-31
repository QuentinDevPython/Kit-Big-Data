# TaskTracker

## Download requirements

```shell
pip install -r requirements.txt
```

## Shell version


## Django version

For Django, you need to install a few more dependencies.

### Setup

There are two ways to launch the app:

#### 1. Local

```shell
cd django-version/todo_list
pip install -r docker-setup.txt
```

Migrate databases:

```shell
python manage.py makemigrations
python manage.py migrate
```

To launch the server:

```shell
python manage.py runserver
```

#### 2. Docker

If you haven't downloaded Docker yet, please follow the steps through this link: https://docs.docker.com/engine/install/

Then, you can setup the needed Docker container by doing:

```shell
docker-compose up
```

### Accessing the app

When your server is running, you can connect to the ```localhost:8000``` on your browser.




Voici une vue d'ensemble de l'application :   



https://user-images.githubusercontent.com/64276525/204151927-b24fae7b-968e-4209-a1ea-93b2c0c47dd0.mp4  




https://user-images.githubusercontent.com/64276525/204151966-fcd01fad-21d1-4c33-a98b-911cf755d868.mp4  



:bulb: Idée du projet:  
Construire une application permettant de gérer, créer, enrichir et customiser ses playlists spotify.

 :computer: Technologies utilisées:
  - Frontend: Django
  - API: Django
  - Conteneur: Docker
  - Database: PostgreSQL
  - Music: Spotify API using spotipy librairy
  - Image Generation : stable diffusion from keras-CV
  

:musical_note: Trackground:  
Sur trackground vous pouvez connecter votre compte spotify et ainsi accéder à l'ensemble de vos playlists.
Trackground permet de visualiser et créer vos playlists. Vous aurez également la possibilité de découvrir certaines statistiques de vos playlists comme les artistes les plus présents. Trackground implémente également le modèle IA "stable diffusion" de KerasCV. Ce modèle vous permet de générer des illustrations pour vos playlists à partir d'une simple description textuelle comme par exemple: "electro album cover" ou "photograph of a dog on the moon" 
<p>
     <img src="https://github.com/jaillont/app_fullstack_data/blob/main/images/electro.png" width="320" height="320" />
     <img src="https://github.com/jaillont/app_fullstack_data/blob/main/images/metal.png" width="320" height="320" />
     <img src="https://github.com/jaillont/app_fullstack_data/blob/main/images/sunset.png" width="320" height="320" />
     <img src="https://github.com/jaillont/app_fullstack_data/blob/main/images/house.jpg" width="320" height="320" />

</p>

:nut_and_bolt: Lancement de l'application :  


`git clone https://github.com/jaillont/app_fullstack_data.git`  
`cd app_fullstack_data`  
`cd spotify_project`  
`docker-compose up -d --build`  
`docker-compose exec web python manage.py makemigrations user`  
`docker-compose exec web python manage.py migrate user`  
`docker-compose exec web python manage.py makemigrations playlists`  
`docker-compose exec web python manage.py migrate playlists`  
`docker-compose exec web python manage.py migrate`  
`docker-compose up`  

Enfin, se rendre sur l'adresse localhost:8000  

Option 1:  
Sur la page login,  
Attention, avant de se connecter sur l'application connectez vous à l'adresse google suivante:  
Email : trackgrounduser@gmail.com  
Mot de passe : MyPassword123&  
Utilisez les mêmes identifiants sur trackground.  
Une fois connecté vous serez rediriger vers spotify pour accepter la connection et il faut alors se connecter à spotify via le même email en cliquant sur connexion avec google avec les mêmes identifiants. (trackgrounduser@gmail.com et mdp: MyPassword123&)  

Option 2:  
Sinon par la page signup,  
inscrivez vous, puis connectez votre compte spotify en récupérant votre identifiant et l'email de votre compte sur le lien suivant:  
https://www.spotify.com/fr/account/overview/?utm_source=spotify&utm_medium=menu&utm_campaign=your_account  
Attention, il faut bien utiliser le même email pour l'application que pour son compte spotify.  
Avec à ces identifiants, trackground se connecte à l'API de spotify en utilisant la librairie spotipy.  

Sur trackground on retrouve:  

🌓 Light / Dark mode :  
En effet il est possible d'utiliser un mode sombre et même de changer le code couleur de l'application.  

🏠 La page home :  
Une fois connecté, vous arriverez sur cette page de présentation de l'application.  

📂 La page service :  
La page service renvoi vers les différents outils comme la création de playlists ou la génération d'images.  

📫 La page contact :  
Cette page permet de nous contacter par mail depuis l'application. L'envoi des emails est assuré par l'API email de Mailtrap.  

🖼️ La génération d'images :  
Cette page vous permet de générer des images grâce à de simples descriptions d'images, de contexte et de style. Pour chaque prompt, le modèle retourne trois propositions que vous pouvez ou non sauvegarder. Seul bémol la génération peut prendre plusieurs minutes selon les ressources de votre machine.  

🎶 La page playlist :  
Cette page contient l'ensemble de vos playlists, il ne vous reste plus qu'à en sélectioner une pour accéder à l'ensemble de ses musiques. Dans chaque playlist on retrouve les informations importantes comme la durée de la playlist et de chaque musique mais aussi les artistes et la possibilité d'écouter la musique.  

PS : Nous avons rencontré des problèmes avec docker compose sur certains pc, nous ne savons pas l'expliquer. Si jamais vous rencontrez ce problème nous serons ravis de pouvoir vous faire une démonstration.
