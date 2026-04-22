# Démo CI/CD avec GitHub Actions — Calculatrice Python

Projet de démonstration pour le cours sur l'**automatisation avec GitHub Actions**.

[![Tests](https://github.com/TON-USER/demo-cicd-python/actions/workflows/02-tests-basiques.yml/badge.svg)](https://github.com/TON-USER/demo-cicd-python/actions/workflows/02-tests-basiques.yml)

## Contenu

Une calculatrice Python toute simple, accompagnée de **5 workflows GitHub Actions** progressifs pour comprendre le CI/CD pas à pas.

```
demo-cicd-python/
├── .github/workflows/        ← les 5 workflows (du plus simple au plus avancé)
│   ├── 01-hello-world.yml
│   ├── 02-tests-basiques.yml
│   ├── 03-tests-complets.yml
│   ├── 04-matrix-testing.yml
│   └── 05-deploiement.yml
├── src/
│   └── calculator.py         ← le code de la calculatrice
├── tests/
│   └── test_calculator.py    ← les tests pytest
├── requirements.txt
└── requirements-dev.txt
```

## Lancer les tests en local

```bash
# Installer les dépendances
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Lancer tous les tests
pytest tests/ -v

# Avec mesure de couverture
pytest tests/ --cov=src --cov-report=html
```

## Mise en place sur GitHub

1. Créer un dépôt **public** sur GitHub (ex : `demo-cicd-python`)
2. Cloner localement : `git clone https://github.com/TON-USER/demo-cicd-python.git`
3. Copier tous les fichiers de ce dossier dans le clone
4. Pousser : `git add . && git commit -m "init" && git push`
5. Aller dans l'onglet **Actions** du dépôt → admirer les pipelines tourner ! 🎉

## Démo : déclencher le workflow de déploiement

Le workflow `05-deploiement.yml` se déclenche sur les tags. Pour le tester :

```bash
git tag v1.0.0
git push --tags
```

→ Cela va lancer les tests, builder le package, et créer une **release GitHub** automatiquement.

## Démo : voir un test échouer

Pour montrer en présentation ce qu'il se passe quand un test casse :

1. Modifie `src/calculator.py` : remplace `return a + b` par `return a + b + 1`
2. Commit et push
3. Va dans l'onglet **Actions** → tu verras le workflow échouer avec un ❌

N'oublie pas de remettre le code correct ensuite !
