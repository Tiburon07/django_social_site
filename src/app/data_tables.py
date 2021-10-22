from ajax_datatable.views import AjaxDatatableView
from app.models import (
    Persona,
    Societa,
    DocumentoBacheca,
    Scadenziario)
from django.contrib.auth.models import Group

import datetime

class PersonaTable(AjaxDatatableView):
    model = Persona
    title = 'Lista Persone'
    column_defs = [
        {'name': 'pk', 'visible': False, 'orderable': True, 'choices': True, 'searchable': False, },
        {'name': 'codice_fiscale', 'visible': True, 'orderable': True, 'searchable': False, },
        {'name': 'cognome', 'visible': True, 'orderable': True, 'searchable': False, },
        {'name': 'nome', 'visible': True, 'orderable': True, 'searchable': False, },
        {'name': 'data_nascita', 'visible': True, 'orderable': True, 'title': 'Data di Nascita', 'searchable': False, },
        {'name': 'luogo_nascita', 'visible': True, 'orderable': True, 'title': 'Luogo di Nascita', 'searchable': False, },
    ]

    def customize_row(self, row, obj):
        row['data_nascita'] = datetime.datetime.strptime(row['data_nascita'], '%m/%d/%Y').strftime('%d/%m/%Y')

    def render_row_details(self, pk, request=None):
        obj = self.model.objects.get(pk=pk)

        return '\
            <div>\
                <p><b>' + obj.cognome + ' '  + obj.nome + '</b></p>\
                <p>' + obj.codice_fiscale + '</p>\
            </div>\
        '

    def get_initial_queryset(self, request=None):
        queryset = self.model.objects.all()

        if 'nome' in request.POST:
            nome = request.POST.get('nome')

            if nome != '':
                queryset = queryset.filter(nome=nome)

        if 'cognome' in request.POST:
            cognome = request.POST.get('cognome')

            if cognome != '':
                queryset = queryset.filter(cognome=cognome)

        if 'cf' in request.POST:
            cf = request.POST.get('cf')

            if cf != '':
                queryset = queryset.filter(codice_fiscale=cf)                

        return queryset

class SocietaTable(AjaxDatatableView):
    model = Societa
    title = 'Lista Societa'
    column_defs = [
        {'name': 'pk', 'visible': False, 'orderable': True, },
        {'name': 'codice_fiscale', 'visible': True, 'orderable': True, },
        {'name': 'denominazione', 'visible': True, 'orderable': True, },
        {'name': 'indirizzo', 'visible': True, 'orderable': True, },
    ]

    def render_row_details(self, pk, request=None):
        obj = self.model.objects.get(pk=pk)

        return '\
            <div>\
                <p><b>' + obj.denominazione + '</b></p>\
                <p>' + obj.codice_fiscale + '</p>\
                <p>' + obj.indirizzo + '</p>\
            </div>\
        '

icone = {'PDF': 'PDF.png', 'PPT': 'PPT.png'}

class DocumentoBachecaTable(AjaxDatatableView):
    model = DocumentoBacheca
    title = 'Bacheca'
    column_defs = [
        {'name': 'pk', 'visible': False, 'orderable': True, },
        {'name': 'tipo', 'visible': True, 'orderable': True, },
        {'name': 'nome', 'visible': True, 'orderable': True, },
        {'name': 'data', 'visible': True, 'orderable': True, },
    ]

    def customize_row(self, row, obj):
        row['tipo'] = '<a href="/download/' + obj.filename + '"><img class="dataTables_icons" src="/static/images/' + icone[obj.tipo] + '"/></a>' + obj.tipo
        row['data'] = datetime.datetime.strptime(row['data'], '%m/%d/%Y').strftime('%d/%m/%Y')

    def get_initial_queryset(self, request=None):
        queryset = self.model.objects.filter(permessi=0)

        for group in Group.objects.all():
            if request.user.groups.filter(pk=group.pk).exists():
                queryset |= self.model.objects.filter(permessi=group.pk)

        return queryset

    def render_row_details(self, pk, request=None):
        obj = self.model.objects.get(pk=pk)

        return '\
            <div>\
                <p><b>' + obj.nome + '</b></p>\
                <p>' + obj.descrizione + '</p>\
                <a href="/download/' + obj.filename + '">\
                    <img class="dataTables_icons" src="/static/images/' + icone[obj.tipo] + '"/>Scarica\
                </a>\
            </div>\
        '

class ScadenzarioTable(AjaxDatatableView):
    model = Scadenziario
    title = 'Scadenziario'
    column_defs = [
        {'name': 'pk', 'visible': False, 'orderable': True, },
        {'name': 'protocollo', 'visible': True, 'orderable': True, },
        {'name': 'titolo', 'visible': True, 'orderable': True, },
        {'name': 'data_inizio', 'visible': True, 'orderable': True, 'title': 'Data di Inizio', },
        {'name': 'data_fine', 'visible': True, 'orderable': True, 'title': 'Data di Fine', },
        {'name': 'ultimo_aggiornamento', 'visible': True, 'orderable': True, 'title': 'Ultimo Aggiornamento', },
    ]

    def customize_row(self, row, obj):
        row['data_inizio'] = datetime.datetime.strptime(row['data_inizio'], '%m/%d/%Y').strftime('%d/%m/%Y')
        row['data_fine'] = datetime.datetime.strptime(row['data_fine'], '%m/%d/%Y').strftime('%d/%m/%Y')
        row['ultimo_aggiornamento'] = datetime.datetime.strptime(row['ultimo_aggiornamento'], '%m/%d/%Y %H:%M:%S').strftime('%d/%m/%Y  %H:%M:%S')

    def render_row_details(self, pk, request=None):
        obj = self.model.objects.get(pk=pk)

        return '\
            <div>\
                <p><b>' + obj.protocollo + '</b> ' + obj.data_inizio.strftime('%d/%m/%Y') + ' - ' + obj.data_fine.strftime('%d/%m/%Y') + '</p>\
                <p>' + obj.titolo + '</p>\
            </div>\
        '