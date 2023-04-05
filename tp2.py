from flask import Flask 
from flask import render_template
from flask import request
# from datetime import datetime
monapp = Flask(__name__)

@monapp.route('/')
def fonction_page_accueil():
    return render_template('index.html')


@monapp.route('/getInfos')
def getInfos():
    nom = request.args.get('nom')
    prenom = request.args.get('prenom')
    numero = request.args.get('numero')
    noteMath = request.args.get('noteMath')
    noteScience = request.args.get('noteScience')
    noteFrancais = request.args.get('noteFrancais')
    noteAnglais = request.args.get('noteAnglais')
    noteHistoire = request.args.get('noteHistoire')


    file = open("G:/6iem_session/phyton/python_OlivierQuintal/TP2_OlivierQuintal/resultats.txt", "a")
    file.write(nom + "," + prenom + "," + numero + "," + noteMath + "," + noteScience + "," + noteFrancais + "," + noteAnglais + "," + noteHistoire + "\n")
    file.close()
    return render_template('index.html')



@monapp.route('/listeEtudiants')
def listeEtudiants():
     
    file = open("resultats.txt")
    ligneDuFichier = file.readlines()
    file.close()
    nom1 = ligneDuFichier[0].split(",")[0]
    print(nom1)
    prenom1 = ligneDuFichier[0].split(",")[1]

    nom2 = ligneDuFichier[1].split(",")[0]
    prenom2 = ligneDuFichier[1].split(",")[1]

    nom3 = ligneDuFichier[2].split(",")[0]
    prenom3 = ligneDuFichier[2].split(",")[1]

    nom4 = ligneDuFichier[3].split(",")[0]
    prenom4 = ligneDuFichier[3].split(",")[1]

    return render_template('listeEtudiants.html', nom1 = nom1, prenom1 = prenom1, nom2 = nom2, prenom2 = prenom2, nom3 = nom3, prenom3 = prenom3, nom4 = nom4, prenom4 = prenom4)


@monapp.route('/choixEtudiant')
def etudiantinfo():
    etudiant = request.args.get('etudiant')
    # print(etudiant)

    file = open("resultats.txt")
    lignes = file.readlines()
    file.close()

    nom = lignes[int(etudiant)-1].split(',')[0]
    prenom = lignes[int(etudiant)-1].split(',')[1]
    numero = lignes[int(etudiant)-1].split(',')[2]
    noteMath = lignes[int(etudiant)-1].split(',')[3]
    noteScience = lignes[int(etudiant)-1].split(',')[4]
    noteHistoire = lignes[int(etudiant)-1].split(',')[5]
    noteAnglais = lignes[int(etudiant)-1].split(',')[6]
    noteFrancais = lignes[int(etudiant)-1].split(',')[7]

    nomFichierBulletin = nom + "_" + prenom +".txt"
    file = open(nomFichierBulletin, "w")
    file.write("Bulletin de " + nom + " " + prenom + "\n")
    file.write("Math : " + noteMath + "\n")
    file.write("Science : " + noteScience + "\n")
    file.write("Histoire : " + noteHistoire + "\n")
    file.write("Anglais : " + noteAnglais + "\n")
    file.write("Francais : " + noteFrancais + "\n")
    file.close()

    return render_template('afficheInfoSurEtudiant.html', nom = nom, prenom = prenom, numero = numero, noteMath = noteMath, noteScience = noteScience, noteHistoire = noteHistoire, noteAnglais = noteAnglais, noteFrancais = noteFrancais, etudiant = etudiant)


@monapp.route('/telechargerBulletin')
def telechargerBulletin():
    return render_template('telechargement.html')



if __name__ == "__main__":
	monapp.run(debug=True)