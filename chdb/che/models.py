from django.db import models


class Computer(models.Model):
    ip = models.CharField(max_length=15)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.ip


class Disk(models.Model):
    computer = models.ForeignKey(Computer, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Model_Atmosphere(models.Model):
    name = models.CharField(max_length=40)
    code = models.IntegerField()

    def __str__(self):
        return self.name

ModelAtmosphere = Model_Atmosphere


class Model_Grid(models.Model):
    name = models.CharField(max_length=10)
    fullname = models.CharField(max_length=50)
    spacing = models.FloatField()

    def __str__(self):
        return self.name

ModelGrid = Model_Grid


class Model_Interaction(models.Model):
    name = models.CharField(max_length=5)
    fullname = models.CharField(max_length=20)

    def __str__(self):
        return self.name

ModelInteraction = Model_Interaction


class Particle(models.Model):
    name = models.CharField(max_length=20)
    code = models.IntegerField()

    def __str__(self):
        return self.name


class Event(models.Model):
    disk = models.ForeignKey(Disk, on_delete=models.DO_NOTHING)
    model_atmosphere = models.ForeignKey(Model_Atmosphere, on_delete=models.DO_NOTHING)
    model_grid = models.ForeignKey(Model_Grid, on_delete=models.DO_NOTHING)
    model_interaction = models.ForeignKey(Model_Interaction, on_delete=models.DO_NOTHING)
    particle = models.ForeignKey(Particle, on_delete=models.DO_NOTHING)

    energy = models.FloatField()
    theta = models.FloatField()
    number = models.IntegerField()
    rand1 = models.IntegerField()
    rand2 = models.IntegerField()
    rand3 = models.IntegerField()
    filepath = models.CharField(max_length=250)
    filename = models.CharField(max_length=250)
    filesize = models.IntegerField()
    costheta = models.FloatField()
    phix = models.FloatField()
    phiy = models.FloatField()
    height = models.FloatField()
    frelectrons = models.IntegerField()
    frhadrons = models.IntegerField()
