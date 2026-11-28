# Letter Request Drafts (2026-11-22)

Status: DRAFT. Scott reads, corrects, and sends. Claude does not send.
Items in [brackets] need Scott's input. Facts come from scottcjx.com and the intake answers only.

---

## 1. To Oliver Armitage (Axoft)

**Subject:** Recommendation letter request: PhD applications, first deadline Dec 1

Hi Oliver,

I hope you are well. I am applying to PhD programs for Fall 2027. Would you be willing to write a recommendation letter for me, based on my internship at Axoft from June to December 2025?

My first deadlines are close, and I am sorry for the short notice:

| Program | Letter deadline |
|---|---|
| MIT-WHOI Joint Program (Applied Ocean Science & Engineering) | Dec 1, 2026, 11:59 PM EST |
| Stanford EE PhD and Stanford ME PhD (2 applications) | Dec 1, 2026 |
| [Ellison Scholars, Oxford: only if the form asks for letters] | [Dec 1, 2026] |

Each portal sends you a link by email. One letter can be used for all programs.

At Axoft, I built hardware-in-the-loop systems for neural electrophysiology data acquisition, synchronization, and real-time processing, including a live decoding pipeline. [Add 1 or 2 specific results or moments that Oliver saw.] I also contributed to our NeurIPS 2025 workshop paper on decoding level of consciousness.

My research plan is integrated communication, sensing, and propulsion for underwater vehicles. This is my NTU thesis at the NUS Acoustics Research Lab. A letter from you can speak to how I build and debug real-time hardware and software systems.

I can send my CV, my draft statement, and a short list of points before you write. If the timeline does not work for you, I fully understand.

Thank you,
Scott

---

## 2. To Prof. Dusit Niyato (NTU, thesis supervisor)

**Subject:** Recommendation letter request: PhD applications, first deadline Dec 1

Dear Prof. Niyato,

I am applying to PhD programs for Fall 2027. Would you be willing to write a recommendation letter for me, as my NTU final-year thesis supervisor?

My first deadlines are close, and I am sorry for the short notice:

| Program | Letter deadline |
|---|---|
| MIT-WHOI Joint Program (Applied Ocean Science & Engineering) | Dec 1, 2026, 11:59 PM EST (Dec 2, 12:59 PM Singapore time) |
| Stanford EE PhD and Stanford ME PhD (2 applications) | Dec 1, 2026 |
| [Ellison Scholars, Oxford: only if the form asks for letters] | [Dec 1, 2026] |

Each portal sends you a link by email. One letter can be used for all programs.

My thesis is "Integrated Communications, Sensing, and Propulsion (ICSP)". It investigates the use of thrusters as acoustic transmitters, and I do the work at the NUS Acoustics Research Lab. [Add current progress: results so far, and how often you meet Prof. Niyato.] My PhD plan continues this direction on autonomous underwater vehicles.

I can send my CV, my draft statement, and a short summary of my thesis work before you write. If the timeline does not work for you, I fully understand.

Thank you very much,
Scott Cheng

---

## Notes for Scott
- Send both today (Sun 22 Nov). Oliver is in Cambridge, MA: 8 PM to 11 PM SGT is his morning.
- After each person agrees, add them in each portal at once. Then the portal sends the link.
- Tell Prof. Chitre the same list of programs and deadlines.
- Check: does Prof. Niyato know your work at NUS ARL well enough? If Prof. Chitre supervises the ARL work, the 2 letters may overlap. Ask Prof. Chitre and Prof. Niyato which parts each one can describe.

---

## 2b. Sending the draft letter to Prof. Niyato (he asked Scott to write it)

