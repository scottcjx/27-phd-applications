# Audit Log

Each entry has: date and time, actor, action, files, reason.

| Date/time | Actor | Action | Files | Reason |
|---|---|---|---|---|
| 2026-11-22 16:13 | Claude | Made project rules file, audit log, and visuals folder. Loaded ASD-STE100 skill. | CLAUDE.md, AUDIT_LOG.md, visuals/ | User request: set up project, keep audit log, use simple English, use web pages for visuals. |
| 2026-11-22 16:14 | Claude | Asked 4 setup questions. Wrote answers to profile file. Made first git commit. | PROFILE.md | Record user facts. User asked for a commit for each change. |
| 2026-11-22 16:15 | Claude | Asked 4 tracker questions. Wrote answers to profile file. | PROFILE.md | Record user facts before research and tracker build. |
| 2026-11-22 16:19 | Claude | Made intake question page v1 and published it as a private claude.ai page (answers saved in page storage, owner only). | visuals/intake-questions.html | User request: web page for questions. |
| 2026-11-22 16:19 | Claude | Read scottcjx.com (8 pages) with a web-fetch agent. Read plan doc 'PhD Lab Shortlist' (read only, no edits). Wrote facts to file, marked not confirmed. | sources/known-facts.md | User gave website and plan doc as inputs. |
| 2026-11-22 16:22 | Claude | Rebuilt intake page as v2 (fact check + open questions), published as v2 and v3. v3 adds a Topics field. | visuals/intake-questions.html | User gave website and plan doc; most v1 questions were already answered. |
| 2026-11-22 16:22 | Claude | Found v1 answers (topics, topics not wanted) in page storage. v2 save replaced them. Backed up v1 answers to a local file. Tried 2 merge writes; both stopped by version check because the user was typing. No data written by Claude. | answers/intake-v1-2026-11-22.json | Do not lose user answers. Do not overwrite live edits. |
| 2026-11-22 16:27 | Claude | Read intake answers (db version 48). Saved copy and wrote confirmed facts to profile. | answers/intake-v2-2026-11-22.json, PROFILE.md | User said answers are ready. |
| 2026-11-22 16:29 | Claude | Asked 4 questions in chat. Wrote to page storage (db v49): put back v1 topics (user approved); also wrote chat answers: MIT-WHOI PIs not contacted, Dusit Niyato added as recommender. | PROFILE.md, intake page db | User approved topic restore. Keep page the same as chat answers. |
| 2026-11-22 16:31 | Claude | Checked deadlines: 8 web searches + 2 web-fetch agents (official pages). Oxford and Imperial pages blocked (403). Wrote deadline table. | sources/deadlines-2027.md | User chose 'Check all deadlines'. |
| 2026-11-22 16:32 | Claude | Incoming professor search round 1: 11 extended web searches. Wrote leads file. | sources/incoming-profs-search-1.md | User request: incoming profs in next 6 months, PhD from June. |
