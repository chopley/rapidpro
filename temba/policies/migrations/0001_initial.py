# Generated by Django 1.11.6 on 2018-05-21 22:19
from __future__ import unicode_literals

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="Consent",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "revoked_on",
                    models.DateTimeField(default=None, help_text="When this consent was revoked", null=True),
                ),
                (
                    "created_on",
                    models.DateTimeField(
                        blank=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        help_text="When consent was given by clicking on web form",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Policy",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "is_active",
                    models.BooleanField(
                        default=True, help_text="Whether this item is active, use this instead of deleting"
                    ),
                ),
                (
                    "created_on",
                    models.DateTimeField(
                        blank=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        help_text="When this item was originally created",
                    ),
                ),
                (
                    "modified_on",
                    models.DateTimeField(
                        blank=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        help_text="When this item was last modified",
                    ),
                ),
                (
                    "policy_type",
                    models.CharField(
                        choices=[
                            ("privacy", "Privacy Policy"),
                            ("tos", "Terms of Service"),
                            ("cookie", "Cookie Policy"),
                        ],
                        help_text="Choose the type of policy",
                        max_length=16,
                    ),
                ),
                ("body", models.TextField(help_text="Enter the content of the policy (Markdown permitted)")),
                (
                    "summary",
                    models.TextField(
                        blank=True, help_text="Summary of policy changes (Markdown permitted)", null=True
                    ),
                ),
                ("requires_consent", models.BooleanField(default=True, help_text="Is Consent Required?")),
                (
                    "created_by",
                    models.ForeignKey(
                        help_text="The user which originally created this item",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="policies_policy_creations",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        help_text="The user which last modified this item",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="policies_policy_modifications",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.AddField(
            model_name="consent",
            name="policy",
            field=models.ForeignKey(
                help_text="The policy the user is consenting to",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="policies",
                to="policies.Policy",
            ),
        ),
        migrations.AddField(
            model_name="consent",
            name="user",
            field=models.ForeignKey(
                help_text="The user consenting to this policy",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]