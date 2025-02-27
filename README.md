# Cloud Microservices

Vous pouvez accéder à la pipeline CI/CD dans l'onglet "Actions" pour vérifier le bon fonctionnement du projet. Cela vous permettra de suivre les étapes de déploiement et de vous assurer que tout fonctionne correctement.

Ce projet est une architecture de microservices déployée sur Minikube avec Istio comme gateway. Il est composé de trois services principaux : un service de calcul, un service de logging et une base de données MariaDB.

## Table des matières

1. [Introduction](#introduction)
2. [Architecture](#architecture)
3. [Services](#services)
   - [Calculateur Service](#calculateur-service)
   - [Logger Service](#logger-service)
   - [DB Service](#db-service)
4. [Déploiement](#déploiement)
5. [Utilisation](#utilisation)
6. [Pipeline CI/CD](#pipeline-cicd)
7. [Contribution](#contribution)

## Introduction

Ce projet vise à démontrer une architecture de microservices en utilisant Minikube et Istio. Il permet d'effectuer des calculs simples et de stocker les résultats dans une base de données.

## Architecture

Le projet est composé de trois services :
- **Calculator Service** : Une API Flask en Python qui effectue des opérations mathématiques de base.
- **Logger Service** : Une API Flask en Python qui reçoit les résultats des calculs et les stocke dans une base de données.
- **DB Service** : Une base de données MariaDB qui stocke les résultats des calculs.

## Services

### Calculateur Service

Le Calculateur Service est une API Flask qui expose les routes suivantes :
- `GET /calculator/add?val1=<value1>&val2=<value2>` : Additionne deux valeurs.
- `GET /calculator/subtract?val1=<value1>&val2=<value2>` : Soustrait deux valeurs.
- `GET /calculator/multiply?val1=<value1>&val2=<value2>` : Multiplie deux valeurs.
- `GET /calculator/divide?val1=<value1>&val2=<value2>` : Divise deux valeurs.

### Logger Service

Le Logger Service est une API Flask qui reçoit les résultats des calculs via une requête POST à la route `/log/update` et les stocke dans la base de données MariaDB. Il expose également une route pour récupérer les données stockées :
- `POST /log/update` : Stocke le résultat d'un calcul dans la base de données.
- `GET /log/data` : Récupère tous les résultats stockés dans la base de données.

### DB Service

Le DB Service est une instance MariaDB qui stocke les résultats des calculs envoyés par le Logger Service.

## Déploiement

Pour déployer ce projet en local, vous devez avoir Minikube et Istio installés sur votre machine, et suivre les étapes de la pipeline CI/CD. Vous pouvez également simplement vérifier l'onglet action de github avec le dernier build correct. 

## Utilisation

Une fois les services déployés, vous pouvez utiliser l'API en envoyant des requêtes HTTP aux différentes routes exposées par les services. Par exemple :

- Pour additionner deux valeurs : `GET http://<minikube-ip>/calculator/add?val1=10&val2=20`
- Pour récupérer les résultats stockés : `GET http://<minikube-ip>/log/data`


