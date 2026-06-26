# Work Instruction: TRT → Zenodo Publishing

Internal SOP for taking a TRT paper from repo source to a citable Zenodo DOI. Reuses the proven `ologos-repos/zenodo-publisher` tool and the central production token — nothing new to build, only TRT conventions on top.

## Prerequisites (already in place)

- **Tool:** `/media/jdlongmire/Macro-Drive-1TB/GitHub_Repos/ologos-repos/zenodo-publisher/zenodo_publisher.py` — creates a draft deposition, uploads files, applies metadata, `--publish` only when explicit, `--sandbox` supported.
- **Token:** the production token (publish-capable: `deposit:write` + `deposit:actions`) lives in `~/.thinxai-credentials` under the name **`ZENODO_ACCESS_TOKEN_PROD`**. The publisher reads **`ZENODO_ACCESS_TOKEN`**, so map it at run time (see below). **Never** commit it, echo it, or pass the whole credentials file to the tool (it holds every thinx secret, not just Zenodo).

  ```bash
  export ZENODO_ACCESS_TOKEN="$(grep '^ZENODO_ACCESS_TOKEN_PROD=' ~/.thinxai-credentials | cut -d= -f2-)"
  ```
- **PDF build:** `pandoc` + `xelatex` are installed; the deposited artifact is a built PDF (single-source rule below).

## Single-source rule

The paper's Markdown (`*.md`) is canonical. The deposited PDF and any public HTML are **built** from it, never authored separately, so the citable record and the reading view cannot drift.

## Per-paper layout

Each citable paper is a self-contained folder carrying its source, deposit metadata, and (post-publish) its record:

```
<paper-folder>/
  <paper>.md         # canonical source
  metadata.json      # Zenodo deposit metadata (see template below)
  RECORD.md          # written back AFTER publishing: DOI, concept DOI, URL, version
  <paper>.pdf        # built artifact (gitignored; rebuilt on demand)
```

The position paper's folder is [`1-hypothesis/paper/`](../../1-hypothesis/paper/). Future standalone result-papers (a co-admissibility paper, a gravity paper) get their own folder — co-located with the tier they report from, or a top-level `papers/<slug>/`.

## Deposit-readiness gate (do NOT skip)

A paper is deposited **only** when:

1. **References verified** — the carried-forward citations are checked against primaries ([issue #1](https://github.com/jdlongmire/triadic-reality-theory/issues/1); [`references/verification-status.md`](../../references/verification-status.md)). No deposit on unverified citations.
2. **Public copy cut** — the working-draft status note is stripped (the note itself says it must be removed from any circulation draft; **a Zenodo deposit is circulation**). Deposit the stripped public version, not the working master.
3. **Version set** — the Zenodo `version` tracks the paper version. **TRT v0.9 is a working draft and is NOT deposited.** First deposit is at **v1.0** readiness (or a deliberately-labelled preprint, JD's call).
4. **Figures resolved** — every figure built and inserted; **zero `[FIGURE-PLACEHOLDER]` markers** in the public copy. Check: `grep -rn '\[FIGURE-PLACEHOLDER\]' <paper>` returns nothing. (See [`figures.md`](figures.md).)

Corrections after publishing are a **new version** of the same record (the concept DOI preserves lineage) — never delete a published version.

## Procedure

```bash
PUB=/media/jdlongmire/Macro-Drive-1TB/GitHub_Repos/ologos-repos/zenodo-publisher
PAPER=1-hypothesis/paper          # the paper folder

# 0. Map the token into the name the publisher expects (value stays out of argv/logs):
export ZENODO_ACCESS_TOKEN="$(grep '^ZENODO_ACCESS_TOKEN_PROD=' ~/.thinxai-credentials | cut -d= -f2-)"

# 1. Build the PDF from the canonical markdown (public copy once it exists)
./0-program-methods/ops/build-paper.sh "$PAPER/TRT-v1.0-public.md" "$PAPER/TRT-v1.0.pdf"

# 2. Fill $PAPER/metadata.json (title, description/abstract, version, keywords).

# 3. DRAFT deposit (review before publishing — never publish blind):
python "$PUB/zenodo_publisher.py" "$PAPER/TRT-v1.0.pdf" --metadata "$PAPER/metadata.json"
#    -> review the draft on zenodo.org

# 4. PUBLISH only after JD approves the draft:
python "$PUB/zenodo_publisher.py" "$PAPER/TRT-v1.0.pdf" --metadata "$PAPER/metadata.json" --publish

# 5. Write back the minted DOI into $PAPER/RECORD.md.
# 6. Update CITATION.cff with the DOI; add a references entry; note in 3-prediction/appraisal.md.
```

**Sandbox option:** to rehearse the full pipeline without touching production, use `--sandbox` (requires a separate sandbox.zenodo.org token). Useful for a first end-to-end dry run.

## Governance (binding)

- **Publishing is a soft-stop** (thinx `morals.md`: publish to an external surface, incurs a DOI commitment). **Always draft-first; JD reviews the draft on Zenodo; `--publish` only on explicit JD approval.** Never auto-publish.
- **Token hygiene:** read from `~/.thinxai-credentials`; never echo it, never commit it, never paste it into a deposit body.
- **Authorship / provenance:** sole author *Longmire, James D.* (ORCID 0009-0009-1383-7698), with an **AI-enabled** provenance note in `metadata.json` (consistent with ADR-GOV-0004 and the inaugural-batch deposits — see [[project-zenodo-redeposit-ai-enabled]]). Confirm with JD before first deposit.
- **Community:** default **account-level (no community)** — TRT is foundational physics, neither theology nor the `scientific-designism` stream. A relevant community can be attached later without changing the DOI.
- **Traceability:** the minted DOI is part of the citable record — record it in `RECORD.md`, `CITATION.cff`, and `related_identifiers`.

## Metadata template

See [`1-hypothesis/paper/metadata.json`](../../1-hypothesis/paper/metadata.json), pre-filled for the position paper and gated per the readiness rule above.
