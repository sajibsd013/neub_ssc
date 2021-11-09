from django import forms

class Search_donor(forms.Form):

    b_type = (
        ("", "Select Group"),
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
        ('',"Select District"),
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

    blood_type = forms.ChoiceField(choices=b_type, widget= forms.Select(attrs={'class': 'form-select'}) )
    district = forms.ChoiceField(choices=district_l, widget= forms.Select(attrs={'class': 'form-select'}) )



