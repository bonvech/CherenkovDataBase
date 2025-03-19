from django.db import models


class Computer(models.Model):
    ip = models.CharField(max_length=15)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Disk(models.Model):
    computer = models.ForeignKey(Computer, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Model_Atmosphere(models.Model):
    name = models.CharField(max_length=40)
    code = models.CharField(max_length=4)

    def __str__(self):
        return self.name


class Model_Interaction(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Particle(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=4)

    def __str__(self):
        return self.name


class Event(models.Model):
    disk = models.ForeignKey(Disk, on_delete=models.DO_NOTHING)
    model_atmosphere = models.ForeignKey(Model_Atmosphere, on_delete=models.DO_NOTHING)
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
