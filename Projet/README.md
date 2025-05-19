# Mini Blog API avec FastAPI et PostgreSQL

Ce projet est une API de mini-blog construite avec FastAPI et PostgreSQL, utilisant une architecture microservices et une authentification JWT.

## 🚀 Fonctionnalités

- Authentification JWT (login/register)
- Gestion des utilisateurs
- Gestion des articles
- Base de données PostgreSQL
- Tests unitaires
- Documentation API automatique (Swagger UI)

## 🛠️ Technologies Utilisées

- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Docker & Docker Compose
- JWT pour l'authentification

## 📋 Prérequis

- Docker
- Docker Compose

## 🔧 Installation et Démarrage

1. Clonez le repository

2. Lancez l'application avec Docker Compose :
   ```bash
   docker-compose up --build
   ```

3. L'API sera accessible à l'adresse : http://localhost:8000
   - Documentation Swagger UI : http://localhost:8000/docs
   - Documentation ReDoc : http://localhost:8000/redoc

## 📝 Endpoints API

### Authentification
- POST `/token` - Obtenir un token JWT
- POST `/users` - Créer un nouvel utilisateur

### Utilisateurs
- GET `/me` - Obtenir les informations de l'utilisateur connecté
- GET `/users` - Liste des utilisateurs

## 🔐 Sécurité

L'API utilise JWT (JSON Web Tokens) pour l'authentification. Pour accéder aux endpoints protégés :
1. Obtenez un token via l'endpoint `/token`
2. Incluez le token dans le header Authorization : `Bearer <votre_token>`

## 💡 Utilisation

Exemple de création d'un utilisateur :
```bash
curl -X POST "http://localhost:8000/users" \
     -H "Content-Type: application/json" \
     -d '{"email":"user@example.com","password":"password123","full_name":"John Doe"}'
```

## 🧪 Tests

Les tests unitaires peuvent être exécutés avec :
```bash
pytest
```

## 📚 Structure du Projet

```
.
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── auth.py
│   └── config.py
├── tests/
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request.

## 📄 Licence

Ce projet est sous licence MIT.