
# ==========================================
# IT AUTOMATION INCIDENT TICKET MANAGER
# Laboratory Exercise 1
# Data Structure: Singly Linked List
# ==========================================


# Node class
class Ticket:
    def __init__(self, incident_id, bot, description):
        self.incident_id = incident_id
        self.bot = bot
        self.description = description
        self.next = None


# Incident Ticket Manager
class IncidentTicketManager:

    def __init__(self):
        self.head = None

    # ==========================================
    # 1. ADD INCIDENT TICKET
    # ==========================================
    def add_ticket(self, incident_id, bot, description):

        new_ticket = Ticket(incident_id, bot, description)

        if self.head is None:
            self.head = new_ticket

        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_ticket

        print("\nSUCCESS: Incident ticket added.")

    # ==========================================
    # 2. DISPLAY ALL ACTIVE TICKETS
    # ==========================================
    def display_tickets(self):

        if self.head is None:
            print("\nNo active incident tickets.")
            return

        print("\n===== ACTIVE INCIDENT TICKETS =====")
        print("=" * 80)

        print(
            f"{'Incident ID':<15}"
            f"{'Bot':<20}"
            f"{'Short Description'}"
        )

        print("-" * 80)

        current = self.head

        while current is not None:

            print(
                f"{current.incident_id:<15}"
                f"{current.bot:<20}"
                f"{current.description}"
            )

            current = current.next

        print("=" * 80)

    # ==========================================
    # 3. SEARCH INCIDENT TICKET
    # ==========================================
    def search_ticket(self, incident_id):

        current = self.head

        while current is not None:

            if current.incident_id.lower() == incident_id.lower():

                print("\nSUCCESS: Incident ticket found.")
                print("-" * 40)
                print(f"Incident ID       : {current.incident_id}")
                print(f"Bot               : {current.bot}")
                print(f"Short Description : {current.description}")
                print("-" * 40)

                return

            current = current.next

        print("\nERROR: Incident ticket not found.")

    # ==========================================
    # 4. REMOVE RESOLVED TICKET
    # ==========================================
    def remove_ticket(self, incident_id):

        if self.head is None:
            print("\nNo active incident tickets.")
            return

        # Remove first ticket
        if self.head.incident_id.lower() == incident_id.lower():

            self.head = self.head.next

            print("\nSUCCESS: Incident ticket removed.")
            return

        current = self.head

        while current.next is not None:

            if current.next.incident_id.lower() == incident_id.lower():

                current.next = current.next.next

                print("\nSUCCESS: Incident ticket removed.")
                return

            current = current.next

        print("\nERROR: Incident ticket not found.")

    # ==========================================
    # 5. COUNT ACTIVE TICKETS
    # ==========================================
    def count_tickets(self):

        count = 0
        current = self.head

        while current is not None:

            count += 1
            current = current.next

        print(f"\nTotal Active Tickets: {count}")


# ==========================================
# CREATE INCIDENT TICKET MANAGER
# ==========================================

manager = IncidentTicketManager()


# ==========================================
# 10 SAMPLE INCIDENT TICKETS
# ==========================================

manager.add_ticket(
    "INC1392939",
    "BOT-Inventory",
    "Failed to generate the daily report"
)

manager.add_ticket(
    "INC1392940",
    "BOT-Email",
    "Failed to send the scheduled notification"
)

manager.add_ticket(
    "INC1392941",
    "BOT-DataSync",
    "Encountered an error during data transfer"
)

manager.add_ticket(
    "INC1392942",
    "BOT-Invoice",
    "Failed to process an invoice"
)

manager.add_ticket(
    "INC1392943",
    "BOT-Report",
    "Failed to generate the weekly report"
)

manager.add_ticket(
    "INC1392944",
    "BOT-FileTransfer",
    "Failed to upload the required file"
)

manager.add_ticket(
    "INC1392945",
    "BOT-DataEntry",
    "Encountered an error while entering records"
)

manager.add_ticket(
    "INC1392946",
    "BOT-Backup",
    "Failed to complete the scheduled backup"
)

manager.add_ticket(
    "INC1392947",
    "BOT-Validation",
    "Failed to validate the submitted records"
)

manager.add_ticket(
    "INC1392948",
    "BOT-Notification",
    "Failed to send the system alert"
)


# ==========================================
# MAIN MENU
# ==========================================

while True:

    print("\n======================================")
    print("        INCIDENT TICKET SYSTEM")
    print("======================================")
    print("1. Add Incident Ticket")
    print("2. Display All Active Tickets")
    print("3. Search Incident Ticket")
    print("4. Remove Resolved Ticket")
    print("5. Count Active Tickets")
    print("6. Exit")
    print("======================================")

    choice = input("Enter your choice (1-6): ")

    # ======================================
    # ADD
    # ======================================

    if choice == "1":

        print("\n===== ADD INCIDENT TICKET =====")

        incident_id = input("Enter Incident ID: ")
        bot = input("Enter Bot: ")
        description = input("Enter Short Description: ")

        manager.add_ticket(
            incident_id,
            bot,
            description
        )

    # ======================================
    # DISPLAY
    # ======================================

    elif choice == "2":

        manager.display_tickets()

    # ======================================
    # SEARCH
    # ======================================

    elif choice == "3":

        print("\n===== SEARCH INCIDENT TICKET =====")

        incident_id = input("Enter Incident ID: ")

        manager.search_ticket(incident_id)

    # ======================================
    # REMOVE
    # ======================================

    elif choice == "4":

        print("\n===== REMOVE RESOLVED TICKET =====")

        incident_id = input("Enter Incident ID: ")

        manager.remove_ticket(incident_id)

    # ======================================
    # COUNT
    # ======================================

    elif choice == "5":

        print("\n===== COUNT ACTIVE TICKETS =====")

        manager.count_tickets()

    # ======================================
    # EXIT
    # ======================================

    elif choice == "6":

        print("\nThank you for using the Incident Ticket System!")
        print("Program ended.")

        break

    else:

        print("\nInvalid choice. Please enter 1-6.")
