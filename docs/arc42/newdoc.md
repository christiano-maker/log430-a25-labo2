# Broker X - Documentation d'Architecture
Ce document, basé sur le modèle arc42, décrit une application de gestion de magasin pour le Labo 01, LOG430.

## 1. Introduction et Objectifs

### Panorama des exigences
L'application Broker X a pour but principal d'offrir à des investisseurs particuliers une plateforme de courtage. Elle doit intégrer des fonctionnalitées telles ques: 
- La création de compte et la vérification d'identité
- L'approvisionnement du portefeuille virtuel
- La possibilité d'interageir avec des marchés financiers simulés

Nous nous assererons que ce projet soit concu de facon à pouvoir évoluer facilement à travers les diverses phases.


### Objectifs qualité
| Priorité | Objectif qualité | Scénario |
|----------|------------------|----------|
| 1 | **Performance** | Doit avoir une latence ≤ 500 ms et supporter plus de 300 ordres/s |
| 2 | **Disponibilité** | système doit être opérationnel pour au moins 90% du temps |
| 3 | **Observabilité** | Présence de logs pour suivre les actions effectuées |

### Parties prenantes (Stakeholders)
- **Développeur.euse** : Concoivent et déploiement l'applcation au complet
- **Employé.es de l'entreprise** : Utilisateur.trices qui controllent les transactions effectuées et gèrent les utilisateurs dans l'application 
- **investisseurs particuliers** : Client.es servis par l'application (ils peuvent se servir de l'application pour gérer leurs investissements)

## 2. Contraintes d'architecture

| Contrainte | Description |
|------------|-------------|
| **Technologie** | Utilisation de Java, C#, Go, Rust C++ et Docker|
| **Déploiement** | Déploiement à l'aide de Docker, runner github |
| **Éducatif** | L'application doit démontrer clairement l'architecture monolythique et l'application du modèle MVC |

## 3. Portée et contexte du système

### Contexte métier

## 4. Stratégie de solution

| Problème | Approche de solution |
|----------|---------------------|
| **Sécurité** | Mise en place du MFA(Multi factor Authentification) |
| **Persistance des données** | Utilisation de PostgreSQL et DAO |
| **Gestion de la qualité** | Implémentations de tests s'assurer de la robustesse |
| **Déploement automatisé** | Implémentations de Pipeline CI/CD avec runner Github |

## 5. Vue des blocs de construction


## 6. Vue d'exécution


## 7. Vue de déploiement


## 8. Concepts transversaux
- Patrons monolithique, MVC, DAO
- Persistance, base de données relationelle, PostgreSQL

## 9. Décisions d'architecture


## 10. Exigences qualité

### Maintenabilité
- Séparation claire des responsabilités via MVC+DAO
- Conventions de nommage cohérentes à travers toutes les couches

### Flexibilité
- Facile d'échanger entre implémentations MySQL et MongoDB
- Extensible pour des types d'entités additionnels (démontré avec Users et Products)

### Évolutivité
- L'application peut avoir plusieurs clients connectés à un serveur
- L'application peut également avoir plusieurs serveurs, même s'ils ne partagent pas les mêmes données

## 11. Risques et dettes techniques
Non applicable pour cette application.

## 12. Glossaire

| Terme | Définition |
|-------|------------|
| **BD** | Base de données |
| **CLI** | Command-line interface : application d'interface de ligne de commande |
| **DAO** | Data Access Object : abstrait les opérations de base de données |
| **MVC** | Model-View-Controller : patron architectural |
| **NoSQL** | Not only SQL : désigne une famille de systèmes de gestion de base de données qui s'écarte du paradigme classique des bases relationnelles |