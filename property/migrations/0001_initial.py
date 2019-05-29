# Generated by Django 2.2.1 on 2019-05-23 19:43

from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255)),
                ('address', django.contrib.postgres.fields.jsonb.JSONField(encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('coordinates', django.contrib.postgres.fields.jsonb.JSONField(encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('property_type', models.CharField(choices=[('B', 'BUILDING'), ('E', 'EMPTY LOT')], default='B', max_length=1)),
                ('description', models.TextField()),
                ('list_date', models.DateField(blank=True, null=True)),
                ('is_published', models.BooleanField(default=False)),
                ('is_sold', models.BooleanField(default=False)),
                ('sold_at', models.DateTimeField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=14)),
                ('bedrooms', models.IntegerField(blank=True, null=True)),
                ('bathrooms', models.IntegerField(blank=True, null=True)),
                ('garages', models.IntegerField(blank=True, null=True)),
                ('lot_size', models.DecimalField(decimal_places=4, max_digits=8)),
                ('image_main', models.URLField()),
                ('image_others', django.contrib.postgres.fields.ArrayField(base_field=models.URLField(unique=True), blank=True, null=True, size=None)),
                ('view_count', models.IntegerField(default=0)),
                ('purchase_plan', models.CharField(choices=[('I', 'INSTALLMENTS'), ('F', 'FULL PAYMENT')], max_length=1)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='authentication.Client')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PropertyReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('comment', models.TextField()),
                ('is_published', models.BooleanField(default=True)),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewers', to=settings.AUTH_USER_MODEL)),
                ('target_property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewed_property', to='property.Property')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PropertyInspection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('inspection_time', models.DateTimeField()),
                ('remarks', models.TextField()),
                ('inspection_mode', models.CharField(choices=[('P', 'PHYSICAL INSPECTION'), ('V', 'VIDEO INSPECTION')], default='P', max_length=1)),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requesters', to=settings.AUTH_USER_MODEL)),
                ('target_property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inspected_property', to='property.Property')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PropertyEnquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('enquirer_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=17)),
                ('message', models.TextField(max_length=1000)),
                ('target_property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enquired_property', to='property.Property')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]