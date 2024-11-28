import factory
from factory.django import DjangoModelFactory
from datetime import date, timedelta
from .models import (
    Department, ReferralType, Patient, Test, Referral, 
    Billing, PaymentDetail, Appointment, AppointmentTest
)

from faker import Faker

fake = Faker()


class DepartmentFactory(DjangoModelFactory):
    class Meta:
        model = Department

    name = factory.Sequence(lambda n: f"Referral Type {n + 1}")


class ReferralTypeFactory(DjangoModelFactory):
    class Meta:
        model = ReferralType

    name = factory.Sequence(lambda n: f"Referral Type {n + 1}")


class PatientFactory(DjangoModelFactory):
    class Meta:
        model = Patient

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    date_of_birth = factory.Faker('date_of_birth', minimum_age=18, maximum_age=80)
    gender = factory.Iterator(['M', 'F', 'O'])
    phone =  factory.LazyAttribute(lambda _: fake.numerify(text='###########')[:15]) 
    email = factory.Faker('email')
    address = factory.Faker('address')
    medical_history = factory.Faker('paragraph')


class TestFactory(DjangoModelFactory):
    class Meta:
        model = Test

    parent = None  # Set to `None` for root-level tests; override as needed
    test_name = factory.Faker('word')
    description = factory.Faker('paragraph')
    department = factory.SubFactory(DepartmentFactory)
    price = factory.Faker('pydecimal', left_digits=5, right_digits=2, positive=True)


class ReferralFactory(DjangoModelFactory):
    class Meta:
        model = Referral

    name = factory.Faker('name')
    type_of_referral = factory.SubFactory(ReferralTypeFactory)
    percentage = factory.Faker('pydecimal', left_digits=2, right_digits=2, positive=True, max_value=100)


class BillingFactory(DjangoModelFactory):
    class Meta:
        model = Billing

    appointment = None  # Set to `None` by default; override as needed
    bill_type = factory.Iterator(['credit', 'debit'])
    total_amount = factory.Faker('pydecimal', left_digits=5, right_digits=2, positive=True)
    discount_amount = factory.Faker('pydecimal', left_digits=3, right_digits=2, positive=True)
    final_amount = factory.LazyAttribute(
        lambda obj: obj.total_amount - obj.discount_amount
    )
    payment_status = factory.Iterator(['Paid', 'Unpaid'])


class PaymentDetailFactory(DjangoModelFactory):
    class Meta:
        model = PaymentDetail

    billing = factory.SubFactory(BillingFactory)
    payment_type = factory.Iterator(['Online', 'Cash', 'Cheque'])
    transaction_id = factory.Faker('uuid4')
    cheque_number = factory.Maybe(
        factory.LazyAttribute(lambda o: o.payment_type == 'Cheque'),
        factory.Faker('bothify', text='CHEQ####'),
        None,
    )


class AppointmentFactory(DjangoModelFactory):
    class Meta:
        model = Appointment
    appointment_id = factory.LazyAttribute(
        lambda o: Faker().random_int(min=1000000000, max=9999999999)
    )
    patient = factory.SubFactory(PatientFactory)
    referral = factory.SubFactory(ReferralFactory)
    date = factory.Faker('date_between', start_date='-30d', end_date='+30d')
    time = factory.Faker('time_object')
    status = factory.Iterator(['Scheduled', 'Completed', 'Cancelled'])
    remarks = factory.Faker('paragraph')


class AppointmentTestFactory(DjangoModelFactory):
    class Meta:
        model = AppointmentTest

    appointment = factory.SubFactory(AppointmentFactory)
    test_name = factory.Faker('name')
    test_price = factory.Faker('pydecimal', left_digits=5, right_digits=2, positive=True)
