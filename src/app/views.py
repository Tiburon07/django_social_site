from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse, JsonResponse
from .models import DocumentoBacheca, PermessiPagine, GroupLabel
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import connection
from django.contrib.auth.models import User
from django.core.mail import send_mail

import json
import logging
import os

def favicon(request):
    return FileResponse(open('static/favicon.ico', 'rb'))

@login_required
def routes(request):
    args = { 'login_url': 'https://www.google.com' }

    if request.path == '/':
        return redirect('/bacheca')

    url = request.path.strip('/')
    pagina = PermessiPagine.objects.filter(url=url)

    if not pagina:
        return render(request, 'app/{0}.html'.format(url), args)

    for item in pagina:
        if request.user.groups.filter(pk=item.permessi).exists():
            return render(request, 'app/{0}.html'.format(url))

    return redirect('/')

@login_required
def download(request):
    filename = os.path.basename(request.path)
    queryset = DocumentoBacheca.objects.filter(filename=filename)

    for item in queryset:
        if request.user.groups.filter(pk=item.permessi).exists() or item.permessi==0:
            return FileResponse(open('/app/documents/{0}'.format(filename), 'rb'))

    return HttpResponse('Unauthorized', status=401)

@login_required
def nuova_utenza(request):
        permesso = request.user.groups.filter(name='PROCURA_GENERALE').exists()

        if request.method == 'GET':
            if not permesso:
                return redirect('/bacheca')

            return render(request, 'app/nuova_utenza.html')
        if request.method == 'POST':
            if not permesso:
                return JsonResponse({ 'successo': False, 'messaggio': 'Non si dispone dei permessi necessari.' })

            ruolo = request.POST.get('ruolo')
            username = request.POST.get('username')
            password = request.POST.get('password')
            password_confirm = request.POST.get('password_confirm')
            email = request.POST.get('email')
            nome = request.POST.get('nome')
            cognome = request.POST.get('cognome')

            if (password != password_confirm):
                return JsonResponse({ 'successo': False, 'messaggio': 'La password non corrisponde.' })

            u, created = User.objects.get_or_create(username=username)

            if not created:
                return JsonResponse({ 'successo': False, 'messaggio': 'Utente già registrato' })

            send_mail(
                'Prova registrazione Giustizia Sportiva',
                'LOL funziona.',
                'noreply@giustizia-sportiva.it',
                [email],
                fail_silently=False,
            )

            return JsonResponse({ 'successo': True })

'''@login_required
def anagrafica_data(request):
    with connection.cursor() as cursor:
        cursor.execute("select * from app_persona")
        columns = [col[0] for col in cursor.description]
        return JsonResponse([
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ], safe=False)'''
