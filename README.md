# CinéTracker
CinéTracker est une application web conteneurisée permettant aux utilisateurs de gérer leur collection de films (vus, à voir, notés, commentés), avec un système complet d’authentification sécurisée par JWT. Ce projet utilise **FastAPI** pour l'API backend et **PostgreSQL** pour la base de données.

## Fonctionnalités principales
-  Authentification JWT (connexion/inscription)
-  Gestion des utilisateurs
-  Gestion des films personnels (CRUD)
-  Titre, genre, année, statut (vu / à voir), note, commentaire
-  Récupération des films par utilisateur
-  Tests unitaires disponibles (à compléter)

## Stack technique
- **Backend** : Python + FastAPI
- **Base de données** : PostgreSQL
- **ORM** : SQLAlchemy
- **Authentification** : JWT 
- **Conteneurisation** : Docker + Docker Compose

## Lancement du projet

https://github.com/AbdelhaK2003/DSIA-5201A.git

cd DSIA-5201A

docker-compose up --build