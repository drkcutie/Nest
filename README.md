
# Link Sync

The app is to be developed to address these issues by providing an automated solution for categorizing, and managing events such as meetings etc, ultimately enhancing productivity and reducing the burden of manual calendar management.




## FUNCTIONAL REQUIREMENTS

Authentication / Login Register:
The system must allow users to register, log in, and authenticate securely. Specific requirements include:

    Password Complexity: Enforce strong password rules, including a mix of uppercase, lowercase, numbers, and special characters.
    Error Handling: Provide appropriate error messages for invalid login attempts, registration failures, and password mismatches.
    Session Management: Ensure secure session handling using token-based authentication, with features like session expiration and logout options.
    Database Support: Implement authentication using relational (MySQL, PostgreSQL) or non-relational (MongoDB) databases, with Django handling server-side logic.

Link Organizer:
Users must be able to manage their external links, such as scheduled meetings. Features include:

    Add Links: Allow users to add new links with details like the name, URL, and description.
    Edit Links: Provide functionality for users to modify existing link details.
    Delete Links: Users can delete links they no longer need.
    View Links: Display a list of saved links with sorting and filtering options.
    Categorization: Enable users to organize links by predefined or custom categories for easier management.

Categorization:
Users must be able to categorize their data or content using the following features:

    Predefined and Custom Categories: Users can choose from predefined categories or create their own.
    Tagging and Filtering: Users can assign tags to items and filter them by category, tag, or other attributes.

Parsing Events:
Automatically parse scheduled links into organized, easy-to-view events, making it easier for users to manage tasks and deadlines.
2.2 Optional Features

Automated Schedule Gap Identification and Task Assignment:
The system should automatically identify gaps in users' schedules and assign tasks to fill those gaps. Features include:

    Gap Detection: Analyze work, school, or event schedules to identify free time within a 24-hour period.
    Task Assignment: Automatically suggest or assign tasks to available time slots.
    Recursive Scheduling: Apply gap detection and task assignment for a week or month.

Notifications / Reminders:
Allow users to set notifications or reminders for upcoming tasks, events, or schedule changes.

Time Estimation for Tasks:
Let users estimate the duration of tasks, with the scheduler adjusting available time slots based on these estimates.

Priority-Based Scheduling:
Enable users to assign priorities to tasks or events, ensuring high-priority items are scheduled first.

Recurring Tasks and Events:
Support recurring scheduling for tasks or events (daily, weekly, or monthly) to automate repetitive tasks.
## GANTT CHART

https://docs.google.com/spreadsheets/d/1DDcX2QFPq0fwrB0ADPTwiGHagGypi_Tlt7m-oKX9lXc/edit?usp=sharing
## ERD

https://lucid.app/lucidchart/5ffb15d8-721d-4da4-8d53-179f8a59e261/edit?viewport_loc=333%2C-1641%2C2647%2C1520%2C0_0&invitationId=inv_51865532-232e-47c5-9b57-4f572c34bb95
## UI/ UX DESIGN

https://www.figma.com/design/J7ee0FpgF2qD2yIp5FqTzj/Information-Management-2-(UI-%2F-UX-)?node-id=0-1&t=8sXbcibwYCDYRl6m-1