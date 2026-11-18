# Material classification

Classify after reading contents during intake. Classification supports search, processing selection, and collections; it neither establishes a diagnosis nor replaces health analysis.

## Independent attributes
- material_type: laboratory result, clinical consultation, instrumental examination, data export, or unknown. JPEG/PDF/ZIP describe file formats, not medical material types.
- subtype: a specific subtype such as ECG or complete blood count. Determine it from content; permit new values after checking real materials.
- domains: content domains, potentially several. A mixed laboratory panel can involve endocrinology and immunology simultaneously.
- primary_domain: the main domain if identifiable confidently, otherwise null. For a consultation it usually follows the author's explicitly stated specialty.
- basis: short content-based rationale; status and reviewed_date record classification review.

Machine-readable codes and labels: [classification.json](../../materials/classification.json). Each material's classification is stored in [manifest.json](../../materials/manifest.json), with a readable version at the card's beginning.

Route processing using classification.material_type and classification.domains. The older technical kind field, where present, describes an earlier format/handler choice, not a unified content classification.

Author specialty and content topics differ: an immunologist's report may discuss the thyroid. Exports can use Physical activity, Sleep, and Anthropometry domains without assigning a clinician specialty.

## Uncertainty and changes
Do not determine type/domain from filename, extension, or directory name. If information is insufficient, use unknown/needs_review; do not infer a specialty from a diagnosis-like word. Keep several domains and selection rationale for mixed documents.

One classification applies to the whole document, even when it spans several files. Changing labels does not change identifier, dates, or originals. Labels can be revised and do not strictly limit searches: no label does not establish no relevant information.

## Selecting further processing
- Type determines what to read/extract: measurement tables, consultation sections, examination plots/protocol, or export time series.
- Domains help select material for a question or specialist; they do not determine type. ECGs and cardiology consultations share a domain but have different types and processing.
- The index navigates by type, domain, and date without aggregate statistics. The manifest supports programmatic filtering.

## Verification
Check that type and domain codes exist, primary_domain belongs to domains or is null, rationale is supported by contents, and card/manifest agree. Check mixed lab panels, consultations, ECGs, and exports rather than one type alone.
