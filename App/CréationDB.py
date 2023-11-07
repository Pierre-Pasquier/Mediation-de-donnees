import sqlite3

#Création de la base de données database.db

conn = sqlite3.connect('database.db')
print("Opened database successfully")

#Création de la table user
cursor = conn.cursor()
# Création de la table user avec les champs id, username, password
cursor.execute('''DROP TABLE IF EXISTS userinfo''')
cursor.execute('''DROP TABLE IF EXISTS lecon''')
cursor.execute('''DROP TABLE IF EXISTS vocabulaire''')
cursor.execute('''DROP TABLE IF EXISTS vocabulaire_mot''')
cursor.execute('''CREATE TABLE userinfo (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)''')
cursor.execute('''CREATE TABLE lecon (id_lecon INTEGER PRIMARY KEY AUTOINCREMENT, titre TEXT, description TEXT, lecon TEXT, question TEXT, nb_question INTEGER)''')
cursor.execute('''CREATE TABLE vocabulaire (id INTEGER PRIMARY KEY AUTOINCREMENT, titre TEXT , description TEXT) ''')
cursor.execute('''CREATE TABLE vocabulaire_mot (id INTEGER PRIMARY KEY AUTOINCREMENT, id_vocabulaire INTEGER, mot TEXT, traduction TEXT) ''')
cursor.execute('''CREATE TABLE cours (id INTEGER PRIMARY KEY AUTOINCREMENT, titre TEXT , contenu TEXT) ''')

lecon1 = '''
    <style>
			h1 {
				font-size: 2.5rem;
				font-weight: bold;
				text-align: center;
				margin-top: 2rem;
			}
			h2 {
				font-size: 1.5rem;
				font-weight: bold;
				margin-top: 1.5rem;
			}
			p {
				font-size: 1.2rem;
				line-height: 1.5;
				margin-top: 1rem;
			}
			ul {
				font-size: 1.2rem;
				line-height: 1.5;
				margin-top: 1rem;
				margin-left: 2rem;
			}
			.list {
				list-style: disc;
			}
		</style>
	<div class="container">
	<h1>Le Present Perfect Continuous</h1>
	<p>Le <em>Present Perfect Continuous</em> est un temps qui est utilisé pour décrire une action qui a commencé dans le passé et qui se poursuit jusqu'à maintenant. Ce temps est également appelé <em>Present Perfect Progressive</em>.</p>
	<h2>Formation</h2>
<p>Le Present Perfect Continuous est formé en utilisant le Present Perfect de "to be" (au présent) + le participe présent de "to be" + le verbe principal avec "-ing".</p>
<p>Exemple : I have been studying for two hours. (J'étudie depuis deux heures.)</p>

<h2>Utilisation</h2>
<p>Le Present Perfect Continuous est souvent utilisé pour :</p>
<ul>
	<li class="list">Décrire une action qui a commencé dans le passé et qui se poursuit jusqu'à maintenant.</li>
	<li class="list">Décrire une action qui a été répétée plusieurs fois dans le passé et qui continue jusqu'à maintenant.</li>
	<li class="list">Exprimer une action qui a commencé dans le passé mais qui est toujours en cours dans le présent et qui peut continuer dans le futur.</li>
	<li class="list">Exprimer un changement graduel ou une évolution.</li>
</ul>

<h2>Exemples</h2>
<p>Voici quelques exemples de phrases avec le Present Perfect Continuous :</p>
<ul>
	<li class="list">I have been studying for two hours. (J'étudie depuis deux heures.)</li>
	<li class="list">She has been working in this company for five years. (Elle travaille dans cette entreprise depuis cinq ans.)</li>
	<li class="list">They have been playing tennis every Saturday. (Ils jouent au tennis tous les samedis.)</li>
	<li class="list">The tree has been growing slowly for many years. (L'arbre pousse lentement depuis de nombreuses années.)</li>
</ul>
</div>
'''


