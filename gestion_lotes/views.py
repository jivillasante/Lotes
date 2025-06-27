from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import LoteForm
from .models import Lote
import pandas as pd

@login_required
def home(request):
    return render(request, 'home/home.html')  # Esta plantilla debe estar en templates/home/home.html

@login_required
def subir_lote(request):
    if request.method == 'POST':
        form = LoteForm(request.POST, request.FILES)
        if form.is_valid():
            lote = form.save(commit=False)
            lote.usuario = request.user
            lote.save()
            return redirect('resultado_lote', lote_id=lote.id)
    else:
        form = LoteForm()
    return render(request, 'gestion_lotes/subir_lote.html', {'form': form})

@login_required
def resultado_lote(request, lote_id):
    lote = Lote.objects.get(id=lote_id, usuario=request.user)
    df = pd.read_excel(lote.archivo.path)
    df['Categoria'] = df.apply(lambda row: 'Exportación' if row['Firmeza'] >= 130 else 'Nacional', axis=1)
    return render(request, 'gestion_lotes/resultado_lote.html', {'df': df.to_html(classes='table')})