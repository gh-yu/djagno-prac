# Generated by Django 4.0.4 on 2022-04-24 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fc_user', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='수량')),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='등록일')),
                ('fc_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fc_user.fcuser', verbose_name='사용자')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='상품')),
            ],
            options={
                'verbose_name': '주문',
                'verbose_name_plural': '주문',
                'db_table': 'fastcampus_order',
            },
        ),
    ]
