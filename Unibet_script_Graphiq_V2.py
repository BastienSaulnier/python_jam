import os
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import time
import matplotlib.gridspec as gridspec



#PRE-TRAITEMENT 

################Chemin du repertoire à changer#######################################

# Chemin vers votre fichier de données
Chemin_Repertoire = os.getcwd()
nom_fichier_traitment = os.path.join(Chemin_Repertoire, "Unibet_Source.txt")


# Buy-in sur Unibet
positions = [1, 2, 5, 10, 25, 50, 100]
# Initialisation du tableau avec des zéros pour compter les victoires par multi sur les Hexapro en fonction de Buy-in
X2w_H = [0] * (max(positions) + 1)
X3w_H = [0] * (max(positions) + 1)
X5w_H = [0] * (max(positions) + 1)
X10w_H = [0] * (max(positions) + 1)
X10L_H = [0] * (max(positions) + 1)
X25w_H = [0] * (max(positions) + 1)
X100w_H = [0] * (max(positions) + 1)
X1000w_H = [0] * (max(positions) + 1)
Temps_H = [0] * (max(positions) + 1)

# Initialisation du tableau avec des zéros pour compter les victoires par multi sur les Banzai
X2w_B = [0] * (max(positions) + 1)
X3w_B = [0] * (max(positions) + 1)
X5w_B = [0] * (max(positions) + 1)
X10w_B = [0] * (max(positions) + 1)
X10L_B = [0] * (max(positions) + 1)
X25w_B = [0] * (max(positions) + 1)
X100w_B = [0] * (max(positions) + 1)
X1000w_B = [0] * (max(positions) + 1)
Temps_B = [0] * (max(positions) + 1)
#Definition du RB

# Fonction pour vérifier si une chaîne peut être convertie en nombre réel
def est_nombre_reel(chaine):
    try:
        float(chaine)
        return True
    except ValueError:
        return False

# Demander à l'utilisateur d'entrer un nombre réel
while True:
    Tx_RB = input("Entrez le taux de Rakeback : ")
    if est_nombre_reel(Tx_RB):
        Tx_RB = float(Tx_RB)
        print("Parfait le RB est de : ", Tx_RB,"%")
        break
    else:
        print("Veuillez entrer un nombre réel valide.")

# Initialisez le tableau avec l'en-tête des colonnes
jeux = [
    [" TYPE       ", "Nbr Games ", "X2Win ", "X3Win ", "X5Win ", "X10Win ", "X10Lost ", "X25Win ", "X100 ", "X1000 ","ITM ","Net chips/Game ","ROI sans RB "," Gains Nets  ","   Rake  "," RB " + str(Tx_RB)+"% ", "Tps de Jeu "," Games/Hr ", "TxHr avec RB", " RB62% + Gains Nets"]
]

Aff_Stat_game = "TYPE \t\t|TOTAL \t|X2w\t|X3w\t|X5w\t|X10w\t|X10L\t|X25\t|X100\t|X1000\t|% Win     \t|net chips     \t|ROI     \t|Gains   \t|RB 20,0% \t|Temps \t| Tx Hr(RB)\n"



# Fonction pour calculer la différence de temps entre deux dates
def time_diff_in_minutes(date1, date2):
    return int((date2 - date1).total_seconds() / 60)










##########################################          GRAPHIQUE   ###################################

# Chemin vers votre fichier de données
Chemin_Repertoire = os.getcwd()
nom_fichier_traitment = os.path.join(Chemin_Repertoire, "Unibet_Source.txt")

# Lire les données à partir du fichier source Unibet_Source.txt
with open(nom_fichier_traitment, 'r') as file:
    lines = file.readlines()


# Lire les données à partir du fichier source Unibet_Source.txt
with open(nom_fichier_traitment, 'r') as file:
    lines = file.readlines()

# Convertir les lignes en listes de tuples (date, game_type, buy_in, amount)
data = []
i = 0
while i < len(lines):
    if "Sit & Gos" in lines[i]:
        date_string = lines[i].split('Sit & Gos')[0].strip()
        #print("date_string : ", date_string," | ")
        game_type = lines[i + 1].split(' ')[1].strip()
        #print("Type Game : ", game_type," | ")
        buy_in = float(lines[i + 1].split(' ')[0].replace('â‚¬', '').strip())
        #print("BI : ", buy_in," | ")
        amount_str = lines[i + 2].replace('â‚¬', '').replace(',', '.').strip()
        #print("amount_str : ", amount_str," | ")
        try:
            amount = float(amount_str)
            #print("amount : ", amount," | ")
            date = datetime.strptime(date_string, '%d/%m/%Y - %H:%M')
            #print("date : ", date," | ")
            data.append((date, game_type, buy_in, amount))
        except ValueError:
            print(f"Impossible de convertir en float : {amount_str}")
            print(f"Ligne problématique : {lines[i].strip()}")
        i += 4
    else:
        i += 1