Updated 2026-11-28. The draft letter goes in the body of the email (Scott's choice). Plain email has no colours, so suggested wording is marked [Suggested: …] and gaps are marked [Please fill: …]. The same letter, with colours, is Scott's own copy `letters/rec-scott-niyato.docx` in the résumé repo (not committed): attach it too, so he can paste from Word if he prefers. Also attach the CV and the MIT-WHOI statement (v2 PDF). Deadline: 1 Dec 2026, 11:59 PM EST (2 Dec, 12:59 PM Singapore). Send as early as possible.

**Subject:** Draft recommendation letter for MIT-WHOI (deadline 1 Dec)

Dear Prof. Niyato,

Thank you for agreeing to write my recommendation letter. As you asked, I have written a draft for the MIT-WHOI Joint Program. It is below, and also attached as a Word file, with my CV and statement for reference.

The draft is written in your voice, and everything in it is yours to change:
- Plain text is factual.
- [Suggested: …] marks wording I have suggested. Please keep, change or delete it so that it matches your own view.
- [Please fill: …] marks the parts only you can complete.

The letter is due on 1 December, 11:59 PM EST, which is 2 December, 12:59 PM in Singapore. The portal should have sent you an upload link by email.

If anything in the draft is not accurate, or you would rather write it your own way, that is completely fine.

Thank you again for your support.

Best regards,
Scott

--- Draft letter ---

Dusit Niyato
President's Chair Professor in Computer Science and Engineering
College of Computing and Data Science, Nanyang Technological University
dniyato@ntu.edu.sg
1 December 2026

Admissions Committee
MIT-WHOI Joint Program in Oceanography/Applied Ocean Science and Engineering

Dear Members of the Admissions Committee,

I am writing to recommend Scott Jia Xu Cheng for the MIT-WHOI Joint Program in Applied Ocean Science and Engineering, [Suggested: and I do so with great enthusiasm]. I have supervised Scott's final year project at Nanyang Technological University since June 2026, jointly with Prof. Mandar Chitre of the Acoustic Research Laboratory at the National University of Singapore. My research is in wireless communication and networking. In recent years I have also co-authored work on underwater acoustic communication with collaborators, including integrated sensing and communication waveforms for underwater acoustic sensor networks, underwater acoustic channel estimation, and underwater acoustic backscatter. Over my career I have supervised [Please fill: number] undergraduate final year project students.

Scott's project, Integrated Communications, Sensing, and Propulsion, asks whether an underwater vehicle can communicate acoustically through its own thrusters. The idea is Scott's own; he brought it to us, and it is an unusual question for an undergraduate to pose. If it works, a small vehicle could send messages without a separate acoustic modem. Scott has done this work himself, seeking advice and feedback whenever he needed it. He began by characterizing the thrusters and their acoustic noise in an acoustically dampened tank, so that he knew what the thrusters actually produce before asking them to do more. He is now formulating techniques to inject communication signals into the thrusters' modulation, and the end goal is to integrate them into the UnetStack underwater networking framework.

[Suggested: From the point of view of my own field, Scott's project is an underwater form of integrated sensing and communication, with propulsion added as a third function of the same hardware. Most work in this area, including my own, assumes a dedicated acoustic transducer. Scott asks whether the vehicle's propulsion can do the job instead, which is a fresh and practical direction. It also raises the kind of question I work on: how to share one physical resource, here the thruster, between moving the vehicle and carrying data, and, once several thrusters or vehicles transmit, how they should share a slow and noisy acoustic channel.] Scott understands this networking side of the problem. On exchange at Queen's University in Canada he took a graduate networking course taught by Prof. Hesham ElSawy, [Suggested: whose work in wireless networking I know well]. The course went from the high-level design of wireless networks down to physical-layer modulation, and for his course project Scott studied how existing modulation and demodulation techniques can be applied to underwater acoustic signals to deal with intersymbol interference and multipath. He has also set integration into a full underwater network stack as the end goal of his final year project.

Scott is a self-starting researcher. He came to his supervisors with his own research question rather than asking for a topic, carried out the thruster characterization himself, and chose UnetStack as his target so that his work would meet a real networking framework. He does this while leading Mecatron, NTU's autonomous robotics team, as its Head. [Suggested: In our work together he has shown the attributes I look for in a doctoral student. He works independently: he plans the next step himself and comes to meetings with results and questions, not with a request for direction. He holds his own in technical discussions with researchers far more senior than him, defends his choices with evidence, and changes course when the evidence says he should. I have no doubt that he can carry a research project from a question to a result.]

[Suggested: In my assessment, Scott is among the top [X]% of the undergraduate students I have supervised.] [Optional, please fill: one example from our meetings that shows his independence or judgment.]

Scott already has clear ideas for where this work can go next: several thrusters on one vehicle transmitting together, the same thrusters used as an acoustic source for sonar or USBL positioning, and thruster-based communication to coordinate swarms of vehicles. [Suggested: These are research questions, not engineering tasks, and he needs the formal training in ocean acoustics and signal processing that a doctoral program gives.] The MIT-WHOI Joint Program, with its strength in underwater acoustics and its access to work at sea, is the right place for him to develop these ideas. [Suggested: I am confident he will succeed there, and I recommend him without reservation.]

Sincerely,

Dusit Niyato, IEEE Fellow
President's Chair Professor in Computer Science and Engineering
College of Computing and Data Science, Nanyang Technological University

--- End of draft ---
