# Generated by Django 5.1.3 on 2025-02-20 11:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('appointment_id', models.CharField(max_length=20, unique=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.CharField(choices=[('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], max_length=50)),
                ('remarks', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('medical_history', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReferralType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('payment_type', models.CharField(choices=[('Online', 'Online'), ('Cash', 'Cash'), ('Cheque', 'Cheque')], default='Cash', max_length=50)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('final_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_status', models.CharField(choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], max_length=50)),
                ('transaction_id', models.CharField(blank=True, max_length=100, null=True)),
                ('appointment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lab.appointment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.patient'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='referral',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.referral'),
        ),
        migrations.AddField(
            model_name='referral',
            name='type_of_referral',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lab.referraltype'),
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('test_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lab.department')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AppointmentTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('test_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.appointment')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.test')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
