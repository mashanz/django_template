# Generated by Django 4.2.11 on 2024-03-07 23:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = []

    operations = [
        migrations.RunSQL(
            sql=[
                (
                    """
                        CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
                    """
                ),
                (
                    """
                        CREATE SCHEMA IF NOT EXISTS "master_data";
                    """
                ),
                (
                    """
                        CREATE TABLE IF NOT EXISTS "master_data"."province" (
                            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
                            name VARCHAR(100) NOT NULL,
                            updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                        );
                    """
                ),
            ],
            reverse_sql=[
                (
                    """
                        DROP TABLE IF NOT EXISTS "master_data"."province";
                    """
                ),
                (
                    """
                        DROP SCHEMA IF EXISTS "master_data";
                    """
                ),
            ],
        )
    ]
