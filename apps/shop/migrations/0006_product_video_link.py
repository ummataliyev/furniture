# Generated by Django 5.1.4 on 2024-12-25 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0005_alter_product_image_alter_productgallery_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="video_link",
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
