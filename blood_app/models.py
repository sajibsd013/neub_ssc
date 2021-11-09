from django.db import models

# Create your models here.


class Blood_donor(models.Model):
    gender_l = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Others", "Others")
    )

    b_type = (
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
        ("O+", "O+"),
        ("O-", "O-")
    )

    district_l = (
        ('B.baria', 'B.baria'),
        ('Bagerhat', 'Bagerhat'),
        ('Bandarban', 'Bandarban'),
        ('Barguna', 'Barguna'),
        ('Barishal', 'Barishal'),
        ('Bhola', 'Bhola'),
        ('Bogura', 'Bogura'),
        ('C. nawabganj', 'C. nawabganj'),
        ('Chandpur', 'Chandpur'),
        ('Chattogram', 'Chattogram'),
        ('Chuadanga', 'Chuadanga'),
        ("Cox's bazar", "Cox's bazar"),
        ('Cumilla', 'Cumilla'),
        ('Dhaka', 'Dhaka'),
        ('Dinajpur', 'Dinajpur'),
        ('Faridpur', 'Faridpur'),
        ('Feni', 'Feni'),
        ('Gaibandha', 'Gaibandha'),
        ('Gazipur', 'Gazipur'),
        ('Gopalganj', 'Gopalganj'),
        ('Habiganj', 'Habiganj'),
        ('Jamalpur', 'Jamalpur'),
        ('Jashore', 'Jashore'),
        ('Jhalokathi', 'Jhalokathi'),
        ('Jhenaidah', 'Jhenaidah'),
        ('Joypurhat', 'Joypurhat'),
        ('Khagrachari', 'Khagrachari'),
        ('Khulna', 'Khulna'),
        ('Kishoreganj', 'Kishoreganj'),
        ('Kurigram', 'Kurigram'),
        ('Kushtia', 'Kushtia'),
        ('Lalmonirhat', 'Lalmonirhat'),
        ('Laxmipur', 'Laxmipur'),
        ('Madaripur', 'Madaripur'),
        ('Magura', 'Magura'),
        ('Manikganj', 'Manikganj'),
        ('Meherpur', 'Meherpur'),
        ('Moulvibazar', 'Moulvibazar'),
        ('Munshiganj', 'Munshiganj'),
        ('Mymensingh', 'Mymensingh'),
        ('Naogaon', 'Naogaon'),
        ('Narail', 'Narail'),
        ('Narayanganj', 'Narayanganj'),
        ('Narshingdi', 'Narshingdi'),
        ('Natore', 'Natore'),
        ('Netrokona', 'Netrokona'),
        ('Nilphamari', 'Nilphamari'),
        ('Noakhali', 'Noakhali'),
        ('Pabna', 'Pabna'),
        ('Panchagarh', 'Panchagarh'),
        ('Patuakhali', 'Patuakhali'),
        ('Pirojpur', 'Pirojpur'),
        ('Rajbari', 'Rajbari'),
        ('Rajshahi', 'Rajshahi'),
        ('Rangamati', 'Rangamati'),
        ('Rangpur', 'Rangpur'),
        ('Satkhira', 'Satkhira'),
        ('Shariatpur', 'Shariatpur'),
        ('Sherpur', 'Sherpur'),
        ('Sirajganj', 'Sirajganj'),
        ('Sunamganj', 'Sunamganj'),
        ('Sylhet', 'Sylhet'),
        ('Tangail', 'Tangail'),
        ('Thakurgaon', 'Thakurgaon')

    )

    name = models.CharField(max_length=122)
    email = models.EmailField()
    phone = models.CharField(max_length=122)
    blood_type = models.CharField(choices=b_type, max_length=12)
    gender = models.CharField(choices=gender_l, max_length=122)
    district = models.CharField(choices=district_l, max_length=122,null=True)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    last_donate = models.DateField(blank=True, null=True)
    address = models.TextField()
