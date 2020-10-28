class Comptes:

	def __init__(self,numero,proprietaire,montant,banque):
		self.numero=numero
		self.proprietaire=proprietaire
		self.montant=montant
		self.banque=banque

	def ajouterArgent(self,montant):
		if montant >0:
			self.montant+=montant	

	def retirerArgent(self,montant):
		if self.montant>=montant and montant>0:
			self.montant-=montant
	def __add__(self,compte):
		if isinstance(compte,Comptes):
			self.montant+=compte.montant	
	def __iadd__(self,compte):
		if isinstance(compte,Comptes):
			self.montant+=compte.montant
			return self
	
	def __isub__(self,compte):
		if isinstance(compte,Comptes):
			self.montant-=compte.montant
			return self

class Banque:

	listes=dict()

	def __init__(self,nom,compte):
		self.nom=nom
		self.listes[compte.numero]=compte.proprietaire

	def creerCompte(self,numero,proprietaire,montant):
		if montant>0:
			return Comptes(numero,proprietaire,montant,self.nom)
		
		
