from tkinter.font import names

patient = ("Kim", 40, "100/60", 72)
print("1. Patient is", patient)
age = patient[1]
heart_rate = patient[3]
print("\n2. Age:", age, "Heart Rate:", heart_rate)

print("\n3. Tuples are suitable because:")
print("  -Patient vitals should not change accidentally (immutable)")
print("  -Data integrity is maintained")
print("  -Fixed structure ensures consistency")

patient_list = list(patient)
patient_list[3] = 68
patient_update = tuple(patient_list)
print("\n4. Updated patient:", patient_update)

patients = (
    ("Kim", 40, "100/60", 72),
    ("Yun", 32, "110/70", 65),
    ("Jing", 58, "130/85", 80),
    ("Jane", 29, "115/75", 70),
    ("Julie", 41, "125/80", 75)
)
patient_names = [patient[0] for patient in patients]
print("\n5. Patient names:", patient_names)