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
    name = models.CharField(max_length=100, blank=True, null=True)
    division = models.TextField(blank=True, null=True)
    based = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'club'


class Player(models.Model):
    playerid = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100, blank=True, null=True)
    clubid = models.BigIntegerField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    born = models.DateField(blank=True, null=True)
    height = models.PositiveIntegerField( blank=True, null=True)
    weight = models.PositiveIntegerField( blank=True, null=True)
    bestpos = models.TextField(blank=True, null=True)
    club = models.TextField(blank=True, null=True)
    nation = models.TextField(blank=True, null=True)
    preferredfoot = models.TextField(blank=True, null=True)
    value = models.PositiveIntegerField(blank=True, null=True)
    wage = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player'


class Score(models.Model):
    playerid = models.CharField(max_length=100, blank=True, null=True)
    aerialability = models.PositiveIntegerField( blank=True, null=True)
    commandofarea = models.PositiveIntegerField( blank=True, null=True)
    communication = models.PositiveIntegerField( blank=True, null=True)
    eccentricity = models.PositiveIntegerField( blank=True, null=True)
    handling = models.PositiveIntegerField( blank=True, null=True)
    kicking = models.PositiveIntegerField( blank=True, null=True)
    oneonones = models.PositiveIntegerField( blank=True, null=True)
    reflexes = models.PositiveIntegerField( blank=True, null=True)
    rushingout = models.PositiveIntegerField( blank=True, null=True)
    tendencytopunch = models.PositiveIntegerField( blank=True, null=True)
    throwing = models.PositiveIntegerField( blank=True, null=True)
    corners = models.PositiveIntegerField( blank=True, null=True)
    crossing = models.PositiveIntegerField( blank=True, null=True)
    dribbling = models.PositiveIntegerField( blank=True, null=True)
    finishing = models.PositiveIntegerField( blank=True, null=True)
    firsttouch = models.PositiveIntegerField( blank=True, null=True)
    freekicks = models.PositiveIntegerField( blank=True, null=True)
    heading = models.PositiveIntegerField( blank=True, null=True)
    longshots = models.PositiveIntegerField( blank=True, null=True)
    longthrows = models.PositiveIntegerField( blank=True, null=True)
    marking = models.PositiveIntegerField( blank=True, null=True)
    passing = models.PositiveIntegerField( blank=True, null=True)
    penaltytaking = models.PositiveIntegerField( blank=True, null=True)
    tackling = models.PositiveIntegerField( blank=True, null=True)
    technique = models.PositiveIntegerField( blank=True, null=True)
    aggression = models.PositiveIntegerField( blank=True, null=True)
    anticipation = models.PositiveIntegerField( blank=True, null=True)
    bravery = models.PositiveIntegerField( blank=True, null=True)
    composure = models.PositiveIntegerField( blank=True, null=True)
    concentration = models.PositiveIntegerField( blank=True, null=True)
    vision = models.PositiveIntegerField( blank=True, null=True)
    decisions = models.PositiveIntegerField( blank=True, null=True)
    determination = models.PositiveIntegerField( blank=True, null=True)
    flair = models.PositiveIntegerField( blank=True, null=True)
    leadership = models.PositiveIntegerField( blank=True, null=True)
    offtheball = models.PositiveIntegerField( blank=True, null=True)
    positioning = models.PositiveIntegerField( blank=True, null=True)
    teamwork = models.PositiveIntegerField( blank=True, null=True)
    workrate = models.PositiveIntegerField( blank=True, null=True)
    acceleration = models.PositiveIntegerField( blank=True, null=True)
    agility = models.PositiveIntegerField( blank=True, null=True)
    balance = models.PositiveIntegerField( blank=True, null=True)
    jumping = models.PositiveIntegerField( blank=True, null=True)
    leftfoot = models.PositiveIntegerField( blank=True, null=True)
    naturalfitness = models.PositiveIntegerField( blank=True, null=True)
    pace = models.PositiveIntegerField( blank=True, null=True)
    rightfoot = models.PositiveIntegerField( blank=True, null=True)
    stamina = models.PositiveIntegerField( blank=True, null=True)
    strength = models.PositiveIntegerField( blank=True, null=True)
    consistency = models.PositiveIntegerField( blank=True, null=True)
    dirtiness = models.PositiveIntegerField( blank=True, null=True)
    importantmatches = models.PositiveIntegerField( blank=True, null=True)
    injuryproness = models.PositiveIntegerField( blank=True, null=True)
    versatility = models.PositiveIntegerField( blank=True, null=True)
    adaptability = models.PositiveIntegerField( blank=True, null=True)
    ambition = models.PositiveIntegerField( blank=True, null=True)
    loyalty = models.PositiveIntegerField( blank=True, null=True)
    pressure = models.PositiveIntegerField( blank=True, null=True)
    professional = models.PositiveIntegerField( blank=True, null=True)
    sportsmanship = models.PositiveIntegerField( blank=True, null=True)
    temperament = models.PositiveIntegerField( blank=True, null=True)
    controversy = models.PositiveIntegerField( blank=True, null=True)
    positionsdesc = models.PositiveIntegerField( blank=True, null=True)
    goalkeeper = models.PositiveIntegerField( blank=True, null=True)
    sweeper = models.PositiveIntegerField( blank=True, null=True)
    striker = models.PositiveIntegerField( blank=True, null=True)
    attackingmidcentral = models.PositiveIntegerField( blank=True, null=True)
    attackingmidleft = models.PositiveIntegerField( blank=True, null=True)
    attackingmidright = models.PositiveIntegerField( blank=True, null=True)
    defendercentral = models.PositiveIntegerField( blank=True, null=True)
    defenderleft = models.PositiveIntegerField( blank=True, null=True)
    defenderright = models.PositiveIntegerField( blank=True, null=True)
    defensivemidfielder = models.PositiveIntegerField( blank=True, null=True)
    midfieldercentral = models.PositiveIntegerField( blank=True, null=True)
    midfielderleft = models.PositiveIntegerField( blank=True, null=True)
    midfielderright = models.PositiveIntegerField( blank=True, null=True)
    wingbackleft = models.PositiveIntegerField( blank=True, null=True)
    wingbackright = models.PositiveIntegerField( blank=True, null=True)
    scoreid = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'score'
