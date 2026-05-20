# Hospital Management System 

# Data storage
patients = []
doctors = [
    {"id": 1, "name": "Dr. Sharma", "specialization": "Cardiologist"},
    {"id": 2, "name": "Dr. Verma", "specialization": "Dermatologist"},
    {"id": 3, "name": "Dr. Khan", "specialization": "Neurologist"}
]
appointments = []


# Function to add patient
def add_patient():
    print("\n--- Add Patient ---")
    name = input("Enter patient name: ")
    age = input("Enter age: ")
    gender = input("Enter gender: ")

    patient_id = len(patients) + 1

    patient = {
        "id": patient_id,
        "name": name,
        "age": age,
        "gender": gender
    }

    patients.append(patient)
    print("Patient added successfully!\n")


# Function to view patients
def view_patients():
    print("\n--- Patient List ---")
    if not patients:
        print("No patients found.")
    else:
        for p in patients:
            print(f"ID: {p['id']}, Name: {p['name']}, Age: {p['age']}, Gender: {p['gender']}")
    print()


# Function to view doctors
def view_doctors():
    print("\n--- Doctor List ---")
    for d in doctors:
        print(f"ID: {d['id']}, Name: {d['name']}, Specialization: {d['specialization']}")
    print()


# Function to book appointment
def book_appointment():
    print("\n--- Book Appointment ---")
    
    if not patients:
        print("No patients available. Please add a patient first.\n")
        return

    view_patients()
    patient_id = int(input("Enter Patient ID: "))

    view_doctors()
    doctor_id = int(input("Enter Doctor ID: "))

    date = input("Enter appointment date (DD-MM-YYYY): ")

    appointment = {
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "date": date
    }

    appointments.append(appointment)
    print("Appointment booked successfully!\n")


# Function to view appointments
def view_appointments():
    print("\n--- Appointments ---")
    if not appointments:
        print("No appointments found.\n")
        return

    for a in appointments:
        patient_name = next((p['name'] for p in patients if p['id'] == a['patient_id']), "Unknown")
        doctor_name = next((d['name'] for d in doctors if d['id'] == a['doctor_id']), "Unknown")

        print(f"Patient: {patient_name}, Doctor: {doctor_name}, Date: {a['date']}")
    print()


# Main menu
def main():
    while True:
        print("===== Hospital Management System =====")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. View Doctors")
        print("4. Book Appointment")
        print("5. View Appointments")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_patient()
        elif choice == '2':
            view_patients()
        elif choice == '3':
            view_doctors()
        elif choice == '4':
            book_appointment()
        elif choice == '5':
            view_appointments()
        elif choice == '6':
            print("Exiting system...")
            break
        else:
            print("Invalid choice! Try again.\n")


# Run program
main()