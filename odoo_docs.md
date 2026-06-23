Documents
=========

**Odoo Documents** allows you to store, view, and manage files within Odoo.

Folders and documents are organized into sections accessible from the tree on the left. The following sections are available:

*   **All**: displays all folders and files the user has access to.
    
*    **Company**: contains folders and files shared across the company. Access is determined by the [access rights](https://www.odoo.com/documentation/19.0/applications/productivity/documents.html#documents-access-rights) defined for the folder and file.
    
*    **My Drive**: the user’s personal workspace for organizing and accessing files and folders they own or have uploaded.
    
*    **Shared with me**: includes files that have been shared with the user but are not part of any parent folder they have access to.
    
*    **Recent**: shows recently modified files the user has permission to view or edit.
    
*    **Trash**: stores [deleted files and folders](https://www.odoo.com/documentation/19.0/applications/productivity/documents.html#documents-deletion-delay).
    

Click a section in the tree to view its contents. Select a folder to open it, [manage it](https://www.odoo.com/documentation/19.0/applications/productivity/documents.html#documents-folders), and access its files.

Click a file to open it and [take available actions](https://www.odoo.com/documentation/19.0/applications/productivity/documents.html#documents-documents). To close the file, press **Esc** or click the  (**close**) icon. You can also drag and drop a file or folder to move it to another folder or section.

 Tip

*   Use the [search bar](https://www.odoo.com/documentation/19.0/applications/essentials/search.html#search-values) to quickly find specific items.
    
*   The [chatter](https://www.odoo.com/documentation/19.0/applications/productivity/discuss/chatter.html) tracks changes to folders and files and allows communication with internal users and external contacts. Open the [Details panel](https://www.odoo.com/documentation/19.0/applications/productivity/documents.html#documents-details-panel) to access it.
    

 See also

[Sign documentation](https://www.odoo.com/documentation/19.0/applications/productivity/sign.html)

Configuration
-------------

### Deletion delay

By default, items moved to the trash remain there for 30 days before being permanently deleted. To adjust this delay, go to **Documents ‣ Configuration ‣ Settings** and edit the **Deletion delay (days)** field.

### File centralization

File centralization allows for automatically organizing all files associated with a specific app into dedicated folders. It is enabled by default for each app upon installation. To disable file centralization, modify the default folder, or configure the tags to be added to the app-specific files, go to **Documents ‣ Configuration ‣ Settings**, and edit the relevant setting under the **File Centralization** section.

 Tip

*   File centralization cannot be disabled for **Accounting** documents. A sub-folder is automatically created for each journal type (e.g., Sales, Purchase, Bank, etc.), and the journal name is added as a tag on each document. Click **Journals** to edit the list of journals to synchronize and define their corresponding folders and tags.
    
*   For **Human Resources** files, a sub-folder is automatically created for each employee, and specific tags are added to the files based on the document type (e.g., **Contracts**, **Payslips**, etc.). You can also create additional **Employee Subfolders** automatically by entering the desired folder names, separated by commas.
    

 Note

*   Changing the folder or tags only affects new files; existing files remain unchanged.
    
*   When file centralization is enabled for an app, deleting a record in that app moves its attachments to the trash in the Documents app.
    

Folders
-------

You can organize files in folders available in the  **Company** or  **My Drive** sections.

To create a folder, select the desired section in the tree, click **New**, and select **Folder**. In the pop-up, enter the folder’s **Name** and click **Save**. To create a sub-folder, select the parent folder first, then follow the same steps.

 Note

Some folders and sub-folders are created automatically based on the [file centralization settings](https://www.odoo.com/documentation/19.0/applications/productivity/documents.html#documents-file-centralization).

To manage a folder or sub-folder, select it and click the  (**Actions**) icon above the tree. The following options are available in the menu:

*    **Download**: Download the folder as a .zip file, including its files and sub-folders.
    
*    **Rename**: Modify the folder’s name.
    
*    **Share**: [Share the folder and manage its access rights](https://www.odoo.com/documentation/19.0/applications/productivity/documents.html#documents-access-rights).
    
*    **Add star**: Mark a folder as a favorite for quicker access. This setting is user-specific and does not affect other users’ workspaces. You can then use the [Starred filter](https://www.odoo.com/documentation/19.0/applications/essentials/search.html#search-favorites) to navigate to your favorite folders quickly.
    
*    **Info & Tags**: View the folder’s [details](https://www.odoo.com/documentation/19.0/applications/productivity/documents.html#documents-details-panel) and chatter.
    
*    **Move to trash**: Move the folder and its content to the [trash](https://www.odoo.com/documentation/19.0/applications/productivity/documents.html#documents-deletion-delay).
    
*    **Actions on Select**: Define the server actions that are available (as buttons) for the files in the folder. Click an action to add or remove it. Click **Add Custom Action** to [create a new one](https://www.odoo.com/documentation/19.0/developer/reference/backend/actions.html#reference-actions-server).
    
*    ImportantSetting up automation rules requires activating [Studio](https://www.odoo.com/documentation/19.0/applications/studio.html), which may impact your [pricing plan](https://www.odoo.com/pricing).
    
*   **AI Auto-sort**: Use Odoo AI to automatically organize the files in the folder and trigger actions based on the provided AI prompt. Add the corresponding actions for your prompt in the lower section of the popup. This option requires the **Odoo AI** app to be installed.
    

 Tip

Switch to the list view to:

*   manage multiple folders at once.
    
*    **Export** or  **Insert in spreadsheet** one or multiple folders.
    
*   quickly execute actions such as **Share**, **Download**, **Rename**, etc. Hover over a folder line and click the corresponding icon at the end of the line to perform the desired action.
    

Files
-----

To upload a file, select the desired folder in the tree, click **New**, and select **Upload**.

 Tip

*   On Odoo Online databases, each uploaded file must not exceed 64MB.
    
*   You can also drag and drop a file from your computer to the desired folder within the Documents app.
    

### URL links

To add a link to a URL (e.g., a video) and make it accessible from a folder, click **New** and select **Link**. Enter the **URL**, add a **Name**, and select the appropriate **Folder**.

### Spreadsheets

To create a spreadsheet, click **New** and select **Spreadsheet**.

 See also

[Spreadsheet documentation](https://www.odoo.com/documentation/19.0/applications/productivity/spreadsheet.html)

### Managing files

Several buttons are available in the top bar when opening a file:

*   the  **Actions** menu, which includes the options described below
    
*   **Share**: to [share the file and manage its access rights](https://www.odoo.com/documentation/19.0/applications/productivity/documents.html#documents-access-rights)
    
*   **Download**
    
*   any [buttons defined for the folder](https://www.odoo.com/documentation/19.0/applications/productivity/documents.html#documents-folders)
    

The following options are available in the  **Actions** menu:

*    **Duplicate**: Create a copy of the file. In the popup, select or create the destination folder, then click **Duplicate in** _destination folder’s name_.
    
*    **Move to Trash**: Move the file to the [trash](https://www.odoo.com/documentation/19.0/applications/productivity/documents.html#documents-deletion-delay).
    
*    **Rename**
    
*    **Info & tags**: View the file’s [details](https://www.odoo.com/documentation/19.0/applications/productivity/documents.html#documents-details-panel) and chatter.
    
*    **Move**: Move the file to another folder. In the popup, select or create the destination folder, then click **Move to** _destination folder’s name_.
    
*    **Create shortcut**: A shortcut is a pointer to a file, allowing access from multiple folders without duplicating the file. In the popup, select or create the destination folder, then click **Create a shortcut in** _destination folder’s name_.
    
*    **Manage versions**: View all versions of the file in upload order, download a specific version, or upload a new one as needed.
    
*    **Lock**: Protect the file from any modifications.
    
*    **Copy Links**: Copy the file’s URL for sharing. Access is controlled based on the file’s [access rights](https://www.odoo.com/documentation/19.0/applications/productivity/documents.html#documents-access-rights).
    
*    **Split PDF**: [Split a PDF file](https://www.odoo.com/documentation/19.0/applications/productivity/documents.html#documents-pdfs).
    

 Tip

*   You can use folder-specific [email aliases](https://www.odoo.com/documentation/19.0/applications/productivity/documents.html#documents-email-aliases) to automatically save files sent to the alias into the corresponding folder.
    
*   Switch to the list view to:
    
    *   manage multiple files at once.
        
    *    **Export** or  **Insert in spreadsheet** one or multiple files.
        
    *   quickly perform actions such as **Share**, **Download**, **Rename**, etc. Hover over a file line and click the corresponding icon at the end of the line to perform the desired action.
        

### Splitting and merging PDFs

To divide a PDF into individual or groups of pages, open the PDF, click the  **Actions** button, and select  **Split PDF**. Click the  (**scissors**) icon between pages to remove a split if needed, then click **Split** to confirm.

To merge PDF files, follow these steps:

1.  Navigate to the folder containing the files you want to merge.
    
2.  Hold down **Ctrl** and click the relevant files.
    
3.  Click the  **Actions** button and select  **Merge PDFs**.
    
4.  If needed, click **Add file** to browse and select a PDF file from your computer.
    
5.  Click the  (**scissors**) icon between the files.
    
6.  Click **Split** to merge them.
    

 Note

The original PDFs are replaced by the merged version.

 Tip

*   Press **Shift + S** to add or remove all splits between pages.
    
*   To delete a specific page, select the page, then click **Delete**.
    

### Requesting files

Request files from users as a reminder for them to upload specific files. To do so, follow these steps:

1.  Click **New** and select **Request**.
    
2.  Enter a **Document Name** and select the person you’re requesting it from in the **Request To** field.
    
3.  If needed, set a **Due Date In**, edit the **Folder** where the file should be added, add **Tags**, and write a **Message**.
    
4.  Click **Request**.
    

A placeholder for the missing file is created in the selected folder. Once the file is available, click the placeholder to upload it.

 Tip

You can also request a document from the [list of scheduled activities](https://www.odoo.com/documentation/19.0/applications/essentials/activities.html#activities-all).

To see the list of all requested files, switch to the Activity view of the Documents app and go to the **Requested Document** column. Click a requested file’s date to view its details. You can then:

*   Upload a file using the  (**upload**) button;
    
*   Edit the activity using the  (**edit**) button;
    
*   Cancel the activity using the  (**cancel**) button;
    
*   Send a reminder email. Click **Preview** to preview the content of the reminder email if needed, then **Send Now**.
    

To send a reminder email for all requested files, click the  (**ellipsis**) icon in the **Requested Document** column and select **Document Request: Reminder**.

Details panel
-------------

To view a folder’s or file’s information and tags, select the folder or file, then click the  icon (for folders) or  **Actions** button (for files) and select  **Info & Tags**.

 Tip

Alternatively, for folders, you can also click the  (**Info & Tags**) button in the upper-right corner next to the view icons.

The details panel allows the following:

*   Change the file’s folder or the folder’s name.
    
*   View the file’s or folder’s size and the folder’s item count.
    
*   Change the file’s or folder’s owner and contact. By default, the person who creates a file or folder is set as its owner and granted full access rights to it. To change it, select the required user from the dropdown list. The contact is a person who only has **Viewer** [access rights](https://www.odoo.com/documentation/19.0/applications/productivity/documents.html#documents-access-rights) to the file or folder, e.g., an existing supplier in the database.
    
*   Access the [chatter](https://www.odoo.com/documentation/19.0/applications/essentials/activities.html).
    

To close the details panel, click the  (**remove**) button in the upper-right corner.

>  Note
> 
> To view a file from their user profile, a user must be set as the contact and have at least **Viewer** [access](https://www.odoo.com/documentation/19.0/applications/productivity/documents.html#documents-access-rights).

### Email aliases

You can use an email alias to automatically save files sent to the email alias into a specific folder. To set up an email alias for a folder, follow these steps:

1.  Make sure a [custom alias domain](https://www.odoo.com/documentation/19.0/applications/general/email_communication/email_servers_inbound.html#email-inbound-custom-domain) is configured in the **General Settings**.
    
2.  Select the folder where files should be saved.
    
3.  Click the  (**Info & Tags**) in the upper-right corner next to the view icons.
    
4.  In the details panel, enter the desired email alias.
    
5.  Optionally, specify an **Activity type** and assignee to create an [activity](https://www.odoo.com/documentation/19.0/applications/essentials/activities.html) when a file is received via the alias.
    
6.  Optionally, select the [Tags](https://www.odoo.com/documentation/19.0/applications/productivity/documents.html#documents-tags) to automatically apply to the files created through the alias.
    

 Note

Emails sent to the alias without attachments are converted into files, using the email subject as the file name.

 See also

[Manage inbound messages](https://www.odoo.com/documentation/19.0/applications/general/email_communication/email_servers_inbound.html)

### Tags

Tags help organize and categorize files, making it easier to search and filter them. To configure tags for files, go to **Documents ‣ Configuration ‣ Tags**. Click **New** to create a new tag. Enter the **Tag Name**, select a **Color**, and optionally add a **Tooltip** that appears when hovering over the tag.

To add tags to a file, open the file, click the  **Actions**, select  **Info & Tags**, and then, in the details panel, select a tag from the **Tags** dropdown menu (identifiable by its placeholder **Add tags**).

 Note

[Alias tags](https://www.odoo.com/documentation/19.0/applications/productivity/documents.html#documents-email-aliases) can also be used to automatically apply tags to files created through the alias.

### Linked records

To link the file to a specific record, select the appropriate model from the **Linked to** dropdown menu (identifiable by its placeholder **No linked model**), then select the desired record.

 Note

If [file centralization](https://www.odoo.com/documentation/19.0/applications/productivity/documents.html#documents-file-centralization) is enabled for a specific app, adding a file to the Documents app by uploading an attachment automatically adds the corresponding record in the **Linked to field** of the file.

Sharing and access rights
-------------------------

 Note

You can only share folders and files and edit their access rights if you have editing rights.

Access rights can be set on:

*   folders: Select the folder, click the  (**gear**) icon, and select **Share**.
    
*   files: Open the file and click **Share** in the top bar.
    

 Tip

Switch to the list view to share or manage the access rights of multiple filers or folders at once.

To grant access to specific users or contacts, follow these steps:

1.   Note**Access through link** must be enabled first before granting access to external contacts.
    
2.  Set the **Role** field to **Viewer** or **Editor**.
    
3.  If desired, toggle the **Notify** switch off to avoid sending a notification email.
    
4.  Click **Share** to grant access (with or without a notification) or **Copy Links** to copy the sharing link to the clipboard.
    

 Tip

To remove a permission or set an expiration date for it, hover the mouse over the relevant contact and click the  (**remove**) or  (**calendar**) button, respectively.

To configure **General access** for **Internal users** or **Access through link**, select **Viewer**, **Editor**, or **None** (to completely restrict access). For **Access through link**, you can also specify whether the folder or file should be **Discoverable** (i.e., accessible through browsing). Click **Save** to apply the changes, then **Copy Links** to copy the sharing link to the clipboard.

 Note

*   Each folder and file URL includes the access rights assigned to it. When you share a link to a folder, recipients are directed to a dedicated portal where they can view the files in that folder, excluding any with restricted access.
    
*   [Portal users](https://www.odoo.com/documentation/19.0/applications/general/users/user_portals.html) can access folders and files they have permission to view or edit through the customer portal by clicking the **Documents** card.
    

Managing files across apps
--------------------------

You can save files to or attach existing files in the Documents app from any record.

*   To save an attachment to the Documents app, hover over an attachment in the record’s chatter and click the  (**Add to Documents**) icon.
    
*   To attach a file to a record from the record’s chatter, click the **Add from Documents** icon, select the desired file, and click **Add from Documents** to add the raw file, or **Paste Link(s)** to insert a link to the file (and preserve the document’s [access rights](https://www.odoo.com/documentation/19.0/applications/productivity/documents.html#documents-access-rights)).
    
*   To insert a file from Documents into the [Odoo rich-text editor](https://www.odoo.com/documentation/19.0/applications/essentials/html_editor.html), type /file, then select the desired file, and click **Add from Documents** to add the raw file, or **Paste Link(s)** to insert a link to the file (and preserve the document’s [access rights](https://www.odoo.com/documentation/19.0/applications/productivity/documents.html#documents-access-rights)).
    

File digitization with AI
-------------------------

Files available in the Finance folder can be digitized. Select the file, click **Create Vendor Bill**, **Create Customer Invoice**, or **Create Customer Credit Note**, then click **Send for Digitization**.

 See also

[AI-powered document digitization](https://www.odoo.com/documentation/19.0/applications/finance/accounting/vendor_bills/invoice_digitization.html)

[Edit on GitHub](https://github.com/odoo/documentation/edit/19.0/content/applications/productivity/documents.rst)

##### On this page

*   [Configuration](https://www.odoo.com/documentation/19.0/applications/productivity/documents.html#configuration)
    
*   [Folders](https://www.odoo.com/documentation/19.0/applications/productivity/documents.html#folders)
    
*   [Files](https://www.odoo.com/documentation/19.0/applications/productivity/documents.html#files)
    
*   [Details panel](https://www.odoo.com/documentation/19.0/applications/productivity/documents.html#details-panel)
    
*   [Sharing and access rights](https://www.odoo.com/documentation/19.0/applications/productivity/documents.html#sharing-and-access-rights)
    
*   [Managing files across apps](https://www.odoo.com/documentation/19.0/applications/productivity/documents.html#managing-files-across-apps)
    
*   [File digitization with AI](https://www.odoo.com/documentation/19.0/applications/productivity/documents.html#file-digitization-with-ai)
    

#### Get Help



Recruitment
===========

Odoo keeps all job applicants organized with a preconfigured series of steps and stages that each applicant goes through. Each stage has a specific steps that should be performed. These range from scheduling a phone call, conducting an interview, or sending a job offer, for example. This process is referred to as the _applicant flow._

When an applicant applies for a job position, an _applicant card_ is automatically created in Odoo’s **Recruitment** app for that specific job position. As the applicant progresses through the recruitment pipeline, the recruitment team moves their card from one stage to the next.

[Stages can be configured](https://www.odoo.com/documentation/19.0/applications/hr/recruitment.html#recruitment-modify-stages) so that an email is automatically sent out using a set, preconfigured template as soon as an applicant’s card enters a stage. These automated emails are defined on each stage in the applicant flow.

The flow described in this document is Odoo’s default configuration, but it can be customized to suit any recruitment process.

 Note

Stages apply to all job positions unless [marked as job-specific](https://www.odoo.com/documentation/19.0/applications/hr/recruitment.html#recruitment-customize-stages) Changes to stages (e.g., additions, deletions) affect all positions unless explicitly scoped.

Settings
--------

Before creating a job position in Odoo, configure the necessary settings for the **Recruitment** app. To view and edit the settings, navigate to **Recruitment app ‣ Configuration ‣ Settings**. After any changes are made, click the **Save** button in the top-left corner to save all the changes.

### Process

The **Process** section of the settings page specifies what the database can and cannot do during the recruitment process.

#### Send interview survey

Odoo is capable of having a survey sent to an applicant to gather more information about them. Surveys can be thought of as exams, or questionnaires, and can be customized in various ways to provide the recruitment team with valuable insights into the applicant

Enable the **Send Interview Survey** option to send surveys to applicants. Once enabled, an  **Interview Survey** internal link appears. Click the  **Interview Survey** link to navigate to a list of all created surveys.

This list includes all surveys that were created in the database, not only surveys used in the **Recruitment** app. If no surveys have been created, the surveys list displays a **No Survey Found** message, and presents options to create a survey from several preconfigured survey templates.

 See also

[create/edit surveys](https://www.odoo.com/documentation/19.0/applications/marketing/surveys/create.html)

 Note

Enabling the **Send Interview Survey** option will install the **Surveys** application once the settings are saved, if not already installed.

#### Salary package configurator

When sending an offer to an applicant, an expiration date can be set on the offer. Enter the number of days an offer is valid for in the **days** field. After the set amount of days has passed, if the applicant has not accepted the offer, the offer is no longer available.

#### Résumé display

When applicants submit an application, one of the default required fields is a résumé, or CV. All résumés are stored in the **Documents** application, and are accessible on the applicant’s card.

A résumé has the option to appear on the applicant’s form, which can be viewed by clicking on the applicant’s card. The résumé appears on the right-side of the screen. If this is not enabled, the résumé is accessed via a link in the chatter, where it needs to be clicked to expand and view it, or downloaded.

Enable the **Résumé Display** option to show the résumé on the applicant’s card by default, and in addition to the document link. When enabled, the résumé appears on the right side of the applicant’s card.

 Note

For the résumé to appear on the right-side, the browser window must be in full-screen mode (where the browser spans the entire screen).

If the browser window is set to a size smaller than the entire width of the screen (not full-screen), then the résumé does not appear on the right-side. Instead, the résumé appears in the **Files** section of the chatter, below the applicant’s card.

### In-App Purchases

The **In-App Purchases** section of the **Settings** menu deals with items that required credits to use, such as SMS text messages, and digitizing résumés.

 See also

[SMS pricing and FAQs](https://www.odoo.com/documentation/19.0/applications/marketing/sms_marketing/pricing_and_faq.html)

#### Send SMS

It is possible to send text messages to applicants directly through the **Recruitment** app. This feature requires credits to use. Click the  **Manage Service & Buy Credits** internal link, and follow the steps to [purchase credits](https://www.odoo.com/documentation/19.0/applications/marketing/sms_marketing/pricing_and_faq.html).

#### Résumé digitization (OCR)

When an application is submitted using any of the available methods, such as an online application submission, emailing a resume to the job position alias, or creating an applicant record directly from the database, it is possible to have Odoo extract the applicant’s name, phone number, and email address from the résumé and populate the applicant’s form. To do so, enable the **Résumé Digitization (OCR)** option.

When enabled, additional options appear. Click on the corresponding radio button to select one of the following options:

*   **Do not digitize**: this option turns off résumé digitization.
    
*   **Digitize on demand only**: this option only digitizes resumes when requested. A **Digitize document** buttons appears on applicant cards. When clicked, the résumé is scanned and the applicant’s card is updated.
    
*   **Digitize automatically**: this option automatically digitizes all résumés when they are submitted.
    

Beneath these options are two additional links. Click the  **Manage Service & Buy Credits** internal link to purchase credits for résumé digitization. Click the  **View My Services** internal link to view a list of all current services, and their remaining credit balances.

For more information on document digitization and IAP’s, refer to the [In-app purchase (IAP)](https://www.odoo.com/documentation/19.0/applications/essentials/in_app_purchase.html) documentation.

 Note

The **Do not digitize** option may appear redundant but serves a distinct purpose. Disabling the **Résumé Digitization (OCR)** option uninstalls the module, while **Do not digitize** keeps the module installed but inactive—allowing the user to re-enable digitization later without reinstalling the module.

Kanban view
-----------

To access the Kanban view for a job position, navigate to the main **Recruitment** app dashboard, which is the default view when opening the application. All job positions appear on the main dashboard. Click the **(#) New Applications** smart button on a job position card to navigate to the Kanban view for all the applicants for that particular job position.

Inside the job application, the Kanban stages appear, with all the applicants populated in their respective columns, indicating what stage they are currently in. In Odoo, six default stages are configured:

*   [New](https://www.odoo.com/documentation/19.0/applications/hr/recruitment/recruitment-flow.html#recruitment-new)
    
*   [Initial Qualification](https://www.odoo.com/documentation/19.0/applications/hr/recruitment/recruitment-flow.html#recruitment-initial-qualification)
    
*   [First Interview](https://www.odoo.com/documentation/19.0/applications/hr/recruitment/recruitment-flow.html#recruitment-first-interview)
    
*   [Second Interview](https://www.odoo.com/documentation/19.0/applications/hr/recruitment/recruitment-flow.html#recruitment-second-interview)
    
*   [Contract Proposal](https://www.odoo.com/documentation/19.0/applications/hr/recruitment/offer_job_positions.html)
    
*   [Contract Signed](https://www.odoo.com/documentation/19.0/applications/hr/recruitment/offer_job_positions.html#recruitment-offer-job-positions-contract-signed)
    

The last column, **Contract Signed**, is folded by default. Folded columns appear gray, and the applicants in it are hidden from view. To expand the folded stage and view the applicant cards for that column, click anywhere on the thin gray column that says the stage name and the column expands, revealing the applicants.

Each stage has a color-coded bar beneath the stage name, providing status information for the applicant’s in that specific stage. The status colors are:

*   **Green**: the applicant is ready to move to the next stage.
    
*   **Red**: the applicant is blocked from moving to the next stage.
    
*   **Gray**: the applicant is still in progress in the current stage and is neither ready nor blocked from the next stage.
    

The status for each card is set manually. To set the status, click on the small circle in the lower-left of the applicant card. A status pop-up window appears. Click on the desired status for the applicant. The status dot on the applicant card as well as the status bar updates.

 Tip

The names for the three status colors (In Progress, Ready for Next Stage, and Blocked) [can be modified](https://www.odoo.com/documentation/19.0/applications/hr/recruitment.html#recruitment-modify-stages), if desired.

Customize stages
----------------

Stages can be modified, added, or deleted to match the particular hiring steps of a business.

### New stage

To create a new stage, click on  **Stage** and a new column appears. Enter the title for the new stage in the **Stage title** field, then click **Add**. The new column appears, and another new stage is available to create. If no new stages are needed, click anywhere on the screen to exit the new stage creation.

### Modify stage

To modify the settings of a stage, hover over the name of the stage, and a  **(Settings)** icon appears in the upper right hand side of the stage. Click on the  **(Settings)** icon and a menu appears. Then click on the **Edit** option. An **Edit: (Stage)** form appears. Make any desired modifications to the form, then click **Save & Close** when done.

#### Edit stage form

The **Edit: (Stage)** form is where the stage’s settings are configured. The only required field is the **Stage Name**.

The fields to be populated or modified are:

*   **Stage Name**: Type in a name for the stage.
    
*   **Email Template**: Select an email template to be used from the drop-down menu. If a template is selected, when the applicant card enters the stage, an email is automatically sent to the applicant using the selected template.
    
*   **Folded in Kanban**: Check the box to have the stage appear folded (hidden) at all times in the default view.
    
*   **Hired Stage**: Check the box if this stage indicates that the applicant is hired. When an applicant’s card enters this stage, the card displays a **Hired** banner in the upper right corner. If this box is checked, this stage is used to determine the hire date of an applicant.
    
*   **Job Specific**: If the stage only applies to specific job positions, select the job positions from the drop-down menu. Multiple job positions can be selected.
    
*   **Show in Referrals**: Check the box if this stage should be seen in the _Referrals_ application, and allow the referrer to accrue points when a referral of theirs reaches this stage. If this is active, a **Points** field appears. Enter the amount of referral points the employee receives when an applicant enters this stage. The **Referrals** app must be installed in order to use this option.
    
*   **Points**: If **Show in Referrals** is enabled, this field appears. Enter the number of points the employee earns when an applicant moves to this stage.
    
*   **Tooltips** section: There are three preconfigured status labels (colored circles) for each applicant’s card, indicating its status. These colors are displayed at the top of each stage to reflect the statuses of the applicants in the stage. The _names_ for the label can be modified, but the label itself (the color) cannot. The default names and labels are: **In Progress** (gray), **Blocked** (red), and **Ready for Next Stage** (green).
    
*   **Requirements**: Enter any internal notes for this stage explaining any requirements of the stage.
    

### Delete stage

If a stage is no longer needed, the stage can be deleted. To delete a stage, hover over the name of the stage, and a  **(Settings)** icon appears. First, click on the  **(Settings)** icon to reveal a drop-down menu, then click **Delete**. A **Confirmation** pop-up warning appears, asking **Are you sure you want to delete this column?** Click **Delete** to delete the column.

 Important

If there are applicants currently in the stage being deleted, an error pops up when attempting to delete the stage. The records currently in the stage to need to be either deleted, archived, or moved to a different stage before the stage can be deleted.

Email templates
---------------

To communicate with the applicant, Odoo has several preconfigured email templates that can be used. The preconfigured email templates and when to use them are as follows:

*   **Recruitment: Applicant Acknowledgement**: this template is used to let the applicant know that their application was received. This email is automatically sent out once the applicant is in the **New** stage.
    
*   **Recruitment: Interest**: this template is used to let the applicant know that their application caught the recruiter’s attention, and they have been shortlisted for either a phone call or an interview.
    
*   **Recruitment: Not interested anymore**: this template is used when an applicant communicates that they are no longer interested in the position, and thanks them for their time and consideration.
    
*   **Recruitment: Refuse**: this template is used when an applicant is no longer being considered for the position.
    
*   **Recruitment: Schedule Interview**: this template is used to let the applicant know that they have passed the **Initial Qualification** stage, and they will soon be contacted to set up an interview with the recruiter. This email is automatically sent out once the applicant is in the **Initial Qualification** stage.
    

 Note

Email templates can be created, modified, and deleted to suit the needs of a business. For more information on email templates, refer to the [Email templates](https://www.odoo.com/documentation/19.0/applications/general/companies/email_template.html) document.

To manually send an email, click **Send message** in the chatter. A text box appears, as well as the applicant’s email address.

Click the  **(Full composer)** icon in the bottom right corner of the **Send Message** tab in the chatter. A **Compose Email** pop-up window loads, with the **To** and **Subject** pre-populated. The applicant’s email address is entered in the **To** field, and the **Subject** is (Job Position). The email body is empty by default.

To use a preconfigured email template, click the  **(vertical elipsis)** button in the bottom of the window. Select the email template to use from the drop-down menu.

Preconfigured email templates may contain dynamic placeholders so unique information can be populated in the email for a more personalized message to the applicant. Several preconfigured email templates are available to choose from. Depending on the template selected, the email subject or body may change.

 Note

Only the email templates that are configured for the model load. Other email templates come preconfigured in Odoo, but if they are not configured for the recruitment application, they do not appear in the list of available templates.

If any attachments need to be added, click the  **(paperclip)** button at the bottom of the window. Navigate to the file to be attached, then click **Open** to attach it. To delete an attachment, click the  **(delete)** icon to the right of the attachment.

If any changes need to be made to the email, edit the body of the email. If the edits should be saved to be used in the future, the email can be saved as a new template. Click the  **(vertical elipsis)** button in the bottom of the window, and select **Save as Template**. Options are presented to either overwrite an existing template, or save a new template. Click on an existing template name to overwrite that template, or click **Save as Template** to save a new template. A **Create a Mail Template** pop-up window loads. Enter a name for the template in the **Template Name** field, then click **Save**.

To send the email, click **Send** and the email is sent to the applicant. The email then appears in the chatter.

 See also

*   [Job positions](https://www.odoo.com/documentation/19.0/applications/hr/recruitment/new_job.html)
    
*   [Post job positions](https://www.odoo.com/documentation/19.0/applications/hr/recruitment/post_job.html)
    
*   [Add new applicants](https://www.odoo.com/documentation/19.0/applications/hr/recruitment/add-new-applicants.html)
    
*   [Schedule interviews](https://www.odoo.com/documentation/19.0/applications/hr/recruitment/schedule_interviews.html)
    
*   [Offer job positions](https://www.odoo.com/documentation/19.0/applications/hr/recruitment/offer_job_positions.html)
    
*   [Refuse applicants](https://www.odoo.com/documentation/19.0/applications/hr/recruitment/refuse_applicant.html)
    
*   [Applicant analysis](https://www.odoo.com/documentation/19.0/applications/hr/recruitment/applicant_analysis.html)
    
*   [Source analysis reporting](https://www.odoo.com/documentation/19.0/applications/hr/recruitment/source_analysis.html)
    
*   [Velocity analysis](https://www.odoo.com/documentation/19.0/applications/hr/recruitment/velocity_analysis.html)
    
*   [Team performance](https://www.odoo.com/documentation/19.0/applications/hr/recruitment/team_performance.html)
    

[Edit on GitHub](https://github.com/odoo/documentation/edit/19.0/content/applications/hr/recruitment.rst)

##### On this page

*   [Settings](https://www.odoo.com/documentation/19.0/applications/hr/recruitment.html#settings)
    
*   [Kanban view](https://www.odoo.com/documentation/19.0/applications/hr/recruitment.html#kanban-view)
    
*   [Customize stages](https://www.odoo.com/documentation/19.0/applications/hr/recruitment.html#customize-stages)
    
*   [Email templates](https://www.odoo.com/documentation/19.0/applications/hr/recruitment.html#email-templates)
    

#### Get Help


Project dashboard
=================

The project dashboard allows you to get a comprehensive overview of your project’s status. It displays information such as the total number of tasks, timesheets, and planned hours linked to the project, as well as detailed information about project milestones and its costs and revenues. Within the project dashboard, you can create **Project updates**, which allow you to take a snapshot of the project’s status at a certain point in time. As such, it is a crucial tool for effective project management and ensuring that your project stays on track.

Using the project dashboard
---------------------------

To access the project dashboard, open the **Project** app and navigate to the applicable project. Click the  (**sliders**) icon to add **Dashboard** to the project’s [top bar](https://www.odoo.com/documentation/19.0/applications/services/project/project_management.html#project-project-management-top-bar).

 Tip

You can also access the project dashboard by hovering over the desired project’s card, clicking the  (**vertical ellipsis**), and selecting **Dashboard**.

The left side of the dashboard displays a list of existing [project updates](https://www.odoo.com/documentation/19.0/applications/services/project/project_management/project_dashboard.html#project-project-dashboard-updates), and the right side provides [detailed information about records linked to the project](https://www.odoo.com/documentation/19.0/applications/services/project/project_management/project_dashboard.html#project-project-dashboard-smart-buttons), as well as [milestones](https://www.odoo.com/documentation/19.0/applications/services/project/project_management/project_dashboard.html#project-project-dashboard-milestones), [profitability](https://www.odoo.com/documentation/19.0/applications/services/project/project_management/project_dashboard.html#project-project-dashboard-profitability), and [budgets](https://www.odoo.com/documentation/19.0/applications/services/project/project_management/project_dashboard.html#project-project-dashboard-budgets).

 Note

The information displayed on the project dashboard varies depending on the applications installed on your database. For example, you will not see information about **Timesheets**, **Planning**, or **Purchase Orders** if the corresponding applications are not installed.

### Totals smart buttons

The following smart buttons are displayed on the top right of the project dashboard:

> *   **Tasks**: the number of completed (i.e., **Done** or **Canceled** [tasks](https://www.odoo.com/documentation/19.0/applications/services/project/tasks/task_stages_statuses.html#project-tasks-task-stages-statuses-statuses)) and all tasks, in format completed/all, as well as the entire project’s completion percentage estimation.
>     
> *   **Timesheets**: the number of hours or days (depending on the **Timesheets** app configuration) allocated in the project’s **settings**. This includes all [timesheets](https://www.odoo.com/documentation/19.0/applications/services/timesheets.html), whether or not they have been validated.
>     
> *   **Planned**: the number of hours that have been planned for shifts in the **Planning** app. This includes all [planned shifts](https://www.odoo.com/documentation/19.0/applications/services/planning.html), including past shifts and shifts that have not yet been published.
>     
> *   **Documents**: number of [documents](https://www.odoo.com/documentation/19.0/applications/productivity/documents.html) in the project’s workspace.
>     
> *   **Burndown Chart**: click the smart button to access a [report](https://www.odoo.com/documentation/19.0/applications/essentials/reporting.html) on the status of the project’s tasks over time.
>     
> *   **Timesheets and Planning**: click the smart button to access a [report](https://www.odoo.com/documentation/19.0/applications/essentials/reporting.html) on the project’s timesheets and shifts. This allows you to easily compare planned and effective hours of work on the project.
>     
> *   **Additional fields**, such as **Sales Orders**, **Sales Order Items**, **Purchase Orders**, and more, represent the number of records linked to the project.
>     

 Tip

Use the project dashboard smart buttons to update the project records easily. Click **Timesheets** to validate timesheets, **Planned** to create project planning, **Documents** to view and validate documents, etc.

### Milestones

This section is only visible if [milestones](https://www.odoo.com/documentation/19.0/applications/services/project/project_management/project_milestones.html) have been enabled in the project you’re browsing: go to **Project**, click the  (**vertical ellipsis**) icon on one of your projects, and click on **Settings**. Click on the **Settings** tab, look for **Tasks Management** and make sure **Milestones** is enabled.

In a project’s Dashboard, click **Add Milestone** to create a new milestone. Click a milestone in the checklist to edit it, enable its checkbox to mark it as completed, or click the  (**trash**) icon to remove it.

The milestones are displayed in red if they’re past their deadline, or in green if they are ready to be marked as reached (i.e. tasks linked to the milestone that have been marked with **done** or **canceled** [status](https://www.odoo.com/documentation/19.0/applications/services/project/tasks/task_stages_statuses.html#project-tasks-task-stages-statuses-statuses)).

### Profitability

The [profitability dashboard](https://www.odoo.com/documentation/19.0/applications/services/project/project_management/project_profitability.html) provides a breakdown of project costs and revenues, which are impacted by all records linked to the project and its [Analytic account](https://www.odoo.com/documentation/19.0/applications/finance/accounting/reporting/analytic_accounting.html).

 Note

The profitability report is only displayed for billable projects.

### Budgets

If a budget has been set for the project, its status and related details are displayed in this section. Click **Add Budget** to create a new budget for the project.

 Note

[Budgets](https://www.odoo.com/documentation/19.0/applications/finance/accounting/reporting/budget.html) must be enabled in your database’s **Accounting** application in order for this section to be displayed.

Project updates
---------------

Project updates allow you to take a snapshot of the project’s overall status at a given point in time, for example, during a periodic (weekly, bi-weekly, or monthly) review. This allows you to compare specific data points, note any aspects of the project that need improvement, and estimate if the project is on or off track.

To create a new project update, go to the project dashboard, click **New**, and fill in the following fields:

> *   **Status**: Choose between **On Track**, **At Risk**, **Off Track**, **On Hold**, and **Done**. Once the status is set, a color-coded dot is displayed on the project’s Kanban card, allowing the project manager to easily identify which projects need attention.
>     
> *   **Progress**: Manually input the completion percentage based on the project’s progress.
>     
> *   **Date** and **Author**: These fields are automatically filled in with appropriate information based on the user who created the update and the current date.
>     
> *   **Description**: Use this rich-text field to gather notes. Depending on the project configuration (e.g., if the project is billable), this field may be pre-filled with current information on aspects such as profitability, budget, milestones, etc.
>     

[Edit on GitHub](https://github.com/odoo/documentation/edit/19.0/content/applications/services/project/project_management/project_dashboard.rst)

##### On this page

*   [Using the project dashboard](https://www.odoo.com/documentation/19.0/applications/services/project/project_management/project_dashboard.html#using-the-project-dashboard)
    
    *   [Totals smart buttons](https://www.odoo.com/documentation/19.0/applications/services/project/project_management/project_dashboard.html#totals-smart-buttons)
        
    *   [Milestones](https://www.odoo.com/documentation/19.0/applications/services/project/project_management/project_dashboard.html#milestones)
        
    *   [Profitability](https://www.odoo.com/documentation/19.0/applications/services/project/project_management/project_dashboard.html#profitability)
        
    *   [Budgets](https://www.odoo.com/documentation/19.0/applications/services/project/project_management/project_dashboard.html#budgets)
        
*   [Project updates](https://www.odoo.com/documentation/19.0/applications/services/project/project_management/project_dashboard.html#project-updates)
    

#### Get Help

 Project profitability

When handling billable projects, it is essential to determine whether your projects are turning a profit. Measuring **project profitability** involves keeping track of the costs of resources used to carry out the project, such as employee costs, materials used, purchases, expenses, or after-sales services, and comparing them with the project revenues.

Project profitability is tracked in the [project dashboard](https://www.odoo.com/documentation/19.0/applications/services/project/project_management/project_dashboard.html) on all billable projects.

To access the [project dashboard](https://www.odoo.com/documentation/19.0/applications/services/project/project_management/project_dashboard.html), open the **Project** app and navigate to the applicable project. Click the  (**sliders**) icon to add **Dashboard** to the project’s [top bar](https://www.odoo.com/documentation/19.0/applications/services/project/project_management.html#project-project-management-top-bar).

 Tip

You can also access the [project dashboard](https://www.odoo.com/documentation/19.0/applications/services/project/project_management/project_dashboard.html) by hovering over the desired project’s card, clicking the  (**vertical ellipsis**), and selecting **Dashboard**.

The **profitability dashboard** is on the right side of the project dashboard and displays data for all records linked to the project and its [analytic account](https://www.odoo.com/documentation/19.0/applications/finance/accounting/reporting/analytic_accounting.html). It’s divided into two major sections: [revenues](https://www.odoo.com/documentation/19.0/applications/services/project/project_management/project_profitability.html#project-project-profitability-revenues), which displays a breakdown of income generated by the project, and [costs](https://www.odoo.com/documentation/19.0/applications/services/project/project_management/project_profitability.html#project-project-profitability-costs) accrued by your company. The same record can be displayed in both sections, e.g., the same timesheet is listed under **Revenues** with the amount the customer paid for the work and under **Costs** with the amount of wages paid to the employees.

The amounts displayed in the profitability report are divided into three columns:

> *   **Expected**: the amounts expected based on existing sales or purchase orders.
>     
> *   **To invoice** (revenues) or **To bill** (costs): the amounts are moved to this column when the work or goods have been delivered, e.g., a [timesheet](https://www.odoo.com/documentation/19.0/applications/services/timesheets.html) has been created and/or validated, a delivery order has been marked as done, or the delivered quantity has been manually updated on the sales order.
>     
> *   **Invoiced** or **Billed**: the amounts are moved to this column once an invoice or bill has been confirmed.
>     

Based on the same principle, the revenues section is further divided into **Sold**, **Delivered**, and **Invoiced** columns. Use the  (**arrow**) icon to see a detailed breakdown for each line.

 Tip

Use the project’s [top bar](https://www.odoo.com/documentation/19.0/applications/services/project/project_management.html#project-project-management-top-bar) to easily access and edit records linked to the project’s profitability from the project’s Kanban view.

 Important

In order for a record to be displayed on the profitability dashboard, it must be linked to the project and its [analytic account](https://www.odoo.com/documentation/19.0/applications/finance/accounting/reporting/analytic_accounting.html).

The following records can be displayed in the profitability dashboard.

Revenues
--------

> *   **Timesheets**: revenues from [timesheets](https://www.odoo.com/documentation/19.0/applications/services/timesheets.html), broken down according to the **Invoicing Policy** selected on the product form (e.g., [Prepaid/Fixed Price](https://www.odoo.com/documentation/19.0/applications/sales/sales/invoicing/invoicing_policy.html), [Based on Timesheets](https://www.odoo.com/documentation/19.0/applications/sales/sales/invoicing/time_materials.html), [Based on Milestones](https://www.odoo.com/documentation/19.0/applications/sales/sales/invoicing/milestone.html)).
>     
> *   **Materials**: total of sales prices of products sold via sales orders linked to the project.
>     
> *   **Customer invoices**: a total of invoices linked to the project.
>     
> *   **Subscriptions**: a total of sales prices of [subscriptions](https://www.odoo.com/documentation/19.0/applications/sales/subscriptions.html) linked to the project.
>     
> *   **Down payments**: a total of [down payments](https://www.odoo.com/documentation/19.0/applications/sales/sales/invoicing/down_payment.html) linked to the project.
>     
> *   **Expenses**: any [expenses](https://www.odoo.com/documentation/19.0/applications/finance/expenses.html) that have been reinvoiced to the customer.
>     

Costs
-----

> *   **Timesheets**: total cost of time tracked by employees via [timesheets](https://www.odoo.com/documentation/19.0/applications/services/timesheets.html), based on the employee’s [HR settings](https://www.odoo.com/documentation/19.0/applications/hr/employees/new_employee.html#employees-hr-settings).
>     
> *   **Purchase Orders**: total cost of [purchase orders](https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/purchase/manage_deals.html) linked to the project. Those could cover goods, materials, or even subcontracted services. This entry only appears once the vendor bill is posted.
>     
> *   **Materials**: total cost of products included in [stock moves](https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/inventory/shipping_receiving.html) (deliveries and receipts) that have been validated for the project. This section is only displayed if **Analytic Costs** have been enabled in **Inventory ‣ Configuration ‣ Operations Types** for applicable operations. This ensures that the product’s cost is tracked during the stock move.
>     
> *   **Expenses**: total costs of [expenses](https://www.odoo.com/documentation/19.0/applications/finance/expenses.html) linked to the project that have been submitted and approved.
>     
> *   **Vendor bills**: total costs of [vendor bills](https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/purchase/manage_deals/manage.html) linked to the project’s analytic account.
>     
> *   **Manufacturing orders**: total costs of manufacturing orders linked to the project’s analytic account.
>     
> *   **Other costs**: any other costs linked to the project’s analytic account.
>     

[Edit on GitHub](https://github.com/odoo/documentation/edit/19.0/content/applications/services/project/project_management/project_profitability.rst)

##### On this page

*   [Revenues](https://www.odoo.com/documentation/19.0/applications/services/project/project_management/project_profitability.html#revenues)
    
*   [Costs](https://www.odoo.com/documentation/19.0/applications/services/project/project_management/project_profitability.html#costs)
    

#### Get Help

 Project milestones

**Milestones** enable you to track ongoing project work by designating a sequence of key steps that must be reached before the project’s completion. Milestones are particularly useful in expensive, long, or large-scale projects. They can be used purely for indicative purposes, as a way to ensure that the project is completed in a timely manner.

Milestones can also be used as a basis for [invoicing the client](https://www.odoo.com/documentation/19.0/applications/sales/sales/invoicing/milestone.html). This benefits both parties, as it ensures consistent cash flow for project funding and allows the client to pay for the project in several installments.

Configuration
-------------

Enable milestones for the desired project by opening the **Project** app, clicking the  (**vertical ellipsis**) on the project’s card, and clicking **Settings**. Under **Tasks Management**, enable **Milestones**.

 Note

Milestones are automatically enabled for projects created from a sales order for a service [invoiced by milestone](https://www.odoo.com/documentation/19.0/applications/sales/sales/invoicing/milestone.html).

Configure project milestones by clicking the  (**vertical ellipsis**) on the project’s card and selecting **Milestones**. Create a milestone by clicking **New**, entering the milestone’s **Name**, selecting a **Deadline** if desired, and clicking **Save**.

Add or remove options by clicking the  **sliders**. The following options are relevant when using [invoicing based on milestones](https://www.odoo.com/documentation/19.0/applications/sales/sales/invoicing/milestone.html):

> *   **Sales Order Item**: this field is filled in automatically with the Sales Order number.
>     
> *   **Quantity (%)**: percentage of the ordered quantity that will automatically be delivered on the sales order once the milestone is marked as reached.
>     

Once milestones are configured, **you can link project tasks to milestones**. To do so, navigate to the project you created the milestones in, then click one of the tasks to open it. Then, click the **Milestone** field to open a drop-down menu. Select the desired milestone from the list.

Once all the tasks linked to the milestone are completed (marked as [Done or Cancelled](https://www.odoo.com/documentation/19.0/applications/services/project/tasks/task_stages_statuses.html)), the milestone will be automatically marked as **Reached** in the **Project ‣ Settings ‣ Milestones**. You can also check the **Reached** box manually whenever the milestone is reached. Manual checking of the box will not impact the tasks linked to the milestone.

Using milestones
----------------

Odoo offers several ways to oversee the project’s milestones and their relationship to ongoing tasks.

In the **Gantt view**, a milestone is shown as a vertical line marked with a diamond shape, displayed on the day of the milestone’s deadline. The line is color-coded in blue to indicate that the milestone has not yet reached its deadline, or it has been marked as reached (in which case, a check mark is displayed on the milestone). A milestone is color-coded in red if it has not been reached by its deadline.

If a milestone’s deadline falls on the same day as the project’s deadline, it is displayed with a vertical line marked with a circle, and the same color coding principles as above apply.

Aside from the Gantt view, you can also create, edit, and mark milestones as reached from [the project dashboard](https://www.odoo.com/documentation/19.0/applications/services/project/project_management/project_dashboard.html#project-project-dashboard-milestones).

[Edit on GitHub](https://github.com/odoo/documentation/edit/19.0/content/applications/services/project/project_management/project_milestones.rst)

##### On this page

*   [Configuration](https://www.odoo.com/documentation/19.0/applications/services/project/project_management/project_milestones.html#configuration)
    
*   [Using milestones](https://www.odoo.com/documentation/19.0/applications/services/project/project_management/project_milestones.html#using-milestones)
    

#### Get Help

 Project templates

Templates allow you to create new projects with predefined settings, reducing the need to manually set up similar projects repeatedly.

Creating templates
------------------

To create a project template, an existing project is required and used as a base to be converted into a template. Converting a project into a template transfers the entire project’s properties to the template. This includes the project’s stages, tasks, sub-tasks, and their respective configurations, such as planned dates, statuses, assignees, and more.

First, access the settings of the project that you want to convert into a template by going to **Projects**, hovering your mouse over the project’s card, clicking the  (**vertical ellipsis**) icon, and selecting **Settings**. Review and adjust the project’s properties to ensure it reflects your desired template setup.

Once your project is ready, click the  (**cog**) icon and select **Convert to Template**. The **Template** banner indicates that the project has been successfully converted into a template.

 Warning

Converting a project into a template will also archive the original project used to create the template. To keep using a project that you want to convert into a template, duplicate it first by hovering your mouse over the project’s card, clicking the  (**vertical ellipsis**) icon, and selecting **Duplicate**.

 Tip

To edit or delete a template, go to **Projects ‣ New**. Next to the name of the template, click the  (**pencil**) icon to edit it or the  (**trash**) icon to delete it. Editing or deleting a template does not affect the projects that were previously created from it.

### Project roles in templates

Templates enable you to pre-select specific roles for tasks within your template, making the selection of assignees faster during the creation of a new project using a template.

Go to **Projects ‣ New**, and click the  (**pencil**) icon next to the name of the template you want to edit. Then click on the **Tasks** smart button, and on one of the tasks. In the **Project Roles** field, type or select the roles that you want to perform this task, then click **Save**.

Create a project based on this template: go to **Projects ‣ New**, and click on the name of the template. The **Create a project from template** form then includes **Project Roles**. For each of them, you can select assignees by clicking on the **Assignees** field. This automatically dispatches the right tasks to the right employees.

### Task scheduling in templates

In a project template, task scheduling can be automated according to the planned dates specified within the template.

 Important

Project and task planned dates are not saved when converting a project into a template. These require to be added to the template after it is created.

On the project template, define the **Planned dates** for both the project and each task. When tasks have planned start dates in the template, Odoo calculates the number of days between the project’s start date and the first scheduled task. This time window is referred to as the _delta_.

When a new project is generated from this template:

> *   The system uses the project’s start date as a reference.
>     
> *   Each task’s start date is automatically planned according to its delta.
>     
> *   If no start date is set on the new project, the current date is used as the default start date.
>     
> *   Task end dates are then determined automatically by Odoo’s scheduling algorithm.
>     

 Note

To ensure that all project roles and tasks are planned without conflict according to the team’s availability and workload, the scheduling algorithm calculates the end date of each task based on the allocated time, while also considering task dependencies and assignee’s availability, working schedule, time off, and public holidays.

Using templates
---------------

To create a new project from a template, go to **Projects ‣ New**, and click on a template in the **Project Templates** section. Enter a name for your project. Optionally, add a **Customer**, a **Planned Date**, and set up the task creation email. Then, click **Create Project**.

Templates can also be linked to specific products. To do so, the project template must be set as **Billable**:

*   Go to **Projects ‣ New** and click the  (**pencil**) icon next to the name of the template you want to edit.
    
*   Click the **Settings** tab, tick the **Billable** checkbox, and click **Save**.
    

Once this is done, configure the product by:

*   Selecting **Service** as the **Product Type**.
    
*   Selecting **Project** or **Project & Task** in the **Create on Order** field.
    
*   Selecting a **Project Template** and clicking **Save**.
    

[Edit on GitHub](https://github.com/odoo/documentation/edit/19.0/content/applications/services/project/project_management/project_templates.rst)

##### On this page

*   [Creating templates](https://www.odoo.com/documentation/19.0/applications/services/project/project_management/project_templates.html#creating-templates)
    
    *   [Project roles in templates](https://www.odoo.com/documentation/19.0/applications/services/project/project_management/project_templates.html#project-roles-in-templates)
        
    *   [Task scheduling in templates](https://www.odoo.com/documentation/19.0/applications/services/project/project_management/project_templates.html#task-scheduling-in-templates)
        
*   [Using templates](https://www.odoo.com/documentation/19.0/applications/services/project/project_management/project_templates.html#using-templates)
    

#### Get Help

 Task stages and statuses

Task stages
-----------

Task stages are displayed as columns in the project’s Kanban view, and allow you to update the progress of its tasks with a drag-and-drop. In most projects, the stages will be akin to **New**, **In progress**, **Backlog**, etc.

By default, task stages are project-specific but can be shared across multiple projects that follow the same workflow.

### Creating task stages

Odoo Project doesn’t provide default stages but instead allows you to create custom stages tailored to your specific business needs. You are prompted to do so immediately after [creating a new project](https://www.odoo.com/documentation/19.0/applications/services/project/project_management.html#project-management-configuration).

To create a stage, type its name into the **Stage…** field, then click **Add**.

 Tip

Click **See examples** to find ideas for stage names applicable to your line of business.

### Editing task stages

To edit the task stage, click the  (**cog**) icon next to its name. From there, click one of the following:

> *   **Fold**: to hide the task stage and all of the tasks in this stage from the Kanban view.
>     
> *   **Edit**:
>     
>     *   **Name**: to change the name of the stage.
>         
>     *   **SMS/Email Template**: to automatically send an email or SMS notification to the customer when a task reaches this stage.
>         
>     *   **Folded in Kanban**: to hide the task stage and all of the tasks in this stage from the Kanban view.
>         
>     *   **Projects**: to share this task stage between several projects.
>         
>     *   **Automations**: to create [custom rules that trigger automatic actions](https://www.odoo.com/documentation/19.0/applications/studio/automated_actions.html) (e.g., creating activities, adding followers, or sending webhook notifications). Note that this will activate Studio in your database, which may impact your pricing plan.
>         
> *   **Delete**: to delete this stage.
>     
> *   **Archive/Unarchive all**: to archive or unarchive all of the tasks in this stage.
>     

Task statuses
-------------

Task statuses are used to track the status of tasks within the Kanban stage, as well as to close the task when it’s done or canceled. Unlike Kanban stages, they cannot be customized; five task statuses exist in Odoo and are used as follows:

> *   **In Progress**: this is the default state of all tasks, meaning that work required for the task to move to the next Kanban stage is ongoing.
>     
> *   **Changes Requested**: to highlight that changes, either requested by the customer or internally, are needed before the task is moved to the next Kanban stage.
>     
> *   **Approved**: to highlight that the task is ready to be moved to the next stage.
>     
> *   **Canceled**: to cancel the task.
>     
> *   **Done**: to close the task once it’s been completed.
>     

 Note

*   The **Changes Requested** and **Approved** task statuses are cleared as soon as the task is moved to another Kanban stage. The task status reverts to the default **In Progress** status so that **Changes Requested** or **Approved** status can be applied again once the necessary work has been completed in this Kanban stage.
    
*   The **Done** and **Canceled** statuses are independent from the Kanban stage. Once a task is marked as **Done** or **Canceled**, it is closed. If needed, it can be reopened by changing its status.
    

[Edit on GitHub](https://github.com/odoo/documentation/edit/19.0/content/applications/services/project/tasks/task_stages_statuses.rst)

##### On this page

*   [Task stages](https://www.odoo.com/documentation/19.0/applications/services/project/tasks/task_stages_statuses.html#task-stages)
    
    *   [Creating task stages](https://www.odoo.com/documentation/19.0/applications/services/project/tasks/task_stages_statuses.html#creating-task-stages)
        
    *   [Editing task stages](https://www.odoo.com/documentation/19.0/applications/services/project/tasks/task_stages_statuses.html#editing-task-stages)
        
*   [Task statuses](https://www.odoo.com/documentation/19.0/applications/services/project/tasks/task_stages_statuses.html#task-statuses)
    

#### Get Help

 Task creation

Tasks in Odoo Project can be created manually or automatically, including from emails or website forms.

Manual task creation
--------------------

Open the Project app and choose the desired project. Create a new task by doing one of the following:

> *   Clicking the  (**plus**) button in the upper left corner. This creates a new task in the first stage of your Kanban view.
>     
> *   Pressing the  (**plus**) button next to the Kanban stage name. This creates a new task in this Kanban stage.
>     

Fill in the **Task Title** and add one or more **Assignees**, then click **Add**.

### Task configuration

Click the task to open it. The task form includes the following fields that you can fill in:

> *   **Task Title**: title of the task.
>     
> *    (**Star**): click the  (**star**) icon to mark the task as high priority. The icon will turn yellow. Click it again to remove the high priority.
>     
> *   **Project**: the project that this task belongs to.
>     
> *   **Assignees**: the person(s) in charge of handling the work on this task.
>     
> *   **Tags**: custom labels allowing to categorize and filter your tasks.
>     
> *   **Customer**: the person or company that will be billed for this task. This field only appears in tasks that belong to billable projects.
>     
> *   **Sales Order Item**: this can be either the sales order that was used to create this task, or a sales order that was linked to this task manually. This field only appears in tasks linked to billable projects.
>     
> *   **Allocated Time**: the amount of time that the work on this task is expected to last, tracked by timesheets.
>     
> *   **Deadline**: the expected end date of the task. Click the **Deadline** field to select the task’s end date in the dropdown calendar. To define the task’s duration, including its start and end dates (and optionally specific times), click the  (**fa-calendar-plus-o**) icon in the dropdown calendar, select the dates and times, then click **Apply** to save.
>     

 Tip

*   You can also create new tasks by switching to the list or Gantt view and clicking **New**.
    
*   The following fields can also be edited directly from the Kanban view without opening the individual task:  (**priority**), **Allocated hours**, **Assignees**, and **task status**. You can also **color code** or **Set a Cover image** to your task by clicking the  (**vertical ellipsis**).
    
*   Along with using the correct format, follow this order: the task’s name, followed by the allocated time, the tags, the assignee, and then the priority.For example, if you want to create a task named “Prepare workshop”, allocate 5h hours to it, add the “School” tag, assign it to Audrey and set its priority to **High**, enter the following task title: Prepare workshop 5h #school @Audrey !
    
    *   **30h**: to allocate 30 hours to the task.
        
    *   **#tags**: to add tags to the task.
        
    *   **@user**: to assign the task to a user.
        
    *   **!**: to star the task as high priority.
        

Creating tasks from an email alias
----------------------------------

This feature allows for project tasks to be automatically created once an email is delivered to a designated email address.

To configure it, open the Project app, then click the  (**vertical ellipsis**) icon next to the desired project’s name. Select **Settings**, then open the **Settings** tab.

Fill in the **Create tasks by sending an email to** field as follows:

> *   **Section of the alias before the @ symbol**: type the name of the email alias, e.g. contact, help, jobs.
>     
> *   **Domain**: in most cases, this is filled in by default with your [domain](https://www.odoo.com/documentation/19.0/applications/general/email_communication.html).
>     
> *   **Accept Emails From**: refine the senders whose emails will create tasks in the project.
>     

Once configured, the email alias can be seen under the name of your project on the Kanban dashboard.

When an email is sent to the alias, the email is automatically converted into a project task. The following rules apply:

*   The email sender is displayed in the **Customer** field.
    
*   The email subject is displayed in the **Task Title** field.
    
*   The email body is displayed in the **Description** field.
    
*   The whole content of the email is additionally displayed in the **chatter**.
    
*   All the recipients of the email (To/Cc/Bcc) that are Odoo users are automatically added as **followers** of the task.
    

Creating tasks from a website form
----------------------------------

If you have the Website app installed in your database, you can configure any form on your website to trigger the creation of tasks in a project.

1.  Go to the website page where you wish to add the form and [add the Form building block](https://www.odoo.com/documentation/19.0/applications/websites/website/web_design/building_blocks.html).
    
2.  In the website editor, edit the following fields:
    
    *   **Action**: select **Create a Task**.
        
    *   **Project**: choose the project that you want the new tasks to be created in.
        
3.  [Customize the form](https://www.odoo.com/documentation/19.0/applications/websites/website/web_design/building_blocks.html#website-building-blocks-form).
    

When the form is submitted, it automatically creates a project task. The task’s content is defined by the form’s corresponding fields.

 See also

[Website forms](https://www.odoo.com/documentation/19.0/applications/websites/website/web_design/building_blocks.html#website-building-blocks-form)

[Edit on GitHub](https://github.com/odoo/documentation/edit/19.0/content/applications/services/project/tasks/task_creation.rst)

##### On this page

*   [Manual task creation](https://www.odoo.com/documentation/19.0/applications/services/project/tasks/task_creation.html#manual-task-creation)
    
*   [Creating tasks from an email alias](https://www.odoo.com/documentation/19.0/applications/services/project/tasks/task_creation.html#creating-tasks-from-an-email-alias)
    
*   [Creating tasks from a website form](https://www.odoo.com/documentation/19.0/applications/services/project/tasks/task_creation.html#creating-tasks-from-a-website-form)
    

#### Get Help

 Recurring tasks

When handling a project, the same task often needs to be performed several times: for example, weekly meetings or status reports. The **recurring tasks** feature allows you to automate the creation of those tasks.

 See also

[Odoo Tutorials: Recurring tasks](https://www.odoo.com/slides/slide/recurring-tasks-6958)

Configuration
-------------

To use task dependencies in a project, go to **Project**, click the  (**vertical ellipsis**) icon on one of your projects, and click on **Settings**. Click on the **Settings** tab, look for **Tasks Management** and make sure **Recurring Tasks** is enabled.

### Set up task recurrence

In an existing task, click the  (**Recurrent**) button next to the **Deadline** field. Then, configure the **Repeat Every** field according to your needs.

A new task in recurrence will be created once the status of the previous task is set to **Done** or **Canceled**.

The new task is created on the project dashboard with the following configuration:

*   **Stage**: is set to the first stage of the project dashboard (**New** or equivalent);
    
*   **Name**, **Description**, **Project**, **Assignees**, **Customer**, **Tags**: are copied from the original task;
    
*   **Deadline**: is updated based on the **Repeat Every** field (e.g., if the task is set to repeat once a week, 7 days will be added to the deadline);
    
*   **Milestones**, **Timesheets**, **Chatter**, **Activities**, **Subtasks**: are **not** copied from the original task.
    

Once a recurrence is configured, a **smart button** on the task displays the total number of existing recurrences.

### Edit or stop task recurrence

**To edit** the recurrence, open the last task in recurrence. Any changes made on the task will be applied to the tasks that will be created in the future.

**To stop** the recurrence, open the last task in recurrence and press the **Recurrent** button next to the **Planned date**.

[Edit on GitHub](https://github.com/odoo/documentation/edit/19.0/content/applications/services/project/tasks/recurring_tasks.rst)

##### On this page

*   [Configuration](https://www.odoo.com/documentation/19.0/applications/services/project/tasks/recurring_tasks.html#configuration)
    

#### Get Help

 Sub-tasks

When handling project tasks, you can often benefit from splitting the workload into smaller **sub-tasks**, making it easier to track progress and manage the work.

Odoo’s sub-task feature is particularly useful in some of the following cases:

*   The task workload is too big to handle in one record.
    
*   There’s a clear sequence of steps to follow.
    
*   Some parts of the workload fall under the scope of different projects and/or assignees.
    

The original task to which sub-tasks are linked is referred to as the **parent task**. The sub-tasks of the parent task are known as **child tasks**.

Creating sub-tasks
------------------

To create a sub-task:

1.  Open the Project app, then go into your desired project.
    
2.  Click the task where you want to add the sub-task, then click the **Sub-tasks** tab.
    
3.  Click **Add a line**, then fill in the **Title**.
    
4.  Click the  (**save**) icon to save the task manually.
    

 Tip

You can edit several fields of a sub-task directly from the parent task’s sub-task tab without opening the individual sub-task. By default, those are: **Title**, **Priority**, **Status**, and **Assignees**. Use the  (**sliders**) icon to add or remove fields.

Once the new sub-task is created, the following changes occur in the parent task:

*   A **smart button** displays the total number of sub-tasks, as well as the number of closed (**done** or **canceled**) sub-tasks. Click the smart button to access the list of the sub-tasks.
    
*   The **Allocated time** displays the amount of time allocated to the parent task, as well as time allocated to the sub-tasks. This can be used to ensure that the time allocated to sub-tasks does not exceed time allocated to the parent task.
    
*   The **Timesheets** tab includes a breakdown of time spent on the parent task as well as sub-tasks.
    

Click **View** to open the sub-task you created. The sub-task form is identical to the [task form](https://www.odoo.com/documentation/19.0/applications/services/project/tasks/task_creation.html#task-creation-task-configuration).

 Tip

*   A **smart button** allows to navigate back to the **Parent task**.
    
*   The **Sub-tasks** tab allows for further creation of sub-tasks.
    
*   Selecting a **Project** will trigger this sub-task to be displayed in the Kanban view of the selected project.
    

[Edit on GitHub](https://github.com/odoo/documentation/edit/19.0/content/applications/services/project/tasks/sub-tasks.rst)

#### Get Help

 Task dependencies

Odoo Project allows you to break down projects into tasks and establish relationships between those tasks to determine the order in which they are executed. Task dependencies ensure that certain tasks begin only after the preceding tasks are completed.

To use task dependencies in a project, go to **Project**, click the  (**vertical ellipsis**) icon on one of your projects, and click on **Settings**. Click on the **Settings**. Click on the **Settings** tab, look for **Tasks Management** and make sure **Task Dependencies** is enabled.

Set task dependencies
---------------------

Task dependencies can be created from the task form or the project’s Gantt view by linking the successor task (i.e., the task blocked by other tasks) to its predecessor task(s) (i.e., the tasks blocking the successor task).

To create task dependencies from the task form, access the desired task and, in the **Blocked by** tab, click **Add a line**. Click **View** to access the predecessor task. To access the successor tasks from the predecessor task, click the **Blocked Tasks** smart button.

To create a task dependency from the Gantt view, hover your mouse over the predecessor task, then click one of the dots that appear around it. Drag and drop the dot onto the successor task. An arrow appears, indicating the dependency from the predecessor task to the successor.

Odoo automatically manages task progress based on their dependency. Successor tasks are assigned the **Waiting** status and cannot be moved to **In Progress** until their predecessor task(s) are marked as **Approved**, **Cancelled**, or **Done**.

Remove dependencies
-------------------

To remove a task dependency, proceed as follows:

*   From the task form, go to the **Blocked by** tab and click the  (**times**) button.
    
*   From the Gantt view, click the red  (**times**) button that appears at the center of the arrow when you hover your mouse over it.
    

[Edit on GitHub](https://github.com/odoo/documentation/edit/19.0/content/applications/services/project/tasks/task_dependencies.rst)

##### On this page

*   [Set task dependencies](https://www.odoo.com/documentation/19.0/applications/services/project/tasks/task_dependencies.html#set-task-dependencies)
    
*   [Remove dependencies](https://www.odoo.com/documentation/19.0/applications/services/project/tasks/task_dependencies.html#remove-dependencies)
    

#### Get Help