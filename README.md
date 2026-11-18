# Your personal health history with AI — no dedicated app required

A template for a personal project: a folder of ordinary files where an AI agent stores, reads, and compares your health information. You choose the model and tools; you do not need a dedicated app or a server database to get started.

You need an AI agent that can read and edit files on your computer; see [Connecting an AI agent](#agent).

The template contains no real medical history. The [demo data](examples/README.md) is entirely fictional and kept separate from the working data layers.

> **Privacy.** Your chosen AI model processes the contents of your documents, which may be sent to its provider. Do not publish your personal medical history or store it in a public repository. See [Privacy and publication](#privacy).

## Contents

- [What the system is and what problem it solves](#motivation)
- [Features and use cases](#scenarios)
- [Quick start](#quick-start)
- [Architecture and the role of each layer](#architecture)
- [Creating your own project from the template](#own-project)
- [Connecting an AI agent](#agent)
- [Adding documents and other data sources](#intake)
- [Asking questions and getting results](#queries)
- [Extending the system and reprocessing data](#extension)
- [AI limitations and handling medical information](#limitations)
- [Privacy and publication](#privacy)

<a id="motivation"></a>
## What the system is and what problem it solves

The system helps you use your accumulated medical history when addressing current health questions. Before a doctor's appointment, you can review tests and prescriptions. When a new lab result arrives, you can see how the values have changed. If you have several prescriptions, you can compare them with what you actually take and prepare questions for your doctor.

This requires connecting information from different sources: when an event occurred, what preceded it, what recommendations were made, and what changed afterward. As you add documents, measurements, and your own messages, you build a history that you can revisit with new questions. AI helps find and compare relevant information, while links to original documents let you check its answers.

Storing this history in ordinary files makes it accessible to different AI models and tools. You can choose an agent, change how the data is processed, and adapt the system to your needs while retaining the accumulated data and originals.

<a id="scenarios"></a>
## Features and use cases

| Request | What you get |
|---|---|
| "Help me prepare for a doctor's appointment" | A concise history tailored to the visit, tests, prescriptions, changes, and questions for the doctor, with document links |
| "Show trends in my measurements" | Comparable values by date, units, provenance, and charts with gaps identified |
| "Check my medication schedule against my doctors' prescriptions" | A comparison of prescriptions, your reported regimen, and the product's composition; discrepancies and a calendar of expected changes |
| "Show the latest results for all my lab tests" | A table of the latest available results with dates, reference ranges, and coverage limitations |
| "Compare my sleep, activity, and weight" | Observations and calculations with explicit coverage; coinciding changes are not presented as causation |
| "Import this document" | A preserved source and a readable material |
| "Record a measurement" | An entry in an ongoing observation series, with provenance |

Requests are not limited to this list. You can search the contents, assemble selections, and create new reports. Processing capabilities depend on the agent's tools and the source format.

<a id="quick-start"></a>
## Quick start

1. On GitHub, choose **Code → Download ZIP**, then extract it to a folder on your computer. Use a local folder or a private repository for your medical history.
2. Open the extracted folder containing `AGENTS.md` in an AI agent that can read and edit local files. Ask the agent to check that Python 3.11 or later is available in its terminal. The text demo below runs with Python's standard library.

   Send this message:

   ```text
   Read AGENTS.md and help me get started with the project.
   ```

3. For a first run with fictional data, copy [`examples/demo-lab.txt`](examples/demo-lab.txt) into `incoming/` in this disposable copy of the project. Say "Import this document." After verification, the agent should link to the material card listed in [`materials/INDEX.md`](materials/INDEX.md). The card links to the original in `raw/`.
4. Ask "What value does the demo document report, and where can I verify it?" The answer should give **4.20 demo units** and point to page 1 through the material card.

For your own documents, start with a fresh copy and put one document in `incoming/`. Additional tools may be needed for formats such as scanned PDFs. See [Connecting an AI agent](#agent) and [the full fictional demonstration](examples/README.md).

<a id="architecture"></a>
## Architecture and the role of each layer

Original documents, extracted materials, facts, and query results are stored separately and connected by links. Data moves through the layers in sequence:

```text
incoming → raw → materials → records → overview → outputs

Supporting directories:
  scripts        repeatable operations
  documentation  rules and contracts
  temp           temporary processing
```

| Directory | Purpose |
|---|---|
| [incoming/](incoming/AGENTS.md) | Originals awaiting intake or still being processed |
| [raw/](raw/AGENTS.md) | Accepted originals, unchanged, in dated directories |
| [materials/](materials/AGENTS.md) | Full readable text and tables for individual documents, cards, a registry, and an index |
| [records/](records/AGENTS.md) | Facts from multiple sources, topics, measurements, alternative versions, and contradictions |
| [overview/](overview/AGENTS.md) | A compact medical overview and timeline, created once data is available |
| [outputs/](outputs/AGENTS.md) | Dated reports, charts, doctor visit packages, and other query results |
| [scripts/](scripts/AGENTS.md) | Repeatable technical operations without patient-specific data |
| [documentation/](documentation/AGENTS.md) | Architecture, requirements, current state, decisions, and specifications |
| [temp/](temp/AGENTS.md) | Intermediate files; permanent results do not depend on them |
| [examples/](examples/AGENTS.md) | Fictional examples only, outside the working medical history |

### End-to-end example: one document's journey

You put a scan of a complete blood count in `incoming/` and say: "Import this document." Here is what happens next.

1. **incoming/** — the scan waits for intake.
2. **raw/** — after intake, the original is preserved unchanged in a dated directory.
3. **materials/** — the agent reads the document: readable text, a table of results, a document card, and registry and index entries are created.
4. **records/** — individual facts, such as a hemoglobin value with its date, unit, and document link, join the measurements alongside results from earlier tests.
5. **overview/** — the new event is added to the overview and timeline.
6. **outputs/** — you ask: "Show trends in my measurements." A report or chart is saved in a dated subdirectory. Each value links to a fact and then to its original document.

Originals remain available after processing. From an answer, you can follow links to the information used and the original document. This lets you check the result and revisit the documents when new questions arise.

<a id="own-project"></a>
## Creating your own project from the template

For a local copy, use **Code → Download ZIP** on GitHub and extract it into a separate folder. If GitHub shows **Use this template**, you can also use it to create a private repository. Open your local project folder in your AI agent environment.

The new project starts with an empty medical history. Gradually add your documents, observations, and exports. Keep a backup of the project folder in a secure location.

<a id="agent"></a>
## Connecting an AI agent

You need an AI agent that can open a folder on your computer and read and edit files. Photos and scans require image recognition; voice recordings require speech recognition. Capabilities depend on the model and environment you choose.

Open the project folder in the agent environment and send the first message from the [quick start](#quick-start).

No particular AI provider is required. A local model may reduce the amount of data sent externally, but its tools and recognition quality also need to be checked. An ordinary chat without filesystem access cannot maintain the folder on its own: you would need to transfer files and save results manually.

<a id="intake"></a>
## Adding documents and other data sources

Attach a file to a message in your chat with the AI agent and say:

```text
Import this document.
```

Or copy files into your project's `incoming` folder and say:

```text
Import the documents from incoming.
```

You can add lab results, doctors' reports, discharge summaries, product packaging photos, and other documents this way. If something cannot be read or needs clarification, the agent will tell you.

You can also add messages without a document:

```text
My weight today is 72 kg.
```

The same approach works for reporting how you feel and what medications you take. Add spreadsheets and app exports as files: for example, an Excel workbook, a workout archive, or sleep and activity data. A new kind of export may require setting up a processing method.

Include details that matter for interpreting the request. For example:

```text
Import the cardiologist's report. There are two scan files in incoming, one for each side.
```

The model will use this context to treat the two files as a single data source.

<a id="queries"></a>
## Asking questions and getting results

Ask your question in chat. Specify a time period or purpose if needed:

```text
Help me prepare for my cardiologist appointment.
```

```text
Show my weight trend over the past year.
```

```text
Check my medication schedule against my doctors' prescriptions.
```

The answer appears in chat. Prepared reports, tables, and charts are saved in a dated subdirectory of `outputs`. You can open them separately or use them to prepare for a doctor's visit. Available formats depend on the agent's tools.

<a id="extension"></a>
## Extending the system and reprocessing data

Ask the agent to support a new data source, prepare a new kind of report, or improve document recognition. For example:

```text
There is an archive from my fitness app in incoming. Import it.
```

```text
Read this report again: some of the text was left illegible last time.
```

Preserved originals let you repeat processing with another model or tool. You can ask for an older report to be updated with new data.

<a id="limitations"></a>
## AI limitations and handling medical information

AI can misread a document, confuse numbers, or draw an incorrect conclusion. Built-in checks reduce the risk but do not eliminate errors. Check important information against the original before using it, especially medication names and doses.

An answer's completeness depends on the data you have added. A missing document does not mean there was no illness or treatment. Changes occurring at the same time do not establish causation.

Use the system to find, compare, and prepare information and questions for a healthcare professional. Choosing treatment, stopping medication, and changing doses require a doctor. The project does not replace an examination and is not intended for emergency assessment.

Document recognition and result preparation depend on the chosen model and its tools. The template does not include background monitoring or automatic notifications. A calendar of expected changes is a query result, not an enabled notification service.

<a id="privacy"></a>
## Privacy and publication

Publish the clean template and keep your personal history separate. Medical data can appear in filenames, extracted text, the registry, charts, metadata, GPS tracks, logs, and backups. Do not upload the entire folder to a cloud service without deliberately choosing the data and reviewing its processing terms.

Use private storage and separate backups for your personal history. A `.gitignore` file does not protect files or revision history that have already been published. See the [privacy rules](documentation/PRIVACY.md).
