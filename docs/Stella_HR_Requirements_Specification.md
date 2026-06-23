
MobiPine Limited, 8th Floor,
Greenspot Towers, Eastern Bypass,
P.O Box 15359-0400, Nairobi Kenya
+254790619043 / info@mobipine.com

REQUIREMENTS SPECIFICATION
Stella HR Solutions
HR & Payroll System Implementation Scoping Document

Client
Stella HR Solutions
Client Email
info@stellarhr.co.ke | ronald.azimbu@stellarhr.co.ke 
Client Phone
0745 777 678  |  0742 249 927
Consultant
MobiPine Limited
Prepared By
Patrick N. Maina / Emmanuel Gathu
Document Version
1.0.0
Date
April 2026

















1. Introduction
This document outlines the data and configuration requirements for the implementation of the Odoo HR & Payroll system at Stella HR Solutions. The information gathered will be used to configure the system, set up user access, map HR business processes, and plan for data migration from existing tools.
The implementation will cover employee management, payroll processing, leave management, attendance tracking, recruitment, and document management — all configured to align with Kenyan statutory requirements including PAYE, NSSF, SHIF, and KRA compliance.
These requirements may be refined during the implementation phase based on further stakeholder discussions, system testing, and process clarifications.

2. Scope of Implementation
The implementation covers the following functional areas of the Odoo HR & Payroll system:
Business Setup & Configuration
Employee Management
Payroll & Salary Structure Configuration
Leave (Time Off) Management
Attendance Tracking
Recruitment Module
Documents & e-Signing Module
User Access & Role Management

3. Document Conventions
Throughout this document:
Items marked with (*) are mandatory and must be provided before go-live.
Items marked with (if applicable) are conditional based on business operations.
The 'Purpose' callout boxes explain why each category of information is needed.

4. Business Requirements
4.1 Contractual Documentation
The following contractual documents are required before implementation commences:
Requirement
Details / Action Required
Signed Copy of the Contract *
To be signed by both parties prior to commencement
Signed Copy of the NDA *
To be signed by both parties prior to commencement
Signed Copy of the SLA *
Covers all modules to be deployed under this engagement
Annual Maintenance Contract *
To be signed on or before commencement of the annual support period


4.2 Enterprise Subscription
Requirement
Details / Action Required
Enterprise Subscription Code *
Provided by MobiPine Limited upon contract signing
User Email Addresses *
Full name, email address, department, and designated role for each Odoo user


Purpose: To validate the enterprise licence and set up appropriate system access rights for each user.


4.3 General Company Information
These details will be used to configure the company profile, branding, and organisational structure within Odoo.
Requirement
Details / Action Required
Company / Business Legal Name *
As registered with the relevant authority
KRA PIN *
Required for statutory compliance configuration
Physical & Postal Address *
Full address including building, town, and postal code
Phone Number(s) *
Primary and secondary contact numbers
Email Address *
Official business email address(es)
Website URL
If applicable
Logo & Branding Assets *
High-resolution logo (PNG and JPEG), primary and secondary brand colours
Organisational Chart *
Departments, branches, and reporting lines
User List *
Full name, job title, department, and email for each user to be onboarded
Current HR/Payroll System
Current tools in use — e.g. Excel, Sage HR, other payroll software — including export formats for data migration


Purpose: To establish the business identity, structure, and current digital environment within Odoo — enabling accurate configuration, user role assignment, branding, and planning for data migration.



5. Employee Data Requirements
Accurate and complete employee data is essential for setting up the HR module, payroll processing, and statutory compliance from day one. The following details are required for each employee.
5.1 Personal Information
Requirement
Details / Action Required
Full Name *
As per National ID or passport
ID / Passport Number *
National ID number or passport number
KRA PIN Number *
Required for PAYE tax computation
Date of Birth *
DD/MM/YYYY format
Gender *
Male / Female / Other
Marital Status
Single / Married / Divorced / Widowed
Residential Address *
Physical home address
Phone Number *
Primary contact number
Email Address *
Work or personal email address
Next of Kin — Name *
Full name of emergency contact
Next of Kin — Relationship
Relationship to employee — e.g. Spouse, Parent, Sibling
Next of Kin — Phone *
Emergency contact phone number


5.2 Statutory Registration Numbers
Requirement
Details / Action Required
NSSF Number *
National Social Security Fund membership number
SHIF Number *
Social Health Insurance Fund number (formerly NHIF)
HELB Status
Whether the employee has an active HELB deduction (Yes / No) and monthly deduction amount


