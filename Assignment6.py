class SymptomChecker:
    def __init__(self):
        self.symptoms = {
            'fever': {
                'cough': 'common cold',
                'rash': 'measles',
                'headache': 'flu'
            },
            'headache': {
                'nausea': 'migraine',
                'stiff neck': 'meningitis',
                'earache': 'sinusitis'
            },
            'cough': {
                'shortness of breath': 'pneumonia',
                'sore throat': 'flu',
                'runny nose': 'common cold'
            }
            # Add more symptoms and conditions as needed
        }

    def diagnose(self):
        symptoms = []
        print("Please enter your symptoms (type 'done' when finished):")
        while True:
            symptom = input("- ")
            if symptom == 'done':
                break
            symptoms.append(symptom)

        possible_conditions = set()
        for symptom in symptoms:
            if symptom in self.symptoms:
                conditions = self.symptoms[symptom]
                possible_conditions.update(conditions.values())

        if possible_conditions:
            print("Possible conditions:")
            for condition in possible_conditions:
                print("- " + condition)
        else:
            print("No matching conditions found.")

# Example usage
checker = SymptomChecker()
checker.diagnose()
