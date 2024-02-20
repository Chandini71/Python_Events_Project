import json
from datetime import datetime

# Function to save events to a file
def save_events_to_file(events):
    with open('events.json', 'w') as file:
        json.dump(events, file, default=str)

# Function to load events from a file
def load_events_from_file():
    try:
        with open('events.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Load events from file when the program starts
events = load_events_from_file()

def create_event(title, description, start_time, end_time):
    event = {
        'title': title,
        'description': description,
        'start_time': start_time,
        'end_time': end_time
    }
    events.append(event)
    save_events_to_file(events)
    return event

def get_events():
    events_sorted = sorted(events, key=lambda x: datetime.strptime(x['start_time'], "%Y-%m-%d %H:%M"))
    return events_sorted

def update_event(event_id, updated_event):
    events[event_id] = updated_event
    save_events_to_file(events)
    return updated_event

def delete_event(event_id):
    deleted_event = events.pop(event_id)
    save_events_to_file(events)
    return deleted_event

if __name__ == '__main__':
    while True:
        print("\n1. Create Event")
        print("2. View Events")
        print("3. Update Event")
        print("4. Delete Event")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter event title: ")
            description = input("Enter event description: ")
            start_time = input("Enter event start time (YYYY-MM-DD HH:MM): ")
            end_time = input("Enter event end time (YYYY-MM-DD HH:MM): ")

            try:
                start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M")
                end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M")
                created_event = create_event(title, description, start_time.strftime("%Y-%m-%d %H:%M"), end_time.strftime("%Y-%m-%d %H:%M"))
                print("Event created successfully:")
                print(created_event)
            except ValueError:
                print("Invalid date/time format. Please use YYYY-MM-DD HH:MM.")

        elif choice == '2':
            print("All Events:")
            for idx, event in enumerate(get_events()):
                print(f"{idx + 1}. {event}")

        elif choice == '3':
            event_id = int(input("Enter the event ID to update: "))
            updated_title = input("Enter updated event title: ")
            updated_description = input("Enter updated event description: ")
            updated_start_time = input("Enter updated event start time (YYYY-MM-DD HH:MM): ")
            updated_end_time = input("Enter updated event end time (YYYY-MM-DD HH:MM): ")

            try:
                updated_start_time = datetime.strptime(updated_start_time, "%Y-%m-%d %H:%M")
                updated_end_time = datetime.strptime(updated_end_time, "%Y-%m-%d %H:%M")
                updated_event = update_event(event_id - 1, {
                    'title': updated_title,
                    'description': updated_description,
                    'start_time': updated_start_time.strftime("%Y-%m-%d %H:%M"),
                    'end_time': updated_end_time.strftime("%Y-%m-%d %H:%M")
                })
                print("Event updated successfully:")
                print(updated_event)
            except (ValueError, IndexError):
                print("Invalid date/time or event ID.")

        elif choice == '4':
            event_id = int(input("Enter the event ID to delete: "))
            try:
                deleted_event = delete_event(event_id - 1)
                print("Event deleted successfully:")
                print(deleted_event)
            except IndexError:
                print("Invalid event ID.")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
