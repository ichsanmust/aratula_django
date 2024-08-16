from django.db import models

class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100, blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=255, blank=True, null=True)
    modified_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'

class Levels(models.Model):
    level_id = models.AutoField(primary_key=True)
    level_name = models.CharField(max_length=100, blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=255, blank=True, null=True)
    modified_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'levels'


class Recipes(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    level = models.ForeignKey(Levels, models.DO_NOTHING, blank=True, null=True)
    recipe_name = models.CharField(max_length=255, blank=True, null=True)
    image_filename = models.TextField(blank=True, null=True)
    time_cook = models.IntegerField(blank=True, null=True)
    ingredient = models.TextField(blank=True, null=True)
    how_to_cook = models.TextField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=255, blank=True, null=True)
    modified_time = models.DateTimeField(blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recipes'
        # ordering = ['-recipe_name']