5.3 Employment Information
Requirement
Details / Action Required
Employee Number
Internal employee ID / staff number (if applicable)
Job Title *
Official job title as per employment contract
Department *
Department the employee belongs to
Manager / Supervisor *
Direct line manager or supervisor's name
Employment Type *
Full-time / Part-time / Contract / Casual
Employment Start Date *
Date the employee commenced employment — DD/MM/YYYY
Contract End Date
For contract employees — DD/MM/YYYY (if applicable)
Work Location / Branch *
Primary office or branch location
Work Schedule *
Standard working hours — e.g. Mon–Fri, 8 AM–5 PM


5.4 Banking Information (for Salary Payments)
Requirement
Details / Action Required
Bank Name *
Name of the employee's bank — e.g. Equity Bank, KCB
Bank Branch *
Branch where the account is held
Account Name *
Name on the bank account (must match employee name)
Account Number *
Bank account number for salary disbursement
M-Pesa Number
If salary is paid via M-Pesa — provide registered phone number


Purpose: To create accurate employee profiles in Odoo, ensure correct statutory deductions (PAYE, NSSF, SHIF, HELB), and enable automated salary payments to the correct bank accounts.


6. Payroll & Salary Structure Requirements
The following information is required to configure salary structures, payroll rules, and statutory deductions within Odoo Payroll — fully aligned with Kenyan labour and tax laws.

6.1 Salary Components
Requirement
Details / Action Required
Basic Salary *
Monthly gross basic salary per employee or per grade/band
Housing Allowance
Fixed or percentage-based housing allowance (if applicable)
Transport Allowance
Fixed or percentage-based transport allowance (if applicable)
Airtime / Communication Allowance
Monthly airtime or communication stipend (if applicable)
Medical / Health Allowance
Medical cover or health allowance details (if applicable)
Car Allowance
Car allowance amount or car benefit details (if applicable)
Other Allowances
List any other allowances paid — name, amount or basis
Commission / Bonus Structure
How commissions or bonuses are calculated and paid (if applicable)


6.2 Deductions
Requirement
Details / Action Required
PAYE Tax *
Configured automatically per KRA tax bands — confirm if any staff are tax-exempt
NSSF Deduction *
Confirm applicable NSSF tier (Tier I and/or Tier II)
SHIF Deduction *
Confirm SHIF rate — currently 2.75% of gross salary
HELB Deduction
Monthly HELB repayment amount per employee (if applicable)
Loan / Salary Advance
Details of any active employee loans or salary advances outstanding
Other Deductions
Any other company-specific deductions — name, amount or basis


6.3 Payroll Processing Rules
Requirement
Details / Action Required
Payroll Frequency *
Monthly / Bi-monthly / Weekly — confirm processing schedule
Payroll Processing Date *
Day of the month payroll is processed — e.g. 25th of each month
Salary Payment Date *
Day salaries are disbursed to employees — e.g. last working day of the month
Payment Method *
Bank transfer / M-Pesa / Cheque — confirm method per employee group
Salary Structure per Grade
Are different employee grades on different salary structures? (Yes / No)
Overtime Policy
Overtime rate and eligibility — e.g. 1.5x for weekday OT, 2x for weekends


Purpose: To configure Odoo Payroll with the correct salary rules, statutory deductions, and processing schedule — ensuring every payslip is accurate, compliant with KRA, NSSF, and SHIF requirements, and reflects the specific allowances and deductions applicable to each employee.


7. Leave (Time Off) Management Requirements
Requirement
Details / Action Required
Annual Leave *
Number of days per year — e.g. 21 working days per annum
Sick Leave *
Number of days allowed — e.g. 7 days per annum with certificate
Maternity Leave *
Duration — e.g. 3 months as per Employment Act
Paternity Leave *
Duration — e.g. 2 weeks
Unpaid Leave
Policy for unpaid leave (if applicable)
Compassionate Leave
Bereavement / compassionate leave policy (if applicable)
Leave Carry-Over Policy
Can unused leave be carried forward? If yes, how many days and for how long?
Leave Accrual Policy
Does leave accrue monthly, quarterly, or is it granted upfront annually?
Leave Approval Hierarchy *
Who approves leave requests — e.g. Direct Manager → HR Manager
Public Holidays *
Confirm Kenya's public holiday calendar applies and any additional company holidays


Purpose: To configure leave types, allocation rules, approval workflows, and carry-over policies in Odoo — ensuring leave management is automated, fair, and compliant with the Kenya Employment Act.


