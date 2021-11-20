from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, email, firstname, lastname, address, city, barangay, birthdate, age, gender, 
    licensenumber, licenseexpiry, licensepic, contactnumber, specialization, schedule, password=None): #by default password is blank

        #check if anything required is missing
        if not email:
            raise ValueError("Users must have an email address.")
        if not firstname:
            raise ValueError("Users must enter their first name.")
        if not lastname:
            raise ValueError("Users must enter their last name.")
        if not address:
            raise ValueError("Users must have an address.")
        if not city:
            raise ValueError("Users must enter a city.")
        if not barangay:
            raise ValueError("Users must enter their barangay.")
        if not licensenumber:
            raise ValueError("Users must enter their license number.")
        if not licenseexpiry:
            raise ValueError("Users must enter their license expiry date.")
        if not contactnumber:
            raise ValueError("Users must enter their contact number..")
        if not specialization:
            raise ValueError("Users must enter their specialization.")
        if not schedule:
            raise ValueError("Users must enter their schedule.")
        
        #if everything is in order
        user = self.model(email=self.normalize_email(email), firstname = firstname, lastname = lastname, address = address, city = city, barangay = barangay,
        birthdate = birthdate, age = age, gender = gender, licensenumber = licensenumber, licenseexpiry = licenseexpiry, licensepic=licensepic, contactnumber = contactnumber,
        specialization = specialization, schedule=schedule,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, firstname, lastname, address, city, barangay, birthdate, age, gender, 
    licensenumber, licenseexpiry, licensepic, contactnumber, specialization, schedule, password):
        #check if anything required is missing
        if not email:
            raise ValueError("Users must have an email address.")
        if not firstname:
            raise ValueError("Users must enter their first name.")
        if not lastname:
            raise ValueError("Users must enter their last name.")
        if not licensenumber:
            raise ValueError("Users must enter their license number.")
        if not licenseexpiry:
            raise ValueError("Users must enter their license expiry date.")
        if not contactnumber:
            raise ValueError("Users must enter their contact number..")
        if not specialization:
            raise ValueError("Users must enter their specialization.")

        #if everything is in order
        user = self.create_user(
            email=self.normalize_email(email), 
            firstname = firstname, 
            lastname = lastname, 
            address = address, 
            city = city,
            barangay = barangay,
            birthdate = birthdate, 
            age = age, 
            gender = gender, 
            licensenumber = licensenumber,
            licenseexpiry = licenseexpiry,
            licensepic=licensepic, 
            contactnumber = contactnumber,
            specialization = specialization, 
            schedule=schedule,
            password=password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser, PermissionsMixin):
#required by django superuser
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
#username = models.CharField(max_length=200, null = True, unique = True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateField(verbose_name="last login", auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_Doctor = True
    is_LGUEmployee = False

#added fields
    firstname = models.CharField(max_length=200, null=True, verbose_name="first name")
    lastname = models.CharField(max_length=200, null=True, verbose_name="last name")
    address = models.CharField(max_length=200, null=True)
    barangay = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    birthdate = models.DateField(verbose_name="birth date", blank=True)
    age = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=200, null=True, choices=( 
                ('Male', 'Male'),
                ('Female', 'Female'),
    ), blank=True)
    licensenumber = models.CharField(verbose_name = "license number", max_length=200, null=True)
    licenseexpiry = models.DateField(verbose_name= "license expiry")
    licensepic = models.ImageField(verbose_name= "license picture", null = True, blank=True, upload_to = "pic_uploads/")
    contactnumber = models.CharField(max_length=200, null=True, verbose_name="contact number")
    specialization = models.CharField(max_length=200, null=True, choices=(
                    ('General Practitioner', 'General Practitioner'),
                    ('Family Medicine', 'Family Medicine'),
    ))
    schedule = models.CharField(max_length=200, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname', 'address', 'barangay', 'city', 'licensenumber', 'licenseexpiry', 'birthdate', 'age', 'gender', 'licensepic',    
    'contactnumber', 'specialization', 'schedule']

    objects = MyAccountManager() 

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj = None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def getFullName(self):
        return str(self.firstname + " " + self.lastname).title()

    def getAddress(self):
        return (str(self.address) + ", " + str(self.barangay) + ", " + str(self.city)).title()

    def getAge(self):
        return str(self.age)

    def getBirthdate(self):
        return str(self.birthdate)
    
    def getGender(self):
        return str(self.gender).title()

    def getLicenseNum(self):
        return str(self.licensenumber)

    def getLicenseExp(self):
        return str(self.licenseexpiry)

    def getLicensePic(self):
        return str(self.licensepic)

    def getContactNum(self):
        return str(self.contactnumber)

    def getSpecialization(self):
        return str(self.specialization).title()

    def getSchedule(self):
        return str(self.schedule).title()

    def is_Doc(self):
        return self.is_Doctor

    def is_LGU(self):
        return self.is_LGUEmployee

class LGUAccount(AbstractBaseUser, PermissionsMixin):
#required by django superuser
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
#username = models.CharField(max_length=200, null = True, unique = True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateField(verbose_name="last login", auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_LGUEmployee = True
    is_Doctor = False

#added fields
    firstname = models.CharField(max_length=200, null=True, verbose_name="first name")
    lastname = models.CharField(max_length=200, null=True, verbose_name="last name")
    address = models.CharField(max_length=200, null=True)
    barangay = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    birthdate = models.DateField(verbose_name="birth date")
    age = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=200, null=True, choices=( 
                ('Male', 'Male'),
                ('Female', 'Female'),
    ))
    employeenumber = models.CharField(verbose_name = "employee number", max_length=200, null=True)
    contactnumber = models.CharField(max_length=200, null=True, verbose_name="contact number")
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname', 'address', 'barangay', 'city', 'employeenumber','contactnumber', "password1", "password2"]

    objects = MyAccountManager() 

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj = None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def getFullName(self):
        return str(self.firstname + " " + self.lastname).title()

    def getAge(self):
        return str(self.age)

    def getAddress(self):
         return (str(self.address) + ", " + str(self.barangay) + ", " + str(self.city)).title()
    
    def getBirthdate(self):
        return str(self.birthdate)
    
    def getGender(self):
        return str(self.gender).title()

    def getEmployeeNum(self):
        return str(self.employeenumber)

    def getContactNum(self):
        return str(self.contactnumber)
    
    def is_Doc(self):
        return self.is_Doctor

    def is_LGU(self):
        return self.is_LGUEmployee