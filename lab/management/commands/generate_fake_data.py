from django.core.management.base import BaseCommand
from django.db import transaction
from lab.factory import (
    DepartmentFactory,
    ReferralTypeFactory,
    PatientFactory,
    TestFactory,
    ReferralFactory,
    BillingFactory,
    PaymentDetailFactory,
    AppointmentFactory,
    AppointmentTestFactory,
)


class Command(BaseCommand):
    help = "Generate batch fake data for all models using factories"

    def add_arguments(self, parser):
        parser.add_argument(
            '--batch-size', type=int, default=10,
            help='Number of records to generate for each model (default: 10)'
        )

    def handle(self, *args, **options):
        batch_size = options['batch_size']

        # List of factories to use for data generation
        factories = [
            (DepartmentFactory, "Departments"),
            (ReferralTypeFactory, "Referral Types"),
            (PatientFactory, "Patients"),
            (TestFactory, "Tests"),
            (ReferralFactory, "Referrals"),
            (BillingFactory, "Billings"),
            (PaymentDetailFactory, "Payment Details"),
            (AppointmentFactory, "Appointments"),
            (AppointmentTestFactory, "Appointment Tests"),
        ]

        try:
            with transaction.atomic():  # Begin a transaction block
                for factory_class, model_name in factories:
                    self.stdout.write(f"Generating {batch_size} {model_name}...")
                    factory_class.create_batch(batch_size)
                    self.stdout.write(f"Successfully generated {batch_size} {model_name}.")

                self.stdout.write(self.style.SUCCESS("All data generated successfully!"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error occurred: {str(e)}"))
            self.stderr.write(self.style.ERROR("Rolling back database changes."))