# Update counts based on data
for date, game_type, buy_in, amount in data:
    multiplier = amount / buy_in
    if multiplier == 1:
        if game_type == "Banzai":
            X2w_B[int(buy_in)] += 1
        else:
            X2w_H[int(buy_in)] += 1
    elif multiplier == 2:
        if game_type == "Banzai":
            X3w_B[int(buy_in)] += 1
        else:
            X3w_H[int(buy_in)] += 1
    elif multiplier == 4:
        if game_type == "Banzai":
            X5w_B[int(buy_in)] += 1
        else:
            X5w_H[int(buy_in)] += 1
    elif multiplier == 7:
        if game_type == "Banzai":
            X10w_B[int(buy_in)] += 1
        else:
            X10w_H[int(buy_in)] += 1
    elif multiplier == 0:
        if game_type == "Banzai":
            X10L_B[int(buy_in)] += 1
        else:
            X10L_H[int(buy_in)] += 1
    elif multiplier == 19:
        if game_type == "Banzai":
            X25w_B[int(buy_in)] += 1
        else:
            X25w_H[int(buy_in)] += 1
    elif multiplier == 79:
        if game_type == "Banzai":
            X100w_B[int(buy_in)] += 1
        else:
            X100w_H[int(buy_in)] += 1
    elif multiplier == 799:
        if game_type == "Banzai":
            X1000w_B[int(buy_in)] += 1
        else:
            X1000w_H[int(buy_in)] += 1


          

# Trier les données par date
data.sort(key=lambda x: x[0])


# Initialisation des variables pour suivre les sessions
sessions = []
current_session = {'start_time': None, 'end_time': None, 'game_type': None, 'buy_in': None, 'num_games': 0, 'total_winnings': 0}

# Parcourir les données pour déterminer les sessions et calculer les gains
for i in range(len(data)):
    current_date, game_type, buy_in, amount = data[i]
    if current_session['start_time'] is None:
        current_session['start_time'] = current_date
        current_session['end_time'] = current_date
        current_session['game_type'] = game_type
        current_session['buy_in'] = buy_in
        current_session['num_games'] += 1
        current_session['total_winnings'] += amount
    else:
        prev_date, _, _, _ = data[i - 1]
        time_diff = time_diff_in_minutes(prev_date, current_date)
        if time_diff > 15 or game_type != current_session['game_type'] or buy_in != current_session['buy_in']:
            current_session['end_time'] = prev_date
            sessions.append(current_session)
            current_session = {'start_time': current_date, 'end_time': current_date, 'game_type': game_type, 'buy_in': buy_in, 'num_games': 1, 'total_winnings': amount}
        else:
            current_session['end_time'] = current_date
            current_session['num_games'] += 1
            current_session['total_winnings'] += amount

# Gestion de la dernière session
if current_session['start_time'] is not None:
    current_session['end_time'] = data[-1][0]
    sessions.append(current_session)


# Calcul des temps joués pour les HexaproSit et les Banzai
for session in sessions:
    duration = session['end_time'] - session['start_time']
    game_type = 'Banzai' if 'Banzai' in session['game_type'] else 'HexaproSit'
    buy_in = session['buy_in']
    if game_type == 'Banzai':
        Temps_B[int(buy_in)]  += duration.total_seconds() / 3600
    else: 
        Temps_H[int(buy_in)] += duration.total_seconds() / 3600




# Afficher les données recueillies
#if data:
#    for date, game_type, buy_in, amount in data:
#        print(f"Date: {date}, Type de jeu: {game_type}, Buy-In: {buy_in}, Montant: {amount}")
#else:
#    print("Aucune donnée trouvée pour les parties HexaproSit.")

# Dictionnaire pour stocker les données de chaque type de jeu et buy-in
game_data = {}

# Filtrer les données pour chaque type de jeu et buy-in
for date, game_type, buy_in, amount in data:
    if game_type not in game_data:
        game_data[game_type] = {}
    if buy_in not in game_data[game_type]:
        game_data[game_type][buy_in] = []
    game_data[game_type][buy_in].append((date, amount))


# Tracer les courbes pour chaque type de jeu et buy-in

# Affichage du graphique avec les commentaires
plt.figure(figsize=(14, 6))
gs = gridspec.GridSpec(2, 1, height_ratios=[10, 1])  # Spécifier une grille avec 2 lignes et 1 colonne, où la première ligne a une hauteur deux fois plus grande

