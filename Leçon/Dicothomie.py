def resoudreEquationFonctionCroissanteDichotomie(f , k , a , b , e):
    
    debut = a
    
    fin = b
    
    # Calcul de la longueur de [a , b]
    
    ecart = b - a
    
    while ecart > e :
    
        # Calcul du milieu
    
        m = ( debut + fin ) / 2
    
        if f ( m ) > k :
    
            # La solution est inférieure à m
    
            fin = m
    
        else:
    
            # La solution est supérieure à m
    
            debut = m
    
        ecart = fin - debut
    
    return m

def resoudreEquationParBalayage(f,k,a,e):
    s = a
    while f(s)<= k:
        s=s+e
    return s