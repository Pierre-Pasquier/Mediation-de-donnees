from whoosh import index as index_dir
import sys
from whoosh.qparser import QueryParser

sys.path.append('../src')

from flask import Flask, render_template, request, redirect, url_for
from hpo import get_diseases_by_symptoms
from hpo import get_disease_by_id
from OmimIndex import SearchNO
from meddra import getMaladiebyCUI
from omim_onto import NOtoCUI
from drugbank import ToxicitytoNomMedicament
from final import MaladieToMedicament
from final import MedicamentToMedicament
import re

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        symptoms = request.form.getlist('symptoms[]')
        ix = index_dir.open_dir("OMIMIndex")
        searcher = ix.searcher()
        parser = QueryParser("CS", ix.schema)
        diseases = getMaladiebyCUI(NOtoCUI(SearchNO(symptoms, searcher, parser))) + get_disease_by_id(get_diseases_by_symptoms(symptoms))
        drugs = ToxicitytoNomMedicament(symptoms)
        diseases=[(maladie,info, MaladieToMedicament(maladie)) for maladie ,info in diseases]
        drugs = [(medoc, info, MedicamentToMedicament(medoc, searcher, parser)) for medoc, info in drugs]
        return render_template('results.html', diseases=diseases, drugs=drugs)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

