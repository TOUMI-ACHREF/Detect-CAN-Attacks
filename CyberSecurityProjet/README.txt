---Projet CYBERSÉCURITÉ

--TO TEST lunch this DeploimentSecurité.ipynb


-Objectif :
     L'objectif principal de ce projet est de déployer un modèle de machine learning dans le domaine 
    de la cybersécurité.

-Description :
     De nos jours, les voitures autonomes sont de plus en plus répandues et utilisées. Cependant, elles
    restent vulnérables aux cyberattaques, ce qui peut affecter le véhicule et causer des désastres.

-Protocole CAN :
     Le CAN (Controller Area Network) est un protocole de communication utilisé dans les véhicules 
    pour permettre l'échange de données entre les différents composants sans nécessiter un contrôleur central. 

     Fonctionnant sur un système de bus, il assure des échanges rapides et fiables de données, mais il est aussi
    sensible aux attaques, ce qui rend sa sécurisation cruciale dans les voitures autonomes.

-Attaque sur le protocole CAN:
    1. DoS (Denial of Service) Attack :
         Cette attaque vise à saturer le réseau CAN en envoyant un grand nombre de messages inutiles ou avec
        des identifiants bas. Cela empêche les autres messages importants de circuler, bloquant les communications
        entre les composants du véhicule.

    2. Fuzzy Attack :
         Dans une attaque de type Fuzzy, l'attaquant envoie des messages aléatoires avec des identifiants et 
        des données erronés ou aléatoires. Cela peut perturber les composants du véhicule en les poussant à réagir
        de manière imprévue, ce qui peut altérer le comportement du véhicule.

    3. Impersonation Attack :
         Cette attaque consiste à usurper l'identité d'un composant légitime en imitant son identifiant dans 
        le réseau CAN. L'attaquant envoie des messages frauduleux qui semblent provenir d'un composant autorisé,
        ce qui peut induire le système en erreur et compromettre la sécurité du véhicule.

-Modèle de ML :
     Le modèle entraîné est adapté pour détecter ces trois types d'attaques possibles sur le protocole CAN
    des voitures autonomes et peut les identifier en temps réel.

     Algorithme déployé: Decision Tree Classifier

-Description detaillée de l'Ensemble de données  
     https://ocslab.hksecurity.net/Dataset/CAN-intrusion-dataset