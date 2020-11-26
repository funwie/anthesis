class Farm(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Field(models.Model):
    size = models.DecimalField()
    produce = models.CharField(max_length=500)
    description = models.CharField(max_length=255)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)

    def __str__(self):
        return self.description