# Sous-plot pour les courbes des gains cumulés
plt.subplot(2, 1, 1)



for game_type, buy_ins in game_data.items():
    for buy_in, data_points in buy_ins.items():
        # Trier les données par date
        data_points.sort(key=lambda x: x[0])
        
        # Calculer le nombre de parties jouées et les gains cumulés
        num_parties = list(range(1, len(data_points) + 1))
        gains_cumules = [sum(amount for _, amount in data_points[:i]) for i in num_parties]
        
        # Calculer le ROI et RB
        
                    
        total_buy_in = buy_in * len(data_points)
        total_gain = sum(amount for _, amount in data_points)
        roi = (total_gain / total_buy_in) * 100
        Rake_gener = buy_in * len(data_points)* 0.06854

        RB = (Tx_RB /100) * Rake_gener 
        if game_type == "Banzai":
            ITM = (X2w_B[int(buy_in)] + X3w_B[int(buy_in)] + X5w_B[int(buy_in)] + X10w_B[int(buy_in)] + X25w_B[int(buy_in)] + X100w_B[int(buy_in)] + X1000w_B[int(buy_in)]   )*100/len(data_points)
            Chips = ((ITM/100)*900)-300
            Aff_Stat_game = Aff_Stat_game + game_type + " " + str(buy_in) + "\t|" + str(len(data_points)) + "\t|" + str(X2w_B[int(buy_in)]) + "\t|" + str(X3w_B[int(buy_in)]) + "\t| " + str(X5w_B[int(buy_in)]) + "\t| " 
            Aff_Stat_game = Aff_Stat_game + str(X10w_B[int(buy_in)]) + "\t| " + str(X10L_B[int(buy_in)]) + "\t| " + str(X25w_B[int(buy_in)]) + "\t| " + str(X100w_B[int(buy_in)]) + "\t| " + str(X1000w_B[int(buy_in)]) 
            Aff_Stat_game = Aff_Stat_game + "\t|" + str(round(ITM,1)) + "%   \t|" + str(round(Chips,1)) + "    \t|" + str(round(roi,2)) + "%   \t|" + str(total_gain) + "€   \t|" + str(round(RB,2)) + "€   \t|" 
            Aff_Stat_game = Aff_Stat_game +  str(round(Temps_B[int(buy_in)],1)) + " \t|"
            if (Temps_B[int(buy_in)] != 0):
                Aff_Stat_game = Aff_Stat_game + str(round((total_gain + RB)/Temps_B[int(buy_in)],2)) + "€/hr\n"
                jeux.append([game_type + " " + str(buy_in), str(len(data_points)), str(X2w_B[int(buy_in)]), str(X3w_B[int(buy_in)]), str(X5w_B[int(buy_in)]), str(X10w_B[int(buy_in)]), str(X10L_B[int(buy_in)]), str(X25w_B[int(buy_in)]), str(X100w_B[int(buy_in)]), str(X1000w_B[int(buy_in)]),str(round(ITM,1))+"%",str(round(Chips,1)),str(round(roi,2))+"%",str(total_gain)+"€",str(round(Rake_gener,0))+"€",str(round(RB,0))+"€", str(round(Temps_B[int(buy_in)],1)) + "Hrs",str(round(len(data_points)/Temps_B[int(buy_in)],1)) + " G/Hr", str(round((total_gain + RB)/Temps_B[int(buy_in)],2))+ "€/hr\n"])    
            else:
                Aff_Stat_game = Aff_Stat_game +  "--   \n"
                jeux.append([game_type + " " + str(buy_in), str(len(data_points)), str(X2w_B[int(buy_in)]), str(X3w_B[int(buy_in)]), str(X5w_B[int(buy_in)]), str(X10w_B[int(buy_in)]), str(X10L_B[int(buy_in)]), str(X25w_B[int(buy_in)]), str(X100w_B[int(buy_in)]), str(X1000w_B[int(buy_in)]),str(round(ITM,1))+"%",str(round(Chips,1)),str(round(roi,2))+"%",str(total_gain)+"€",str(round(Rake_gener,0))+"€",str(round(RB,0))+"€", str(round(Temps_B[int(buy_in)],1)) + "Hrs"," - ", " - €/hr\n"])    
            
                
                
                
                
                
        else :
            ITM = (X2w_H[int(buy_in)] + X3w_H[int(buy_in)] + X5w_H[int(buy_in)] + X10w_H[int(buy_in)] + X25w_H[int(buy_in)] + X100w_H[int(buy_in)] + X1000w_H[int(buy_in)]   )* 100/len(data_points)
            Chips = ((ITM/100)*900)-300
            Aff_Stat_game =  Aff_Stat_game + game_type + " " + str(buy_in) + "\t|" + str(len(data_points)) + "\t|" + str(X2w_B[int(buy_in)]) + "\t|" + str(X3w_B[int(buy_in)])
            Aff_Stat_game = Aff_Stat_game + "\t| " + str(X5w_H[int(buy_in)]) + "\t| " + str(X10w_H[int(buy_in)]) + "\t| " + str(X10L_H[int(buy_in)]) + "\t| " + str(X25w_H[int(buy_in)])
            Aff_Stat_game = Aff_Stat_game + "\t| " + str(X100w_H[int(buy_in)]) + "\t| " + str(X1000w_H[int(buy_in)]) + "\t|" + str(round(ITM,1)) + "%   \t|" + str(round(Chips,1)) 
            Aff_Stat_game = Aff_Stat_game + "    \t|" + str(round(roi,2)) + "%   \t|" + str(total_gain) + "€   \t|" + str(round(RB,2)) + "€   \t|"
            Aff_Stat_game = Aff_Stat_game +  str(round(Temps_H[int(buy_in)],1)) + " \t|"
            if (Temps_H[int(buy_in)] != 0):
                Aff_Stat_game = Aff_Stat_game + str(round((total_gain + RB)/Temps_H[int(buy_in)],2)) + "€/Hr\n"
                jeux.append([game_type + " " + str(buy_in), str(len(data_points)), str(X2w_H[int(buy_in)]), str(X3w_H[int(buy_in)]), str(X5w_H[int(buy_in)]), str(X10w_H[int(buy_in)]), str(X10L_H[int(buy_in)]), str(X25w_H[int(buy_in)]), str(X100w_H[int(buy_in)]), str(X1000w_H[int(buy_in)]),str(round(ITM,1))+"%",str(round(Chips,1)),str(round(roi,2))+"%",str(total_gain)+"€",str(round(Rake_gener,0))+"€",str(round(RB,0))+"€", str(round(Temps_H[int(buy_in)],1)) + "Hrs",str(round(len(data_points)/Temps_H[int(buy_in)],1))+ " G/Hr", str(round((total_gain + RB)/Temps_H[int(buy_in)],2))+ "€/hr\n"])    
            else:
                Aff_Stat_game = Aff_Stat_game +  "--   \n"  
                jeux.append([game_type + " " + str(buy_in), str(len(data_points)), str(X2w_H[int(buy_in)]), str(X3w_H[int(buy_in)]), str(X5w_H[int(buy_in)]), str(X10w_H[int(buy_in)]), str(X10L_H[int(buy_in)]), str(X25w_H[int(buy_in)]), str(X100w_H[int(buy_in)]), str(X1000w_H[int(buy_in)]),str(round(ITM,1))+"%",str(round(Chips,1)),str(round(roi,2))+"%",str(total_gain)+"€",str(round(Rake_gener,0))+"€",str(round(RB,0))+"€", str(round(Temps_H[int(buy_in)],1)) + "Hrs"," - ", " - €/hr\n"])    

        
        # Tracer la courbe avec des points plus petits
        plt.plot(num_parties, gains_cumules, marker='o', linewidth=2, markersize=0, label=f"{game_type} - {buy_in}€ ")

plt.title("Évolution des gains pour différents types de jeu en fonction du nombre de parties")
plt.xlabel("Nombre de parties")
plt.ylabel("Gains cumulés (€)")
plt.legend()
plt.grid(True)
# Sous-plot pour les commentaires
plt.subplot(2, 1, 2)
plt.axis('off')  # Désactiver les axes pour la zone de texte

# Calculer la largeur maximale de chaque colonne
column_widths = [max(len(str(row[i])) for row in jeux) for i in range(len(jeux[0]))]

# Affichage des commentaires
# Construction de la chaîne de texte avec alignement central pour chaque colonne
text = "\n".join([" ".join(str(row[i]).center(column_widths[i]) for i in range(len(jeux[0]))) for row in jeux])
# Utilisation de l'alignement central pour afficher le texte
plt.text(-0.02, 0.4, text, verticalalignment='center', horizontalalignment='left', family='monospace', fontsize=8)

# Afficher le graphique
plt.tight_layout()  # Ajuster automatiquement les sous-graphiques pour éviter le chevauchement
#print(Aff_Stat_game)



# Autres configurations du graphique (titre, étiquettes, grille, etc.)
#plt.title("Tableau de données")
plt.axis('off')  # Masquer les axes
plt.show()


