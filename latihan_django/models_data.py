# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FavoriteFoods(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    recipe = models.ForeignKey('Recipes', models.DO_NOTHING, blank=True, null=True)
    is_favorite = models.BooleanField(blank=True, null=True)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=255, blank=True, null=True)
    modified_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'favorite_foods'


class HowToCooks(models.Model):
    how_to_cook_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'how_to_cooks'


class Ingridients(models.Model):
    ingridient_id = models.BigIntegerField(primary_key=True)
    ingridient_measurement = models.CharField(max_length=255, blank=True, null=True)
    ingridient_name = models.CharField(max_length=255, blank=True, null=True)
    ingridient_quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingridients'


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


class RecipeHowToCook(models.Model):
    how_to_cook = models.OneToOneField(HowToCooks, models.DO_NOTHING, primary_key=True)
    recipe = models.ForeignKey('Recipes', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'recipe_how_to_cook'
        unique_together = (('how_to_cook', 'recipe'),)


class RecipeIngridient(models.Model):
    ingridient = models.OneToOneField(Ingridients, models.DO_NOTHING, primary_key=True)
    recipe = models.ForeignKey('Recipes', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'recipe_ingridient'
        unique_together = (('ingridient', 'recipe'),)


class Recipes(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
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


class Roles(models.Model):
    role_id = models.BigIntegerField(primary_key=True)
    role_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    fullname = models.CharField(max_length=255, blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=255, blank=True, null=True)
    modified_time = models.DateTimeField(blank=True, null=True)
    role_0 = models.ForeignKey(Roles, models.DO_NOTHING, db_column='role_id', blank=True, null=True)  # Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'users'
