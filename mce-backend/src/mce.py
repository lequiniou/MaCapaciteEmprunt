import math

def get_mce(
    revenus_mensuels: float, 
    charges_mensuelles: float, 
    duree_annees: int = 20, 
    taux_endettement: float = 0.35, 
    taux_annuel: float = 0.01
):
    """Fonction qui permet de calculer la capacité d'emprunt ainsi que la mensualité maximale en fonction des revenus mensuels (nets avant impôts), des carges mensuelles fixes du taux d'endettement, du taux d'intérêts annuel et de la durée du remboursement

    Args:
        revenus_mensuels (float): revenus mensuels nets avant imposition
        charges_mensuelles (float): charges mensuelles fixes (mensualités d'un autre prêt, loyers, assurances, impôts, etc..)
        duree_annees (int, optional): durée du remboursement en années (15, 20, 25, etc..) Defaults to 20.
        taux_endettement (float, optional): taux d'endettement appliqué (généralement 33 ou 35%): il s'agit de la proportion du reste à vivre pouvant être allouée au remboursement d'un prêt. Defaults to 0.35.
        taux_annuel (float, optional): taux d'intérêts annuel du prêt. Defaults to 0.01.

    Returns:
        float: mensualité maximale
        float: capacité d'emprunt maximale estimée
    """
    # Compute maximum monthly payment
    mensualite_max = (revenus_mensuels - charges_mensuelles) * taux_endettement
    # Monthly interest rate
    taux_mensuel = taux_annuel / 12
    # total nmber of monthly payments
    nombre_mensualites = duree_annees * 12
    # borrowing power
    if taux_mensuel > 0:
        capacite = mensualite_max * (1 - math.pow(1 + taux_mensuel, -nombre_mensualites)) / taux_mensuel
    else:
        # special case: interest rate is zero
        capacite = mensualite_max * nombre_mensualites
    return round(mensualite_max, 2), round(capacite, 2)