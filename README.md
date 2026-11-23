# 📝 Blog Communautaire

Un projet de blog communautaire développé avec **Python et Django** dans le cadre de mon apprentissage du développement web.

L'objectif est de créer une plateforme permettant aux utilisateurs de consulter, rechercher et partager des articles.

## 🚀 Fonctionnalités actuelles

- Affichage de la liste des articles.
- Consultation des détails d'un article.
- Recherche d'articles à partir de leur contenu.
- Navigation entre les différentes pages.
- Templates réutilisables grâce à l'héritage Django.
- Barre de navigation et pied de page communs.

## 🛠️ Technologies utilisées

- Python
- Django
- HTML5
- CSS3
- Git et GitHub

## 📁 Structure du projet

```text
blog_communautaire/
│
├── blog/
│   ├── templates/
│   │   ├── layouts/
│   │   │   ├── base.html
│   │   │   ├── navbar.html
│   │   │   └── footer.html
│   │   ├── index.html
│   │   ├── details.html
│   │   └── search.html
│   │
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   └── admin.py
│
├── blog_communautaire/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/Louisse-prog/blog-communautaire.git
```

### 2. Accéder au projet

```bash
cd blog-communautaire
```

### 3. Créer un environnement virtuel

```bash
python -m venv .venv
```

### 4. Activer l'environnement virtuel

Sous Linux :

```bash
source .venv/bin/activate
```

### 5. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 6. Appliquer les migrations

```bash
python manage.py migrate
```

### 7. Lancer le serveur

```bash
python manage.py runserver
```

Le projet sera accessible à l'adresse :

http://127.0.0.1:8000/

## 🎯 Objectifs d'évolution

Le projet sera progressivement enrichi avec les fonctionnalités suivantes :

- Gestion des utilisateurs et authentification.
- Inscription et connexion.
- Publication et modification d'articles.
- Suppression d'articles.
- Gestion des commentaires.
- Gestion des catégories.
- Stockage des articles dans une base de données.
- Amélioration de l'interface utilisateur.

## 👨‍💻 Auteur

**GLISH-prog**

- GitHub : https://github.com/Louisse-prog

---

*Projet réalisé dans le cadre de mon apprentissage de Django et du développement web.*