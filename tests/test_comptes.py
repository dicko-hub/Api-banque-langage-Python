from Comptes import *

def test_creerCompte():
	c=Comptes(0,"dicko",0,"dickBank")
	assert c.proprietaire=="dicko"

def test_ajouterArgent():
	c=Comptes(0,"dicko",0,"dickBank")
	c.ajouterArgent(125)
	assert c.montant!=0

def test_retirerArgent():
	c=Comptes(0,"dicko",200,"dickBank")
	c.retirerArgent(125)
	assert c.montant==75

def  test_ajouterCompte():
	c1=Comptes(0,"dicko",200,"dickBank")
	c2=Comptes(1,"voison",100,"dickBank")
	c1+c2
	assert c1.montant==300 

def test_ajouterCompte2():
	c1=Comptes(0,"dicko",200,"dickBank")
	c2=Comptes(1,"voison",100,"dickBank")
	c1+=c2
	assert c1.montant==300

def test_soustraireCompte():
	c1=Comptes(0,"dicko",200,"dickBank")
	c2=Comptes(1,"voison",100,"dickBank")
	c1-=c2
	assert c1.montant==100
	
def test_creerBanque():
	c1=Comptes(0,"dicko",200,"dickBank")
	b=Banque("dickBank",c1)
	assert b.nom=="dickBank"
	assert b.listes[0]=="dicko"

def test_creerCompteDepuisBanque():
	c2=Comptes(0,"dicko",200,"dickBank")
	b=Banque("dickBank",c2)
	c=b.creerCompte(1,"voison",150)
	assert c.montant==150
	

