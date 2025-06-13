import time

class DrugBatch:
    def __init__(self, batch_id, manufacturer):
        self.batch_id = batch_id
        self.manufacturer = manufacturer
        self.manufacture_date = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
        self.current_owner = manufacturer
        self.is_authentic = True
        self.transfer_history = []

    def transfer_drug(self, new_owner):
        if not self.is_authentic:
            raise ValueError("Drug batch is not authentic.")
        self.transfer_history.append({
            "from": self.current_owner,
            "to": new_owner,
            "timestamp": time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
        })
        self.current_owner = new_owner

    def validate_drug(self):
        return self.is_authentic

    def get_transfer_history(self):
        return self.transfer_history

class PharmaSupplyChain:
    def __init__(self):
        self.drug_batches = {}

    def create_drug_batch(self, batch_id, manufacturer):
        if batch_id in self.drug_batches:
            raise ValueError("Batch ID already exists.")
        new_batch = DrugBatch(batch_id, manufacturer)
        self.drug_batches[batch_id] = new_batch
        print(f"New batch created: {batch_id}, Manufacturer: {manufacturer}, Manufacture Date: {new_batch.manufacture_date}")

    def transfer_drug(self, batch_id, new_owner):
        if batch_id not in self.drug_batches:
            raise ValueError("Batch ID does not exist.")
        self.drug_batches[batch_id].transfer_drug(new_owner)
        print(f"Batch {batch_id} transferred to {new_owner}.")

    def validate_drug(self, batch_id):
        if batch_id not in self.drug_batches:
            raise ValueError("Batch ID does not exist.")
        is_authentic = self.drug_batches[batch_id].validate_drug()
        print(f"Batch {batch_id} validation status: {'Authentic' if is_authentic else 'Not Authentic'}")
        return is_authentic

    def get_transfer_history(self, batch_id):
        if batch_id not in self.drug_batches:
            raise ValueError("Batch ID does not exist.")
        history = self.drug_batches[batch_id].get_transfer_history()
        if history:
            print(f"Transfer History for Batch {batch_id}:")
            for record in history:
                print(f"  From: {record['from']}, To: {record['to']}, Date: {record['timestamp']}")
        else:
            print(f"No transfer history for Batch {batch_id}.")

def main():
    pharma_chain = PharmaSupplyChain()

    while True:
        print("\nPharma Supply Chain System")
        print("1. Create Drug Batch")
        print("2. Transfer Drug Batch")
        print("3. Validate Drug Batch")
        print("4. View Transfer History")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            batch_id = input("Enter Batch ID: ")
            manufacturer = input("Enter Manufacturer Name: ")
            try:
                pharma_chain.create_drug_batch(batch_id, manufacturer)
            except ValueError as e:
                print(e)
        
        elif choice == "2":
            batch_id = input("Enter Batch ID: ")
            new_owner = input("Enter New Owner Name: ")
            try:
                pharma_chain.transfer_drug(batch_id, new_owner)
            except ValueError as e:
                print(e)
        
        elif choice == "3":
            batch_id = input("Enter Batch ID: ")
            try:
                pharma_chain.validate_drug(batch_id)
            except ValueError as e:
                print(e)
        
        elif choice == "4":
            batch_id = input("Enter Batch ID: ")
            try:
                pharma_chain.get_transfer_history(batch_id)
            except ValueError as e:
                print(e)
        
        elif choice == "5":
            print("Exiting the system.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
