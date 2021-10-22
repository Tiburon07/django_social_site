from django.db import models
from django.contrib.auth.models import Group, User

class Persona(models.Model):
    codice_fiscale = models.CharField(max_length=16)
    cognome = models.CharField(max_length=200)
    nome = models.CharField(max_length=200)
    data_nascita = models.DateField()
    luogo_nascita = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Persone"

class Societa(models.Model):
    codice_fiscale = models.CharField(max_length=11)
    denominazione = models.CharField(max_length=200)
    indirizzo = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Società"
        verbose_name_plural = "Società"

class DocumentoBacheca(models.Model):
    tipo = models.CharField(max_length=200)
    nome = models.CharField(max_length=200)
    descrizione = models.TextField()
    data = models.DateField()
    filename = models.CharField(max_length=200)
    permessi = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Documento Bacheca"
        verbose_name_plural = "Documenti Bacheca"

class PermessiPagine(models.Model):
    url = models.CharField(max_length=200)
    permessi = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Permessi Pagina"
        verbose_name_plural = "Permessi Pagina"

class Scadenziario(models.Model):
    protocollo = models.CharField(max_length=200)
    titolo = models.CharField(max_length=200)
    data_inizio = models.DateField(auto_now_add=True)
    data_fine = models.DateField()
    ultimo_aggiornamento = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Scadenzario"
        verbose_name_plural = "Scadenzario"

class GroupLabel(models.Model):
    group = models.OneToOneField(Group, on_delete=models.DO_NOTHING)
    label = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Group Label"
        verbose_name_plural = "Group Labels"

class Federazione(models.Model):
    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Federazione"
        verbose_name_plural = "Federazioni"

class StatoFascicolo(models.Model):
    stato = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Stato Fascicolo"
        verbose_name_plural = "Stati Fascicolo"

class Fascicolo(models.Model):
    protocollo = models.CharField(max_length=200)
    anno = models.CharField(max_length=4)
    progressivo = models.IntegerField(default=0)
    titolo = models.TextField()
    fsn = models.ForeignKey(Federazione, on_delete=models.DO_NOTHING)
    stato = models.ForeignKey(StatoFascicolo, on_delete=models.DO_NOTHING)
    data_scadenza = models.DateField()
    data_utilma_modifica = models.DateTimeField()
    letto = models.BooleanField()
    letto_fsn = models.BooleanField()
    obbligo_visione = models.BooleanField()
    utente = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    prioritario = models.BooleanField()
    # id_tipo_documento
    # id_stato_padre
    # avocazione

    class Meta:
        verbose_name = "Fascicolo"
        verbose_name_plural = "Fascicoli"

class TipoDocumento(models.Model):
    descrizione = models.CharField(max_length=200)
    giorni = models.IntegerField(default=0)
    codice = models.IntegerField(default=0)
    livello = models.IntegerField(default=0)
    # is_attesa
    # flag_verifica

    class Meta:
        verbose_name = "Tipo Documento"
        verbose_name_plural = "Tipi Documento"

class Documento(models.Model):
    fascicolo = models.ForeignKey(Fascicolo, on_delete=models.DO_NOTHING)
    descrizione = models.TextField(),
    data_creazione = models.DateTimeField(),
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.DO_NOTHING)
    data_scadenza = models.DateField(),
    obbligo_visione = models.BooleanField(),
    letto = models.BooleanField()
    # data_documento
    # segnalanti
    # segnalati

    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documenti"

'''
    Modello che mette in relazione l'utenza con l'FSN necessaria per profilazione fascicolo.
'''
class RelUtenteFSN(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    federazione = models.ForeignKey(Federazione, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Relazione Utente/Federazione"
        verbose_name_plural = "Relazioni Utente/Federazione"