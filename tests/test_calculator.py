"""Tests unitaires pour la calculatrice."""

import pytest
from src.calculator import Calculator


@pytest.fixture
def calc():
    """Fixture qui fournit une calculatrice neuve à chaque test."""
    return Calculator()


# ─── Tests des opérations de base ────────────────────────────────────


class TestOperationsBase:
    """Regroupe les tests des opérations arithmétiques de base."""

    def test_addition_nombres_positifs(self, calc):
        assert calc.additionner(2, 3) == 5

    def test_addition_nombres_negatifs(self, calc):
        assert calc.additionner(-5, -3) == -8

    def test_addition_avec_zero(self, calc):
        assert calc.additionner(7, 0) == 7

    def test_soustraction(self, calc):
        assert calc.soustraire(10, 4) == 6

    def test_soustraction_resultat_negatif(self, calc):
        assert calc.soustraire(3, 8) == -5

    def test_multiplication(self, calc):
        assert calc.multiplier(6, 7) == 42

    def test_multiplication_par_zero(self, calc):
        assert calc.multiplier(123, 0) == 0

    def test_division(self, calc):
        assert calc.diviser(20, 4) == 5

    def test_division_par_zero_leve_exception(self, calc):
        with pytest.raises(ZeroDivisionError):
            calc.diviser(10, 0)

    def test_puissance(self, calc):
        assert calc.puissance(2, 10) == 1024

    def test_puissance_zero(self, calc):
        assert calc.puissance(5, 0) == 1


# ─── Tests de l'historique ───────────────────────────────────────────


class TestHistorique:
    """Tests pour la gestion de l'historique."""

    def test_historique_vide_au_depart(self, calc):
        assert calc.historique == []

    def test_historique_enregistre_addition(self, calc):
        calc.additionner(2, 3)
        assert "2 + 3 = 5" in calc.historique

    def test_historique_plusieurs_operations(self, calc):
        calc.additionner(1, 1)
        calc.multiplier(2, 3)
        calc.diviser(10, 2)
        assert len(calc.historique) == 3

    def test_reinitialiser_historique(self, calc):
        calc.additionner(1, 1)
        calc.additionner(2, 2)
        calc.reinitialiser_historique()
        assert calc.historique == []


# ─── Tests paramétrés (élégants !) ───────────────────────────────────


class TestParametres:
    """Démonstration de tests paramétrés avec @pytest.mark.parametrize."""

    @pytest.mark.parametrize(
        "a,b,attendu",
        [
            (1, 1, 2),
            (0, 0, 0),
            (-1, 1, 0),
            (100, 200, 300),
            (1.5, 2.5, 4.0),
        ],
    )
    def test_addition_multiple(self, calc, a, b, attendu):
        assert calc.additionner(a, b) == attendu

    @pytest.mark.parametrize(
        "base,exp,attendu",
        [
            (2, 3, 8),
            (3, 2, 9),
            (5, 0, 1),
            (10, 1, 10),
        ],
    )
    def test_puissance_multiple(self, calc, base, exp, attendu):
        assert calc.puissance(base, exp) == attendu