8. Attendance Requirements
Requirement
Details / Action Required
Working Hours Policy *
Standard daily working hours — e.g. 8 hours/day, Mon–Fri
Work Schedules *
List all work schedule types in use — e.g. Standard (8 AM–5 PM), Shift A (6 AM–2 PM)
Attendance Tracking Method *
Manual (self-entry), biometric device, QR code, or mobile check-in
Biometric / Device Integration
If a biometric attendance device is in use — provide make, model, and connectivity type (if applicable)
Overtime Policy
How overtime is tracked — automatic from attendance or manually entered
Late Clock-In Policy
Is there a grace period for late arrivals? What are the deduction rules?
Remote / Work-From-Home Policy
How attendance is recorded for remote employees (if applicable)


Purpose: To configure accurate work schedules, attendance tracking, and overtime rules — ensuring attendance data feeds correctly into payroll calculations.



9. Recruitment Module Requirements
Requirement
Details / Action Required
Recruitment Workflow *
Steps in your hiring process — e.g. Job Posted → Applications → Shortlisting → Interview → Offer → Hired
Job Positions List
List of standard job positions / roles in the organisation
Interview Stages
Names of interview stages — e.g. HR Screen, Technical Interview, Final Interview
Approval Hierarchy
Who approves job postings and hiring decisions
Job Board Integration
Should vacancies be published to external job boards via Odoo? (Yes / No)
AI Screening
Use Odoo's AI-assisted CV screening for shortlisting? (Yes / No)
Offer Letter Template
Provide a sample offer letter template for configuration in Odoo


Purpose: To configure the recruitment pipeline, automate the hiring workflow, and enable job postings — reducing manual effort and ensuring a structured, consistent hiring process.


10. Documents & e-Signing Requirements
Requirement
Details / Action Required
Document Types to Manage *
List of HR documents stored in Odoo — e.g. Employment Contracts, NDAs, Appraisal Forms, Policy Documents
e-Signing Requirements
Which documents require electronic signatures? (Yes / No per document type)
Document Retention Policy
How long documents should be retained in the system
Access Permissions per Doc Type
Who should be able to view / edit / sign each document type


Purpose: To configure document storage, e-signature workflows, and access controls — ensuring HR documents are securely managed, easily retrievable, and legally signed within Odoo.


11. Opening / Migration Data Requirements
If Stella HR Solutions is migrating from an existing HR or payroll system, the following historical data is required to ensure continuity from go-live:
Requirement
Details / Action Required
Current Employee Salary Details *
Gross salary, net salary, and all components per employee as at migration date
Outstanding Loans & Advances
Employee name, loan amount, monthly deduction, and outstanding balance
Leave Balances *
Current accrued and remaining leave balance per employee per leave type
Previous Payroll History
Past payroll records — recommended for at least 3 months prior to go-live (optional but recommended)
P9 / Tax Certificates
Previous year P9 forms for each employee — for tax continuity
NSSF / SHIF Remittance History
Recent remittance records for statutory compliance reconciliation


Purpose: To ensure a seamless transition from the existing system — preserving leave balances, loan deductions, and payroll continuity so employees are not adversely affected on go-live.


12. Email & Communication Requirements
Requirement
Details / Action Required
SMTP Gateway *
Email server credentials (host, port, username, password) for Odoo to send emails
Outgoing Email Address *
The official email address from which system emails are sent
Notification Types
Which automated emails are required — e.g. payslip distribution, leave approval, leave rejection, attendance alerts


Purpose: To enable automated HR communications — including payslip emails, leave notifications, and document signing requests — directly from Odoo.


13. Server & Hosting Requirements
Requirement
Details / Action Required
Virtual Private Server (VPS) *
Minimum spec: 8 GB RAM, 4-core CPU, 100 GB SSD, unlimited bandwidth, <150 ms latency. UK location preferred.


Purpose: A dedicated VPS ensures the Odoo HR system is performant, secure, and fully owned by Stella HR Solutions — with no data shared with third-party cloud providers.



14. Additional Notes
The requirements outlined in this document represent the initial scope as agreed upon at the time of preparation. They are subject to revision as the implementation progresses, based on:
Further discussions and clarifications with Stella HR Solutions stakeholders
Outcomes of system testing and user acceptance testing (UAT)
Changes to business processes or Kenyan statutory requirements

Any amendments to the scope will be documented and agreed upon in writing by both parties before implementation proceeds.

15. Document Sign-Off
By signing below, both parties confirm that the requirements outlined in this document have been reviewed, provided, and agreed upon as the basis for the implementation.


On Behalf of Stella HR Solutions
On Behalf of MobiPine Limited
Name: ________________________
Name: __Patrick N. Maina_________
Title: __________________________
Title: ____Team Lead_____________________
Signature: ______________________
Signature: _____________________
Date: __________________________
Date: _________7th April 2026_________________


