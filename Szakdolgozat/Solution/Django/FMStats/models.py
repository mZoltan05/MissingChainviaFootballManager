# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Club(models.Model):
    clubid = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    division = models.TextField(blank=True, null=True)
    based = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'club'


class Player(models.Model):
    playerid = models.CharField(primary_key=True, max_length=-1)
    name = models.CharField(max_length=-1, blank=True, null=True)
    clubid = models.ForeignKey(Club, models.DO_NOTHING, db_column='clubid', blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    born = models.CharField(max_length=-1, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    bestpos = models.TextField(blank=True, null=True)
    club = models.TextField(blank=True, null=True)
    nation = models.TextField(blank=True, null=True)
    preferredfoot = models.TextField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    wage = models.IntegerField(blank=True, null=True)
    scoreid = models.ForeignKey('Score', models.DO_NOTHING, db_column='scoreid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player'


class Score(models.Model):
    playerid = models.CharField(unique=True, max_length=-1, blank=True, null=True)
    aerialability = models.CharField(max_length=-1, blank=True, null=True)
    commandofarea = models.CharField(max_length=-1, blank=True, null=True)
    communication = models.CharField(max_length=-1, blank=True, null=True)
    eccentricity = models.CharField(max_length=-1, blank=True, null=True)
    handling = models.CharField(max_length=-1, blank=True, null=True)
    kicking = models.CharField(max_length=-1, blank=True, null=True)
    oneonones = models.CharField(max_length=-1, blank=True, null=True)
    reflexes = models.CharField(max_length=-1, blank=True, null=True)
    rushingout = models.CharField(max_length=-1, blank=True, null=True)
    tendencytopunch = models.CharField(max_length=-1, blank=True, null=True)
    throwing = models.CharField(max_length=-1, blank=True, null=True)
    corners = models.CharField(max_length=-1, blank=True, null=True)
    crossing = models.CharField(max_length=-1, blank=True, null=True)
    dribbling = models.CharField(max_length=-1, blank=True, null=True)
    finishing = models.CharField(max_length=-1, blank=True, null=True)
    firsttouch = models.CharField(max_length=-1, blank=True, null=True)
    freekicks = models.CharField(max_length=-1, blank=True, null=True)
    heading = models.CharField(max_length=-1, blank=True, null=True)
    longshots = models.CharField(max_length=-1, blank=True, null=True)
    longthrows = models.CharField(max_length=-1, blank=True, null=True)
    marking = models.CharField(max_length=-1, blank=True, null=True)
    passing = models.CharField(max_length=-1, blank=True, null=True)
    penaltytaking = models.CharField(max_length=-1, blank=True, null=True)
    tackling = models.CharField(max_length=-1, blank=True, null=True)
    technique = models.CharField(max_length=-1, blank=True, null=True)
    aggression = models.CharField(max_length=-1, blank=True, null=True)
    anticipation = models.CharField(max_length=-1, blank=True, null=True)
    bravery = models.CharField(max_length=-1, blank=True, null=True)
    composure = models.CharField(max_length=-1, blank=True, null=True)
    concentration = models.CharField(max_length=-1, blank=True, null=True)
    vision = models.CharField(max_length=-1, blank=True, null=True)
    decisions = models.CharField(max_length=-1, blank=True, null=True)
    determination = models.CharField(max_length=-1, blank=True, null=True)
    flair = models.CharField(max_length=-1, blank=True, null=True)
    leadership = models.CharField(max_length=-1, blank=True, null=True)
    offtheball = models.CharField(max_length=-1, blank=True, null=True)
    positioning = models.CharField(max_length=-1, blank=True, null=True)
    teamwork = models.CharField(max_length=-1, blank=True, null=True)
    workrate = models.CharField(max_length=-1, blank=True, null=True)
    acceleration = models.CharField(max_length=-1, blank=True, null=True)
    agility = models.CharField(max_length=-1, blank=True, null=True)
    balance = models.CharField(max_length=-1, blank=True, null=True)
    jumping = models.CharField(max_length=-1, blank=True, null=True)
    leftfoot = models.CharField(max_length=-1, blank=True, null=True)
    naturalfitness = models.CharField(max_length=-1, blank=True, null=True)
    pace = models.CharField(max_length=-1, blank=True, null=True)
    rightfoot = models.CharField(max_length=-1, blank=True, null=True)
    stamina = models.CharField(max_length=-1, blank=True, null=True)
    strength = models.CharField(max_length=-1, blank=True, null=True)
    consistency = models.CharField(max_length=-1, blank=True, null=True)
    dirtiness = models.CharField(max_length=-1, blank=True, null=True)
    importantmatches = models.CharField(max_length=-1, blank=True, null=True)
    injuryproness = models.CharField(max_length=-1, blank=True, null=True)
    versatility = models.CharField(max_length=-1, blank=True, null=True)
    adaptability = models.CharField(max_length=-1, blank=True, null=True)
    ambition = models.CharField(max_length=-1, blank=True, null=True)
    loyalty = models.CharField(max_length=-1, blank=True, null=True)
    pressure = models.CharField(max_length=-1, blank=True, null=True)
    professional = models.CharField(max_length=-1, blank=True, null=True)
    sportsmanship = models.CharField(max_length=-1, blank=True, null=True)
    temperament = models.CharField(max_length=-1, blank=True, null=True)
    controversy = models.CharField(max_length=-1, blank=True, null=True)
    positionsdesc = models.CharField(max_length=-1, blank=True, null=True)
    goalkeeper = models.CharField(max_length=-1, blank=True, null=True)
    sweeper = models.CharField(max_length=-1, blank=True, null=True)
    striker = models.CharField(max_length=-1, blank=True, null=True)
    attackingmidcentral = models.CharField(max_length=-1, blank=True, null=True)
    attackingmidleft = models.CharField(max_length=-1, blank=True, null=True)
    attackingmidright = models.CharField(max_length=-1, blank=True, null=True)
    defendercentral = models.CharField(max_length=-1, blank=True, null=True)
    defenderleft = models.CharField(max_length=-1, blank=True, null=True)
    defenderright = models.CharField(max_length=-1, blank=True, null=True)
    defensivemidfielder = models.CharField(max_length=-1, blank=True, null=True)
    midfieldercentral = models.CharField(max_length=-1, blank=True, null=True)
    midfielderleft = models.CharField(max_length=-1, blank=True, null=True)
    midfielderright = models.CharField(max_length=-1, blank=True, null=True)
    wingbackleft = models.CharField(max_length=-1, blank=True, null=True)
    wingbackright = models.CharField(max_length=-1, blank=True, null=True)
    scoreid = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'score'
