from django.db import models
from django.utils import timezone

# 1. Base Model for Soft Deleting (Archive Feature)
class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
        self.save()

# 2. HOA Registry Profile
class HoaProfile(SoftDeleteModel):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Suspended', 'Suspended'),
        ('No legal standing', 'No legal standing'),
        ('Dissolved', 'Dissolved'),
        ('Revoked', 'Revoked'),
        ('Term expired', 'Term expired'),
        ('Pending', 'Pending'),
    ]

    # Basic Info
    name = models.CharField(max_length=255, unique=True)
    certificate_of_incorporation = models.CharField(max_length=100, blank=True, null=True)
    registration_type = models.CharField(max_length=100)
    issuance_date = models.DateField(blank=True, null=True)
    classification = models.CharField(max_length=100, blank=True, null=True)
    
    # Location
    barangay = models.CharField(max_length=100)
    city_municipality = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    
    # Contact
    contact_person = models.CharField(max_length=255)
    contact_details = models.CharField(max_length=255)
    
    # Governance
    total_members = models.IntegerField(default=0)
    date_of_election = models.DateField(blank=True, null=True)
    term_of_office = models.CharField(max_length=50, blank=True, null=True)
    
    # Status & System
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# 3. Notice of Violation (NOV)
class NoticeOfViolation(SoftDeleteModel):
    control_no = models.CharField(max_length=100, unique=True)
    hoa = models.ForeignKey(HoaProfile, on_delete=models.CASCADE, related_name='novs')
    
    # Violations (Checkboxes converted to Booleans)
    violation_sec_64 = models.BooleanField(default=False, verbose_name="Section 64")
    violation_sec_101 = models.BooleanField(default=False, verbose_name="Section 101")
    violation_sec_62 = models.BooleanField(default=False, verbose_name="Section 62")
    
    date_issued = models.DateField()
    evaluator = models.CharField(max_length=150)

    def __str__(self):
        return f"NOV {self.control_no} - {self.hoa.name}"

# 4. Order To Perform (OTP)
class OrderToPerform(SoftDeleteModel):
    control_no = models.CharField(max_length=100, unique=True)
    hoa = models.ForeignKey(HoaProfile, on_delete=models.CASCADE, related_name='otps')
    nov_reference = models.ForeignKey(NoticeOfViolation, on_delete=models.SET_NULL, null=True, blank=True)
    
    submission_comment = models.TextField()
    date_issued = models.DateField()
    evaluator = models.CharField(max_length=150)
    mr_status = models.CharField(max_length=100, help_text="Motion for Reconsideration Status")

    def __str__(self):
        return f"OTP {self.control_no} - {self.hoa.name}"

# 5. Order for Investigation (OIAS)
class OrderForInvestigation(SoftDeleteModel):
    SANCTION_CHOICES = [
        ('1', 'Censure'),
        ('2', 'Fine'),
        ('3', 'Suspension of Privileges'),
        ('4', 'Suspension of Board'),
        ('5', 'Removal of Officers'),
        ('6', 'Revocation'),
    ]

    control_no = models.CharField(max_length=100, unique=True)
    hoa = models.ForeignKey(HoaProfile, on_delete=models.CASCADE, related_name='investigations')
    nov_reference = models.ForeignKey(NoticeOfViolation, on_delete=models.SET_NULL, null=True, blank=True)
    
    penalties = models.CharField(max_length=50, choices=SANCTION_CHOICES)
    date_issued = models.DateField()
    evaluator = models.CharField(max_length=150)
    mr_status = models.CharField(max_length=100)

    def __str__(self):
        return f"OIAS {self.control_no} - {self.hoa.name}"