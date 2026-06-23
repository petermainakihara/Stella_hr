I will first locate the Version 2 design document and read it together with odoo\_docs.md, then I will synthesize a phased implementation plan with dependencies and verification checkpoints.

Searched for files matching \`\*\*/\*Design\*Version\*2\*.md\`, no matches

Searched for files matching \`\*\*/\*System\*Design\*V2\*.md\`, 1 match

Searched for files matching \`\*\*/\*StellarHR\*Design\*.md\`, 1 match

Searched for files matching \`\*\*/odoo\_docs.md\`, 1 match

I found the new design file at stellaHR\_System\_Design\_V2.md and the Odoo reference file; next I’ll extract the full requirements deltas and translate them into an executable phase plan.

Read \[\](file:///home/wyckie/Desktop/ODOO/Soilex/custom\_addons/stellaHR\_System\_Design\_V2.md#1-1), lines 1 to 360

Read \[\](file:///home/wyckie/Desktop/ODOO/Soilex/custom\_addons/odoo\_docs.md#1-1), lines 1 to 320

I’ve finished reading both documents; next I’ll do a quick discovery of the current module state so the plan is a concrete delta from what is already implemented.

Read \[\](file:///home/wyckie/Desktop/ODOO/Soilex/custom\_addons/mobipine\_odoo\_project\_management)

Searched for files matching \`\*\*/custom\_addons/mobipine\_odoo\_project\_management/models/\*.py\`, 8 matches

Searched for regex \`checkin|session|documents\\.folder|doc\_type|ir\\.attachment|parent\_id|subtask|\_check\_session|readonly|smart button|folder\_id\` (\`\*\*/custom\_addons/mobipine\_odoo\_project\_management/\*\*/\*\`), 14 results

I now have the high-level delta; I’ll pull the rest of the V2 design and current manifest/security details so the plan includes exact sequencing and risk controls.

Read \[\](file:///home/wyckie/Desktop/ODOO/Soilex/custom\_addons/stellaHR\_System\_Design\_V2.md#361-361), lines 361 to 848

Read \[\](file:///home/wyckie/Desktop/ODOO/Soilex/custom\_addons/mobipine\_odoo\_project\_management/\_\_manifest\_\_.py)

Read \[\](file:///home/wyckie/Desktop/ODOO/Soilex/custom\_addons/mobipine\_odoo\_project\_management/security/ir.model.access.csv)

Read \[\](file:///home/wyckie/Desktop/ODOO/Soilex/custom\_addons/mobipine\_odoo\_project\_management/models/project\_task.py)

Read \[\](file:///home/wyckie/Desktop/ODOO/Soilex/custom\_addons/mobipine\_odoo\_project\_management/models/project\_project.py)

I’ve identified key planning constraints: V2 expects Odoo Documents features and session gates not yet present in the module, and there is a version/naming mismatch that needs explicit alignment before implementation sequencing.

Analyzing your answers...

Great, that resolves the big ambiguities; I’ll now produce a concrete delta plan from the current module to V2 features and persist it in the session plan file.

Read memory \[\](file:///home/wyckie/.config/Code/User/workspaceStorage/e2edae5d0e3bbbcdb7ffda0dc72a6a12/GitHub.copilot-chat/memory-tool/memories/NjE3NTVhNzYtMjdhOC00OThkLWI3YjctMGM4YmVmZjIxNGYw/plan.md)

Deleted memory \[\](file:///home/wyckie/.config/Code/User/workspaceStorage/e2edae5d0e3bbbcdb7ffda0dc72a6a12/GitHub.copilot-chat/memory-tool/memories/NjE3NTVhNzYtMjdhOC00OThkLWI3YjctMGM4YmVmZjIxNGYw/plan.md)

Created memory file \[\](file:///home/wyckie/.config/Code/User/workspaceStorage/e2edae5d0e3bbbcdb7ffda0dc72a6a12/GitHub.copilot-chat/memory-tool/memories/NjE3NTVhNzYtMjdhOC00OThkLWI3YjctMGM4YmVmZjIxNGYw/plan.md)

\## Plan: StellarHR V2 Implementation

Reviewed both documents and aligned the plan to your current codebase:

\- V2 design source: stellaHR\_System\_Design\_V2.md

\- Odoo Documents reference: odoo\_docs.md

Aligned decisions applied:

1\. Use Odoo 19 behavior as source of truth.

2\. Keep current namespace mobipine\_project.\*.

3\. Start with global system-wide document types only.

I also saved this full plan to session memory at /memories/session/plan.md.

\*\*Current Delta (What is missing now)\*\*

1\. Folder hierarchy automation is not yet implemented (Project → Task → Subtask).

2\. Session-based check-in gate (UI + ORM) is not yet implemented.

3\. Document type enforcement on uploads is not yet implemented.

4\. Manifest currently lacks Documents/frontend pieces needed for these V2 features.

\*\*Steps\*\*

1\. Phase 0: Baseline Alignment

2\. Update module loading strategy and dependencies for Documents and frontend assets in \_\_manifest\_\_.py. This blocks all V2 features.

3\. Define root-folder configuration policy using ir.config\_parameter and validate at runtime.

4\. Phase 1: Folder Hierarchy (depends on 2)

5\. Extend project and task models with folder-link fields and ancestry helpers in project\_project.py and project\_task.py.

6\. Add create hooks for project, task, and subtask folder creation with idempotent safeguards.

7\. Add smart buttons and counts on project/task forms in project\_project\_views.xml and project\_task\_views.xml.

8\. Add attachment routing rules so chatter uploads land in the corresponding folder.

9\. Phase 2: Session Gate (depends on 2, parallel with late Phase 1 validation)

10\. Add session model and lifecycle states (open/closed) in a new model module registered via \_\_init\_\_.py.

11\. Add project-level check-in/check-out actions and session history views.

12\. Add ORM enforcement on task writes and key task actions in project\_task.py.

13\. Add UI readonly gate feedback in task views/components for immediate user guidance.

14\. Phase 3: Document Types (depends on core folder plumbing, parallel with Phase 2 model work)

15\. Add global document type model plus admin configuration menu in menu\_views.xml.

16\. Extend attachments with doc\_type relation and indexing.

17\. Enforce required doc type on StellarHR upload paths and validate required-attachment expected types.

18\. Add filter/group support by document type in folder/file workflows.

19\. Phase 4: Security and Performance Hardening (depends on 8, 12, 17)

20\. Update ACL and record rules for sessions, folder visibility mirroring, and admin-only document type configuration in ir.model.access.csv and stellar\_hr\_rules.xml.

21\. Add/confirm indexes for project\_id, user\_id, state, folder\_id, doc\_type\_id.

22\. Add failure-safe handling for denied geolocation and invalid session operations.

23\. Phase 5: Verification and Milestone Documentation (depends on all above)

24\. Run module upgrade and smoke scenarios for hierarchy, session gate, and typed upload flows.

25\. Run role matrix tests: Associate vs PM vs Admin.

26\. Update checkpoint docs each milestone:

engineering log.md

concepts.md

postmortem.md

\*\*Verification\*\*

1\. Project/task/subtask creation produces nested folder hierarchy consistently.

2\. Archive/delete of project/task does not delete folders.

3\. Associate without open session cannot edit task/subtask; with open session can edit.

4\. PM/Admin can edit regardless of session.

5\. Only one open session per user+project is allowed.

6\. Uploads in StellarHR flows require document type and store it on attachment.

7\. Folder visibility does not leak across projects.

8\. Upgrade/install completes without registry or XML/security errors.

If you approve this plan, next step is to start Phase 1 implementation (folder hierarchy) and then move sequentially through Phase 2 and Phase 3.