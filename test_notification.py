from plyer import notification

notification.notify(
    title="✈️ AeroTask Reminder",
    message="This is a test notification!",
    timeout=10
)

print("Notification Sent!")