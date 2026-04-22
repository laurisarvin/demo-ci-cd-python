"""
Calculatrice simple — module de démonstration pour le cours CI/CD.

Ce module fournit une classe Calculator avec les opérations de base.
Le code est volontairement simple pour qu'on se concentre sur le pipeline CI/CD.
"""


class CalculatriceErreur(Exception):
    """Exception de base pour toutes les erreurs de la calculatrice."""
    pass


class TypeInvalideErreur(CalculatriceErreur, TypeError):
    """Levée quand un argument n'est pas un nombre (int ou float)."""
    pass


class DivisionParZeroErreur(CalculatriceErreur, ZeroDivisionError):
    """Levée lors d'une tentative de division par zéro."""
    pass


class ExposantInvalideErreur(CalculatriceErreur, ValueError):
    """Levée quand la combinaison base/exposant est mathématiquement invalide."""
    pass


def _valider_nombres(*args: object) -> None:
    """
    Vérifie que tous les arguments sont des int ou float (pas des bool).

    Lève TypeInvalideErreur si un argument est invalide.
    """
    for valeur in args:
        if isinstance(valeur, bool) or not isinstance(valeur, (int, float)):
            raise TypeInvalideErreur(
                f"Type invalide : attendu int ou float, reçu {type(valeur).__name__!r} "
                f"(valeur : {valeur!r})"
            )


class Calculator:
    """Une calculatrice simple avec un historique des opérations."""

    def __init__(self):
        """Initialise la calculatrice avec un historique vide."""
        self.historique = []

    # ------------------------------------------------------------------
    # Méthodes publiques
    # ------------------------------------------------------------------

    def additionner(self, a: float, b: float) -> float:
        """
        Retourne a + b et enregistre l'opération.

        Lève:
            TypeInvalideErreur: si a ou b n'est pas un nombre.
        """
        _valider_nombres(a, b)
        resultat = a + b
        self.historique.append(f"{a} + {b} = {resultat}")
        return resultat

    def soustraire(self, a: float, b: float) -> float:
        """
        Retourne a - b et enregistre l'opération.

        Lève:
            TypeInvalideErreur: si a ou b n'est pas un nombre.
        """
        _valider_nombres(a, b)
        resultat = a - b
        self.historique.append(f"{a} - {b} = {resultat}")
        return resultat

    def multiplier(self, a: float, b: float) -> float:
        """
        Retourne a * b et enregistre l'opération.

        Lève:
            TypeInvalideErreur: si a ou b n'est pas un nombre.
        """
        _valider_nombres(a, b)
        resultat = a * b
        self.historique.append(f"{a} * {b} = {resultat}")
        return resultat

    def diviser(self, a: float, b: float) -> float:
        """
        Retourne a / b et enregistre l'opération.

        Lève:
            TypeInvalideErreur:    si a ou b n'est pas un nombre.
            DivisionParZeroErreur: si b vaut 0.
        """
        _valider_nombres(a, b)
        if b == 0:
            raise DivisionParZeroErreur(
                f"Division par zéro impossible : {a} / {b}"
            )
        resultat = a / b
        self.historique.append(f"{a} / {b} = {resultat}")
        return resultat

    def puissance(self, base: float, exposant: float) -> float:
        """
        Retourne base ** exposant et enregistre l'opération.

        Lève:
            TypeInvalideErreur:    si base ou exposant n'est pas un nombre.
            ExposantInvalideErreur: si l'opération produit un résultat non réel
                                    (ex. racine d'un nombre négatif).
        """
        _valider_nombres(base, exposant)
        try:
            resultat = base ** exposant
        except (ValueError, ZeroDivisionError) as exc:
            raise ExposantInvalideErreur(
                f"Opération invalide : {base} ^ {exposant} — {exc}"
            ) from exc

        # Cas complexe non géré (ex. (-1) ** 0.5 donne nan en float)
        if isinstance(resultat, complex) or (isinstance(resultat, float) and resultat != resultat):
            raise ExposantInvalideErreur(
                f"Résultat non réel pour {base} ^ {exposant}"
            )

        self.historique.append(f"{base} ^ {exposant} = {resultat}")
        return resultat

    def reinitialiser_historique(self) -> None:
        """Vide l'historique des opérations."""
        self.historique = []


# ------------------------------------------------------------------
# Exemple d'utilisation
# ------------------------------------------------------------------
if __name__ == "__main__":
    calc = Calculator()

    exemples = [
        ("additionner",  (10, 5)),
        ("soustraire",   (10, 5)),
        ("multiplier",   (10, 5)),
        ("diviser",      (10, 5)),
        ("diviser",      (10, 0)),          # DivisionParZeroErreur
        ("additionner",  ("dix", 5)),       # TypeInvalideErreur
        ("additionner",  (True, 5)),        # TypeInvalideErreur (bool exclu)
        ("puissance",    (2, 10)),
        ("puissance",    (-1, 0.5)),        # ExposantInvalideErreur
    ]

    for methode, args in exemples:
        try:
            resultat = getattr(calc, methode)(*args)
            print(f"  {methode}{args} → {resultat}")
        except CalculatriceErreur as exc:
            print(f"  {methode}{args} → ⚠ {type(exc).__name__}: {exc}")
