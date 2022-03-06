from django.db import models


class TqBaseModel(models.Model):
    # Abstract model to track creation/update of a model
    created_date = models.DateTimeField(
        auto_now_add=True, null=True, blank=True, editable=False)
    updated_date = models.DateTimeField(
        auto_now=True, null=True, blank=True, editable=False)
    is_active = models.BooleanField(verbose_name="Active Item", default=True)

    class Meta:
        abstract = True


class Docuware(TqBaseModel):
    Document_ID = models.CharField(max_length=250, blank=True, null=True)
    Payee_Name = models.CharField(max_length=250, blank=True, null=True)
    Payment_Requisition_Number = models.CharField(
        max_length=250, blank=True, null=True)
    FMS_Process = models.CharField(max_length=50, blank=True, null=True)
    TQ_Status = models.CharField(max_length=50, blank=True, null=True)
    Amount = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.Document_ID
