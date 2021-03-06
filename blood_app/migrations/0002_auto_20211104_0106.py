# Generated by Django 3.2.8 on 2021-11-03 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blood_donor',
            name='city',
        ),
        migrations.AddField(
            model_name='blood_donor',
            name='district',
            field=models.CharField(choices=[('B.baria', 'B.baria'), ('Bagerhat', 'Bagerhat'), ('Bandarban', 'Bandarban'), ('Barguna', 'Barguna'), ('Barishal', 'Barishal'), ('Bhola', 'Bhola'), ('Bogura', 'Bogura'), ('C. nawabganj', 'C. nawabganj'), ('Chandpur', 'Chandpur'), ('Chattogram', 'Chattogram'), ('Chuadanga', 'Chuadanga'), ("Cox's bazar", "Cox's bazar"), ('Cumilla', 'Cumilla'), ('Dhaka', 'Dhaka'), ('Dinajpur', 'Dinajpur'), ('Faridpur', 'Faridpur'), ('Feni', 'Feni'), ('Gaibandha', 'Gaibandha'), ('Gazipur', 'Gazipur'), ('Gopalganj', 'Gopalganj'), ('Habiganj', 'Habiganj'), ('Jamalpur', 'Jamalpur'), ('Jashore', 'Jashore'), ('Jhalokathi', 'Jhalokathi'), ('Jhenaidah', 'Jhenaidah'), ('Joypurhat', 'Joypurhat'), ('Khagrachari', 'Khagrachari'), ('Khulna', 'Khulna'), ('Kishoreganj', 'Kishoreganj'), ('Kurigram', 'Kurigram'), ('Kushtia', 'Kushtia'), ('Lalmonirhat', 'Lalmonirhat'), ('Laxmipur', 'Laxmipur'), ('Madaripur', 'Madaripur'), ('Magura', 'Magura'), ('Manikganj', 'Manikganj'), ('Meherpur', 'Meherpur'), ('Moulvibazar', 'Moulvibazar'), ('Munshiganj', 'Munshiganj'), ('Mymensingh', 'Mymensingh'), ('Naogaon', 'Naogaon'), ('Narail', 'Narail'), ('Narayanganj', 'Narayanganj'), ('Narshingdi', 'Narshingdi'), ('Natore', 'Natore'), ('Netrokona', 'Netrokona'), ('Nilphamari', 'Nilphamari'), ('Noakhali', 'Noakhali'), ('Pabna', 'Pabna'), ('Panchagarh', 'Panchagarh'), ('Patuakhali', 'Patuakhali'), ('Pirojpur', 'Pirojpur'), ('Rajbari', 'Rajbari'), ('Rajshahi', 'Rajshahi'), ('Rangamati', 'Rangamati'), ('Rangpur', 'Rangpur'), ('Satkhira', 'Satkhira'), ('Shariatpur', 'Shariatpur'), ('Sherpur', 'Sherpur'), ('Sirajganj', 'Sirajganj'), ('Sunamganj', 'Sunamganj'), ('Sylhet', 'Sylhet'), ('Tangail', 'Tangail'), ('Thakurgaon', 'Thakurgaon')], max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='blood_donor',
            name='blood_type',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=12),
        ),
        migrations.AlterField(
            model_name='blood_donor',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=122),
        ),
    ]
