import uuid
import datetime
from django.db import models


class Bank(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    name = models.TextField(max_length=255, blank=False, null=False)
    base_url = models.TextField(max_length=255, blank=False, null=False)
    scrapping_period = models.IntegerField(blank=False, null=False)
    status = models.TextField(max_length=50, blank=False, null=False)
    deleted = models.PositiveSmallIntegerField(
        default=0, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Bank"
        verbose_name_plural = "Banks"

    def __unicode__(self):
        return '%s %s %s %s %s %s %s %s' % (self.id, self.name, self.base_url, self.scrapping_period, self.status, self.deleted, self.created_at, self.updated_at)


class Account(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    bank_id = models.ForeignKey(
        Bank, default=uuid.uuid4, max_length=36, on_delete=models.DO_NOTHING)
    partner_id = models.UUIDField(default=uuid.uuid4, max_length=36)
    account_name = models.TextField(max_length=100, blank=False, null=False)
    account_number = models.TextField(max_length=50, blank=False, null=False)
    status = models.TextField(max_length=50, blank=False, null=False)
    deleted = models.PositiveSmallIntegerField(
        default=0, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"

    def __unicode__(self):
        return '%s %s %s %s %s %s %s %s' % (self.id, self.bank_id, self.partner_id, self.account_name, self.account_number, self.status, self.deleted, self.created_at, self.updated_at)


class AccountMeta(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    account_id = models.ForeignKey(
        Account, default=uuid.uuid4, max_length=36, on_delete=models.DO_NOTHING)
    key = models.TextField(max_length=255, blank=False, null=False)
    value = models.TextField(max_length=500, blank=False, null=False)
    deleted = models.PositiveSmallIntegerField(
        default=0, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "AccountMeta"
        verbose_name_plural = "AccountMetas"
        db_table = "account_meta"

    def __unicode__(self):
        return '%s %s %s %s %s %s %s %s' % (self.id, self.account_id, self.key, self.value, self.deleted, self.created_at, self.updated_at)


class AccountTransaction(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    account_id = models.ForeignKey(
        Account, default=uuid.uuid4, max_length=36, on_delete=models.DO_NOTHING)
    post_date = models.DateTimeField(blank=False, null=False)
    debit = models.BigIntegerField(blank=False, null=False)
    credit = models.BigIntegerField(blank=False, null=False)
    balance = models.BigIntegerField(blank=False, null=False)
    note = models.TextField(max_length=500, blank=False, null=False)
    status = models.TextField(max_length=50, blank=False, null=False)
    deleted = models.PositiveSmallIntegerField(
        default=0, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "AccountMeta"
        verbose_name_plural = "AccountMetas"
        db_table = "account_transaction"

    def __unicode__(self):
        return '%s %s %s %s %s %s %s %s' % (self.id, self.account_id, self.post_date, self.debit, self.credit, self.balance, self.note, self.status, self.deleted, self.created_at, self.updated_at)


class TransferAmount(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    account_id = models.UUIDField(max_length=36)
    amount = models.TextField(max_length=255, blank=False, null=False)
    description = models.TextField(max_length=255, blank=True, null=True)
    status = models.TextField(max_length=50, blank=False, null=False)
    deleted = models.PositiveSmallIntegerField(
        default=0, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "TransferAmount"
        verbose_name_plural = "TransferAmounts"
        db_table = "transfer_amount"

    def __unicode__(self):
        return '%s %s %s %s %s %s %s %s' % (self.id, self.account_id, self.amount, self.description, self.status, self.deleted, self.created_at, self.updated_at)


class TransferRequest(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    account_id = models.ForeignKey(
        Account, default=uuid.uuid4, max_length=36, on_delete=models.DO_NOTHING)
    transfer_amount_id = models.ForeignKey(
        TransferAmount, default=uuid.uuid4, max_length=36, on_delete=models.DO_NOTHING)
    status = models.TextField(max_length=50, blank=False, null=False)
    real_amount = models.BigIntegerField(blank=False, null=False)
    deleted = models.PositiveSmallIntegerField(
        default=0, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "TransferRequest"
        verbose_name_plural = "TransferRequest"
        db_table = "transfer_request"

    def __unicode__(self):
        return '%s %s %s %s %s %s %s %s' % (self.id, self.account_id, self.transfer_amount_id, self.status, self.real_amount, self.deleted, self.created_at, self.updated_at)


class SystemConfig(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    key = models.TextField(max_length=255, blank=False, null=False)
    value = models.TextField(max_length=500, blank=False, null=True)
    deleted = models.PositiveSmallIntegerField(
        default=0, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "SystemConfig"
        verbose_name_plural = "SystemConfigs"
        db_table = "system_config"

    def __unicode__(self):
        return '%s %s %s %s %s %s %s %s %$' % (self.id, self.key, self.value, self.deleted, self.created_at, self.updated_at)


class SystemApp(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    name = models.TextField(max_length=100, blank=False, null=False)
    api_key = models.TextField(max_length=255, blank=False, null=False)
    type = models.TextField(max_length=50, blank=False, null=False)
    status = models.TextField(max_length=50, blank=False, null=False)
    ip = models.TextField(max_length=255, blank=False, null=True)
    deleted = models.PositiveSmallIntegerField(
        default=0, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "SystemApp"
        verbose_name_plural = "SystemApps"
        db_table = "system_app"

    def __unicode__(self):
        return '%s %s %s %s %s %s %s %s %$' % (self.id, self.name, self.api_key, self.type, self.status, self.ip, self.deleted, self.created_at, self.updated_at)
