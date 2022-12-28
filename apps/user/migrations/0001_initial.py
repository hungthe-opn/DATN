from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateUserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, verbose_name='email add')),
                ('user_name', models.CharField(default='Thành viên mới', max_length=150, null=True)),
                ('first_name', models.CharField(blank=True, max_length=150)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('about', models.TextField(blank=True, max_length=500, verbose_name='about')),
                ('rank', models.CharField(choices=[('Thành viên mới', 'Thành viên mới'), ('Người dùng', 'Người dùng'), ('Tác giả', 'Tác giả'), ('Fan cứng', 'Fan cứng'), ('Người có tầm ảnh hưởng', 'Người có tầm ảnh hưởng'), ('Chuyên gia bình luận', 'Chuyên gia bình luận'), ('Quản trị viên', 'Quản trị viên')], default='Thành viên mới', max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='image')),
                ('home', models.CharField(max_length=256, null=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_author', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_report', models.BooleanField(default=False)),
                ('delete', models.BooleanField(default=False)),
                ('is_employee', models.BooleanField(default=False)),
                ('sex', models.CharField(choices=[('Nam', 'Nam'), ('Nữ', 'Nữ'), ('Khác', 'Khác'), ('Bí mật', 'Bí mật'), ('', '')], default='', max_length=30)),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'tbl_user',
                'ordering': ['id'],
                'unique_together': {('email',)},
            },
        ),
        migrations.CreateModel(
            name='UserGroupModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('queue_id', models.CharField(blank=True, max_length=254, null=True)),
                ('is_default', models.BooleanField(blank=True, default=False, null=True)),
                ('caller_phone_number', models.CharField(blank=True, max_length=32, null=True)),
                ('deleted', models.BooleanField(blank=True, default=False, null=True)),
            ],
            options={
                'db_table': 'tbl_user_group',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('muted', models.BooleanField(default=False)),
                ('count', models.IntegerField(default=0)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followings', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tbl_user_follow',
                'unique_together': {('from_user', 'to_user')},
            },
        ),
    ]
