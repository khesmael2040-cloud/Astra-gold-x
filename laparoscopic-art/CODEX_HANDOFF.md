# Codex Handoff — LAPAROSCOPIC ART Book

## Mission
Complete the user's existing LAPAROSCOPIC ART book as a genuinely expanded, professionally edited, bilingual (Arabic/English) practical manual and surgical atlas. Deliver both an editable Word manuscript and a print-ready PDF. Target approximately 200 substantive pages; page count must come from useful content, not padding.

## Source-of-truth files (must be added to this project workspace before execution)
1. The uploaded LAPAROSCOPIC ART – Complete Print Edition PDF (74 pages) is the primary/base edition. Preserve its identity, organization, terminology, useful material, and visual learning system.
2. The prior expanded Word draft LAPAROSCOPIC_ART_Expanded_Manual_200p_2.docx is auxiliary material only. Audit it, reuse good material selectively, remove repetition/template filler, and do not treat its page count as proof of completeness.
3. If available, use the original LAPAROSCOPIC_ART_Complete_Bilingual_Encyclopedia as an additional source. Do not silently invent or overwrite source-specific claims.

If these source files are not present in the Codex workspace, STOP content production and report exactly which files are missing. Do not fabricate a reconstruction from filenames or this handoff. Ask the user to add the files to laparoscopic-art/source/.

## Scope and editorial priorities
- Expand every existing chapter substantially and coherently, with special emphasis on manual laparoscopic instrument skills.
- Build detailed, progressive simulation curricula for: camera navigation and horizon control; 0°/30° optics; depth perception; triangulation; dominant/non-dominant hand coordination; peg transfer; precision cutting; object transfer; atraumatic grasping; dissection; needle handling and driving; intracorporeal/extracorporeal knotting; suturing; ambidexterity; FLS-style drills.
- For each skill include: learning objectives, setup/equipment, starting posture, stepwise drill, progression levels, common errors, troubleshooting, coach dialogue, objective scoring rubric, pass/progression criteria, and practice log/checklist.
- Retain and expand relevant chapters on access/port geometry, ergonomics, anatomy, pelvic retroperitoneal spaces, ureter identification/ureterolysis, energy devices, hemostasis, complication recognition, and gynecologic procedures only where supported by source material and verified references.
- Include algorithms, decision trees, tables, figure plans/diagrams, and consistent bilingual terminology. Do not create decorative filler.
- Preserve the source's color-coded pedagogy: green = Surgical Pearls & Master Secrets; yellow = Practical Tips & Tricks; red = Complication Traps; blue = Anatomical Landmarks & Safe Planes. Use accessible contrast and consistent styles.
- Add educational dialogues and realistic simulation scenarios.
- Add a robust references section. Verify every clinically material recommendation against authoritative, current sources; distinguish source-derived statements from external additions. Cite claims near the text. Never fabricate references, guidelines, page numbers, or DOI data.

## Medical safety and accuracy
This is an educational/simulation manual, not a substitute for accredited training, supervised hands-on instruction, institutional protocols, or attending-surgeon judgment. Surgical techniques and access recommendations are context-dependent. Do not present a single technique as universally safe. Explicitly flag high-risk steps, contraindications, uncertainty, and the need for supervised practice. Never invent clinical outcomes or success rates. Mark any section requiring expert clinical review before publication.

## Production requirements
- Create a clean project structure under laparoscopic-art/ only. Do not modify ASTRA core, social-agent/, or unrelated files.
- Keep source files unchanged under laparoscopic-art/source/.
- Produce a structured manuscript source (Markdown or DOCX-generation source), editable .docx, and print-ready .pdf under laparoscopic-art/dist/.
- Professional book layout: title page, copyright/disclaimer, detailed table of contents, consistent chapter hierarchy, headers/footers, page numbers, figure/table numbering and captions, glossary, abbreviations, references, index if feasible.
- Bilingual Arabic/English typography must render correctly (Arabic shaping, right-to-left direction, punctuation, mixed Latin terms). Verify embedded fonts and PDF text extraction/rendering. Do not ship a PDF with broken Arabic glyphs.
- Avoid large blank pages, accidental orphan headings, duplicate paragraphs, repetitive template sections, broken tables, clipped text, and missing figures.
- Use original vector diagrams where useful; each diagram must be technically meaningful, labeled, captioned, and cross-referenced. Do not use unlicensed copyrighted images.
- Deliver Word and PDF at a print-appropriate page size with embedded fonts and consistent margins.

## Required QA gates (all must pass before calling the work complete)
1. Source inventory: list exact source files, page counts, and formats; confirm all are readable.
2. Content audit: map every source chapter to its expanded destination; list retained, expanded, merged, and omitted sections with reasons.
3. Editorial audit: detect repeated paragraphs/boilerplate and verify chapter completeness.
4. Clinical audit: reference-check surgical claims; flag unresolved high-risk claims for human expert review.
5. Layout audit: render the full PDF to page images; inspect representative pages from beginning, middle, and end plus every page flagged by automated checks.
6. Technical audit: verify DOCX opens; PDF page count; fonts; Arabic RTL; links; table/figure numbering; no blank/error pages; no overflow/clipping.
7. Deliver a concise QA report with page count, word count, chapter coverage, reference count, unresolved review flags, and exact output paths.

## Execution behavior
Work autonomously in this isolated branch and folder. Do not stop for cosmetic preferences. If a source is missing, report the blocker instead of guessing. Make incremental commits with meaningful messages. Do not merge to main. Do not claim completion until both final files and the QA report exist and have been inspected.