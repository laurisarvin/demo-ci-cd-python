"""
Calculatrice simple — module de démonstration pour le cours CI/CD.

Ce module fournit une classe Calculator avec les opérations de base.
Le code est volontairement simple pour qu'on se concentre sur le pipeline CI/CD.
"""


class Calculator:
    """Une calculatrice simple avec un historique des opérations."""

    def __init__(self):
        """Initialise la calculatrice avec un historique vide."""
        self.historique = []

    def additionner(self, a: float, b: float) -> float:
        """Retourne a + b et enregistre l'opération."""
        resultat = a + b
        self.historique.append(f"{a} + {b} = {resultat}")
        return resultat

    def soustraire(self, a: float, b: float) -> float:
        """Retourne a - b et enregistre l'opération."""
        resultat = a - b
        self.historique.append(f"{a} - {b} = {resultat}")
        return resultat

    def multiplier(self, a: float, b: float) -> float:
        """Retourne a * b et enregistre l'opération."""
        resultat = a * b
        self.historique.append(f"{a} * {b} = {resultat}")
        return resultat

    def diviser(self, a: float, b: float) -> float:
        """
        Retourne a / b et enregistre l'opération.

        Lève ZeroDivisionError si b vaut 0.
        """
        if b == 0:
            raise ZeroDivisionError("Division par zéro impossible")
        resultat = a / b
        self.historique.append(f"{a} / {b} = {resultat}")
        return resultat

    def puissance(self, base: float, exposant: float) -> float:
        """Retourne base ** exposant et enregistre l'opération."""
        resultat = base**exposant
        self.historique.append(f"{base} ^ {exposant} = {resultat}")
        return resultat

    def reinitialiser_historique(self) -> None:
        """Vide l'historique des opérations."""
        self.historique = []
