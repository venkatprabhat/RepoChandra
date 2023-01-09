# Generated by Django 3.0.8 on 2022-11-01 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PolicyDetails',
            fields=[
                ('policy_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('policy_name', models.TextField()),
                ('policy_description', models.TextField()),
                ('total_usage', models.IntegerField(help_text='Total usage for the policy')),
                ('price', models.IntegerField(default='-1', help_text='Price of the policy')),
                ('currency', models.TextField(default='INR')),
                ('details', models.TextField(blank=True, default='', help_text='policy details', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RazorPayDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant_id', models.TextField()),
                ('merchant_name', models.TextField()),
                ('access_key', models.TextField()),
                ('secret_key', models.TextField()),
                ('status', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserBasicInfo',
            fields=[
                ('user_id', models.CharField(help_text='Name of the operation', max_length=100, primary_key=True, serialize=False)),
                ('user_name', models.TextField()),
                ('email_id', models.EmailField(max_length=254)),
                ('phone_num', models.TextField()),
                ('status', models.TextField(default='000')),
            ],
        ),
        migrations.CreateModel(
            name='UserScope',
            fields=[
                ('user_id', models.CharField(help_text='Name of the operation', max_length=100, primary_key=True, serialize=False)),
                ('scope', models.TextField(default='users')),
            ],
        ),
        migrations.CreateModel(
            name='UserPolicyUsageDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_start_date', models.DateTimeField(blank=True, null=True)),
                ('policy_end_date', models.DateTimeField(blank=True, help_text='When the policy actually ends', null=True)),
                ('curr_policy_usage_count', models.IntegerField(default=0)),
                ('last_usage', models.DateTimeField(blank=True, null=True)),
                ('policy_status', models.TextField(default='active', help_text='The current status of policy attached. active / inactive')),
                ('policy_deactivation_date', models.DateTimeField(blank=True, help_text='When the current policy is deactivated.', null=True)),
                ('policy_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pecs_models.PolicyDetails')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pecs_models.UserBasicInfo')),
            ],
        ),
        migrations.CreateModel(
            name='UserOperation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('last_operation', models.TextField()),
                ('context', models.TextField(blank=True, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pecs_models.UserBasicInfo')),
            ],
        ),
        migrations.CreateModel(
            name='UserInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('max_speed', models.FloatField()),
                ('avg_speed', models.FloatField()),
                ('bat_acc_cyc', models.IntegerField()),
                ('mass_veh', models.FloatField()),
                ('max_weight', models.FloatField()),
                ('rad_wheel', models.FloatField()),
                ('mass_wheel', models.FloatField()),
                ('slope_angle', models.FloatField()),
                ('gearbox_i', models.FloatField()),
                ('gearbox_efficency', models.FloatField()),
                ('surface_vehicle', models.FloatField()),
                ('acc_time', models.IntegerField()),
                ('drive_time', models.IntegerField()),
                ('dec_time', models.IntegerField()),
                ('ground_material', models.IntegerField()),
                ('num_wheel', models.IntegerField()),
                ('input_json', models.TextField(blank=True, null=True)),
                ('result_json', models.TextField(blank=True, null=True)),
                ('request_id', models.TextField(default='')),
                ('policy_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pecs_models.PolicyDetails')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pecs_models.UserBasicInfo')),
            ],
        ),
        migrations.CreateModel(
            name='UserAccountDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billing_address', models.TextField()),
                ('policy_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pecs_models.PolicyDetails')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pecs_models.UserBasicInfo')),
            ],
        ),
        migrations.CreateModel(
            name='PolicyTransactionDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.TextField()),
                ('creation_date', models.DateTimeField()),
                ('transaction_date', models.DateTimeField(blank=True, null=True)),
                ('rp_payment_id', models.TextField(blank=True, null=True)),
                ('rp_signature', models.TextField(blank=True, null=True)),
                ('order_status', models.TextField()),
                ('rp_order_id', models.TextField(blank=True, null=True)),
                ('rp_order_response', models.TextField()),
                ('policy_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pecs_models.PolicyDetails')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pecs_models.UserBasicInfo')),
            ],
        ),
        migrations.CreateModel(
            name='OTPDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp_number', models.CharField(max_length=6)),
                ('otp_expired_time', models.DateTimeField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pecs_models.UserBasicInfo')),
            ],
        ),
    ]