lecon2 = '''
     <h1>Les temps verbaux en anglais</h1>
    <p>Les temps verbaux en anglais sont utilisés pour exprimer le moment auquel une action se produit. Il existe plusieurs temps verbaux en anglais, chacun avec une utilisation spécifique.</p>
    <h2>Le présent simple (present simple)</h2>
<p>Le présent simple est utilisé pour décrire une action régulière ou une vérité générale. Il est formé en ajoutant un <i>s</i> à la fin du verbe à la troisième personne du singulier.</p>
<p>Exemples:</p>
<ul>
  <li>I eat breakfast every morning. (Je prends mon petit déjeuner tous les matins.)</li>
  <li>She speaks French fluently. (Elle parle couramment français.)</li>
</ul>

<h2>Le passé simple (past simple)</h2>
<p>Le passé simple est utilisé pour décrire une action qui s'est produite dans le passé et qui est maintenant terminée. Il est formé en ajoutant <i>-ed</i> à la fin du verbe régulier.</p>
<p>Exemples:</p>
<ul>
  <li>I walked to the store yesterday. (J'ai marché jusqu'au magasin hier.)</li>
  <li>We watched a movie last night. (Nous avons regardé un film hier soir.)</li>
</ul>

<h2>Le présent progressif (present continuous)</h2>
<p>Le présent progressif est utilisé pour décrire une action qui se produit actuellement ou qui est en cours de réalisation. Il est formé en utilisant le verbe <i>to be</i> au présent suivi du verbe à l'infinitif avec la terminaison <i>-ing</i>.</p>
<p>Exemples:</p>
<ul>
  <li>I am typing on my computer right now. (Je suis en train de taper sur mon ordinateur en ce moment.)</li>
  <li>They are studying for their exams this week. (Ils étudient pour leurs examens cette semaine.)</li>
</ul>

<h2>Le passé progressif (past continuous)</h2>
<p>Le passé progressif est utilisé pour décrire une action qui se produisait dans le passé et qui était en cours de réalisation. Il est formé en utilisant le verbe <i>to be</i> au passé suivi du verbe à l'infinitif avec la terminaison <i>-ing</i>.</p>
<p>Exemples:</p>
<ul>
  <li>I was studying when my phone rang. (J'étudiais quand mon téléphone a sonné.)</li>
  <li>They were playing basketball when it started to rain. (Ils jouaient au basket-ball quand il a commencé à pleuvoir.)</li>
</ul>

<h2>Le futur simple (future simple)</h2>
<p>Le futur simple est utilisé pour décrire une action qui se produira dans
'''
question1 = '''<dl class="mt-5 grid grid-cols-1 gap-5 sm:grid-cols-1">
        <div class="overflow-hidden rounded-lg bg-white px-4 py-5 shadow sm:p-6">
		<fieldset>
			<legend>Question 1 : Quand utilise-t-on 'the' en anglais ?</legend>
			<label for="q1"></label>
			<input  type="text"
                        class="
                          w-max
                          text-center
                          h-[50px]
                          text-sm
                          font-medium
                          bg-white bg-opacity-20
                          placeholder-white
                          text-black
                          rounded
                          mb-4
                          mx-10
                          outline-yes
                          border border-black
                          focus-visible:shadow-none
                          focus:border-white
                        "
                    name="q1" id="q1" required>
        </fieldset></div></dl>
        <dl class="mt-5 grid grid-cols-1 gap-5 sm:grid-cols-1">
        <div class="overflow-hidden rounded-lg bg-white px-4 py-5 shadow sm:p-6">
	<fieldset>
		<legend>Question 2 : Quel est le rôle de 'the' en anglais ?</legend>
		<label for="q2">Choisissez la réponse qui convient :</label>
		<select type="text"
                        class="
                          w-max
                          text-center
                          h-[50px]
                          text-sm
                          font-medium
                          bg-white bg-opacity-20
                          placeholder-white
                          text-black
                          rounded
                          mb-4
                          mx-10
                          outline-yes
                          border border-black
                          focus-visible:shadow-none
                          focus:border-white
                        "

                name="q2" id="q2" required>
			<option value="">-- Choisissez une réponse --</option>
			<option value="1" name="q2">Article indéfini</option>
			<option value="2" name="q2">Article défini</option>
			<option value="3" name="q2">Pronom personnel</option>
			<option value="4" name="q2">Préposition</option>
		</select>
    </fieldset></div></dl>
    <dl class="mt-5 grid grid-cols-1 gap-5 sm:grid-cols-1">
        <div class="overflow-hidden rounded-lg bg-white px-4 py-5 shadow sm:p-6">
	<fieldset>
		<legend>Question 3 : Peut-on utiliser 'the' avec des noms propres en anglais ?</legend>
		<label for="q3">Répondez par oui ou par non :</label>
		<input type="radio" name="q3" id="q3_oui" value="oui" required> <label for="q3_oui">Oui</label>
		<input type="radio" name="q3" id="q3_non" value="non"> <label for="q3_non">Non</label>
    </fieldset></div></dl>
    <dl class="mt-5 grid grid-cols-1 gap-5 sm:grid-cols-1">
        <div class="overflow-hidden rounded-lg bg-white px-4 py-5 shadow sm:p-6">
	<fieldset>
		<legend>Question 4 : Dans quels cas doit-on utiliser 'the' avec des noms de lieux en anglais ?</legend>
		<label for="q4">Choisissez la réponse qui convient :</label>
		<select  type="text"
                        class="
                          w-max
                          text-center
                          h-[50px]
                          text-sm
                          font-medium
                          bg-white bg-opacity-20
                          placeholder-white
                          text-black
                          rounded
                          mb-4
                          mx-10
                          outline-yes
                          border border-black
                          focus-visible:shadow-none
                          focus:border-white
                        "
                name="q4" id="q4" required>
			<option value="">-- Choisissez une réponse --</option>
			<option value="1" name="q4">Pour les noms de pays</option>
			<option value="2" name="q4">Pour les noms de villes</option>
			<option value="3" name="q4">Pour les noms de régions géographiques (montagnes, rivières, océans...)</option>
			<option value="4" name="q4">Pour tous les noms de lieux en anglais</option>
		</select>
    </fieldset></div></dl>
    <dl class="mt-5 grid grid-cols-1 gap-5 sm:grid-cols-1">
        <div class="overflow-hidden rounded-lg bg-white px-4 py-5 shadow sm:p-6">
	<fieldset>
		<legend>Question 5 : Peut-on utiliser 'the' avec des noms comptables et dénombrables en anglais ?</legend>
		<label for="q5">Répondez par oui ou par non :</label>
		<input type="radio" name="q5" id="q5_oui" value="oui" required> <label for="q5_oui">Oui</label>
		<input type="radio" name="q5" id="q5_non" value="non"> <label for="q5_non">Non</label>
    </fieldset></div></dl>'''

cursor.execute('''INSERT INTO lecon (titre, description, lecon,question,nb_question) VALUES ("Present Perfect Continuous", "Cette leçon présente l'utilisation du present perfect continuous en anglais. Elle est composée de 3 parties :<br>
•	La première partie présente la forme du present perfect continuous et son utilisation.<br>
•	La deuxième partie présente des exemples d'utilisation du present perfect continuous.<br>
•	La troisième partie présente des exercices d'application.", ?,?,5) ''', (lecon1,question1))

cursor.execute('''INSERT INTO lecon (titre, description, lecon) VALUES ("Les temps verbaux", "Ce cours porte sur les temps verbaux en anglais. Il présente les cinq temps verbaux les plus courants en anglais : le présent simple, le passé simple, le présent progressif, le passé progressif et le futur simple, avec des exemples d'utilisation. À la fin du cours, plusieurs types de questions sont posées pour tester la compréhension de l'étudiant.", ?) ''', (lecon2,))


cursor.execute('''INSERT INTO vocabulaire (titre,description) VALUES ("Present Perfect Continuous", "Une liste intéressante")''')
cursor.close()
conn.commit()
conn.close()
