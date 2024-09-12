service_tickets = {
    1: {"Customer Name": "John Doe", "Issue": "Internet not working", "Status": "Open"},
    2: {"Customer Name": "Jane Doe", "Issue": "Billing issue", "Status": "Closed"},
    3: {"Customer Name": "Magic Johnson", "Issue": "Slow internet speed", "Status": "Open"}
}
def open_ticket(ticket_id, customer_name, issue):
    service_tickets[ticket_id] = {
        "Customer Name": customer_name,
        "Issue": issue,
        "Status": "Open"
    }
    print(f"Ticket {ticket_id} opened for {customer_name} with issue: {issue}")

# Function to update the status of an existing ticket
def update_ticket_status(ticket_id, new_status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = new_status
        print(f"Ticket {ticket_id} status updated to {new_status}")
    else:
        print(f"Ticket ID {ticket_id} not found.")

# Function to display all tickets (Open/Closed)
def display_tickets(status=None):
    if status:
        print(f"Displaying {status} tickets:")
        for ticket_id, ticket_info in service_tickets.items():
            if ticket_info["Status"].lower() == status.lower():
                print(f"Ticket ID: {ticket_id}, Customer: {ticket_info['Customer Name']}, Issue: {ticket_info['Issue']}, Status: {ticket_info['Status']}")
    else:
        print("Displaying all tickets:")
        for ticket_id, ticket_info in service_tickets.items():
            print(f"Ticket ID: {ticket_id}, Customer: {ticket_info['Customer Name']}, Issue: {ticket_info['Issue']}, Status: {ticket_info['Status']}")

# Sample
print("Initializing system with sample tickets...\n")

# Open a new ticket
open_ticket(4, "Sara Connor", "No dial tone on phone")

# Update ticket status
update_ticket_status(1, "Closed")

# Display all tickets
display_tickets()

print("\n")

# Display only open tickets
display_tickets("Open")