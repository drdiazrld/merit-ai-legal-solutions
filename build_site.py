from pathlib import Path
from html import escape

ROOT = Path(__file__).parent

NAV = [
    ("Work and limits", "capabilities.html"),
    ("Commands", "commands.html"),
    ("Demonstration", "pilot-demo.html"),
    ("How we test", "testing.html"),
    ("Security", "security.html"),
    ("Attorney control", "responsibility.html"),
    ("Pilot", "pilot.html"),
    ("About", "about.html"),
]

HOME_VISUAL = """<figure class='product-visual matter-visual' role='img' aria-label='Fictional matter-preparation workspace showing attorney-supplied records, prepared material, and attorney review.' data-ui>
  <div class='ui-bar'><strong>Merit</strong><span>Fictional demonstration matter</span><b>Preparation</b></div>
  <div class='matter-board'>
    <section><h3>Attorney supplies</h3><p>Review instructions</p><p>Fictional records</p><p>Known dates</p></section>
    <section class='matter-focus'><h3>Merit prepares</h3><p>Research draft</p><p>Source list</p><p>Open questions</p></section>
    <section><h3>Attorney reviews</h3><p>Facts and sources</p><p>Dates and rules</p><p>Final document</p></section>
  </div>
  <figcaption>A fictional workspace view of one matter moving from supplied records to attorney review.</figcaption>
</figure>"""

TESTING_VISUAL = """<figure class='product-visual testing-scope-visual' role='img' aria-label='Testing-scope diagram showing approved positive citation-gate evidence and neutral limits on what the tests establish.' data-ui>
  <div class='ui-bar'><strong>Testing scope</strong><span>Dated checkpoints</span><b>Attorney review required</b></div>
  <div class='test-map'>
    <div class='test-evidence'>
      <article><time>September 29, 2026</time><strong>VM gate and five seat tests passed</strong><span>Specific citation-gate path</span></article>
      <article><time>September 29, 2026</time><strong>79 fresh-seat and 188 local tests passed</strong><span>Named gate and seat configuration</span></article>
      <article><time>October 17, 2026</time><strong>5 of 5 planted citation errors blocked</strong><span>Targeted probes</span></article>
    </div>
    <div class='test-limits'><h3>How to read the results</h3><p>Component and path specific</p><p>Citation checking remains separate</p><p>No broad legal or deadline accuracy claim</p><p>Sources and deadlines require attorney verification</p></div>
  </div>
  <figcaption>Positive observations remain tied to the named component, path, date, and sample.</figcaption>
</figure>"""

SECURITY_VISUAL = """<figure class='data-flow-visual' aria-labelledby='data-flow-title data-flow-caption'>
  <div class='data-flow-head'><span>Data flow</span><strong id='data-flow-title'>From matter records to attorney review</strong></div>
  <ol class='data-flow-list'>
    <li class='flow-step flow-attorney'><span class='flow-number'>1</span><div><strong>Attorney opens the matter</strong><p>The signed-in attorney chooses the matter and task.</p></div></li>
    <li class='flow-step flow-original'><span class='flow-number'>2</span><div><strong>Original file stays on the firm-dedicated environment</strong><p>The product does not upload the original file to a model provider.</p><span class='flow-tag'>Original file</span></div></li>
    <li class='flow-step flow-local'><span class='flow-number'>3</span><div><strong>Processing runs locally</strong><p>Text extraction, OCR, and optional local embeddings run on the assigned machine. Embeddings are off by default and are not persisted.</p><span class='flow-tag'>Local processing</span></div></li>
    <li class='flow-step flow-selected'><span class='flow-number'>4</span><div><strong>Selected text may go to a configured cloud model</strong><p>The task may include selected text, document titles, and document-type labels. The file itself is not sent.</p><span class='flow-tag'>Selected text, not the file</span></div></li>
    <li class='flow-step flow-return'><span class='flow-number'>5</span><div><strong>A draft returns for attorney review</strong><p>The attorney checks the facts, sources, analysis, dates, and document.</p></div></li>
    <li class='flow-step flow-manual'><span class='flow-number'>6</span><div><strong>The attorney takes any external action</strong><p>Sending, filing, serving, and submitting remain manual.</p><span class='flow-tag'>Attorney controlled</span></div></li>
  </ol>
  <figcaption id='data-flow-caption'>The original file and selected text follow different paths. Only selected text and the current title and document-type fields may be sent for model processing.</figcaption>
</figure>"""

pages = {
"index.html": {
"title":"Merit AI Solutions | AI-assisted matter preparation for Minnesota attorneys",
"desc":"Merit helps Minnesota solo and small-firm attorneys prepare research, drafts, matter records, filing documents, and proposed deadlines for attorney review.",
"kicker":"AI-assisted matter preparation for Minnesota attorneys",
"h1":"Prepare work for review",
"lead":"Merit AI Solutions is an AI Legal Associate for Minnesota solo attorneys and firms with 2–6 attorneys. It is an AI-assisted preparation system. It is not a lawyer, employee, or substitute for attorney judgment.",
"mark":"REVIEW",
"sections":[
("Start with one matter", "split", "<p class='statement'>Provide the records and instructions for one task. Merit prepares the material. The attorney checks every authority, fact, date, and document before deciding what to use.</p><a class='text-link' href='capabilities.html'>See the work and limits</a>"+HOME_VISUAL),
("Five ways Merit can help", "workflow-list", "".join(f"<article><h3>{a}</h3><p>{b}</p></article>" for a,b in [
("Research with sources","Merit prepares a research draft with sources for the attorney to open, check, and evaluate."),
("Draft preparation","Merit prepares a draft from attorney-provided records and instructions and returns it for attorney revision."),
("Intake organization","Merit organizes parties, dates, documents, and open questions for attorney review."),
("Filing-document preparation","Merit prepares court-filing documents for review. The attorney submits them manually."),
("Proposed deadlines","Merit prepares a proposed calculation. The attorney independently verifies every deadline."),])),
("The attorney decides what leaves", "dark", "<p class='statement'>Merit prepares material for review. The attorney remains responsible for the representation and manually files, sends, serves, or submits final work.</p><a class='button button-light' href='responsibility.html'>Read about attorney control</a>"),
("Dated evidence from focused tests", "evidence", "<div class='fact'><strong>Sep. 29, 2026</strong><span>Standalone citation-gate behavior was reproduced on the VM.</span></div><div class='fact'><strong>79 + 188</strong><span>Fresh-seat gate and citation tests passed, along with the local test set.</span></div><div class='fact'><strong>5 of 5</strong><span>Planted citation errors were blocked in targeted probes on October 17, 2026.</span></div><p>These are component- and path-specific results. They do not establish broad legal accuracy, deadline accuracy, or client outcomes.</p><a class='text-link' href='testing.html'>Read the dated testing record</a>"),
("A pilot for a defined workflow", "offset", "<p>The first three attorneys may receive one pilot month at no charge. Eligibility and fit are confirmed during the discovery call. No post-pilot pricing or fixed setup time is stated here.</p><a class='text-link' href='pilot.html'>Discuss the pilot</a>"),
("Built by Dr. Raymond Diaz", "split", "<p>Dr. Raymond Diaz, Founder, is a Minnesota resident with a background in education, curriculum development, and building carefully reviewed professional systems.</p><a class='text-link' href='about.html'>About Merit AI Solutions</a>"),
("Bring one workflow", "gold", "<p class='statement'>Choose research, drafting, intake organization, filing-document preparation, or a proposed deadline calculation. The call focuses on that task and its review steps.</p><a class='button' href='https://tidycal.com/drdiaz/discovery-call'>Book a 30-minute discovery call</a>"),
] },
"capabilities.html": {
"title":"Work and limits | Merit AI Solutions","desc":"See what Merit can prepare, what an attorney must provide, and what remains the attorney’s responsibility.","kicker":"Work and limits","h1":"Work Merit can prepare","lead":"Each workflow begins with attorney instructions and matter records. Each output returns to the attorney for review.","mark":"SCOPE",
"sections":[
("The review boundary", "process", "<ol><li><b>Attorney input</b><span>Instructions, facts, records, and governing material.</span></li><li><b>Merit preparation</b><span>A bounded draft, organization, or proposed calculation.</span></li><li><b>Attorney review</b><span>Check facts, sources, law, calculations, and form.</span></li><li><b>Manual action</b><span>The attorney files, sends, serves, or submits.</span></li></ol>"),
("Five workflows and review steps", "table", "<div class='records'>"+"".join(f"<article><h3>{w}</h3><dl><div><dt>Attorney supplies</dt><dd>{i}</dd></div><div><dt>Merit prepares</dt><dd>{o}</dd></div><div><dt>Attorney reviews or does</dt><dd>{r}</dd></div></dl></article>" for w,i,o,r in [
("Legal research with sources","The attorney provides the question, jurisdiction, facts, and controlling records.","Merit prepares a research draft with sources.","Open every source. Confirm its existence, currency, support, and application."),
("Draft preparation","The attorney provides the task, audience, records, position, and drafting instructions.","Merit prepares a draft from the supplied records and instructions.","Check it against the record and law. Revise it and decide whether to use it."),
("Matter intake and organization","Intake information and matter records.","Parties, dates, documents, and open questions.","Correct errors, supply missing facts, and maintain the official file."),
("Court-filing document preparation","Intended filing, court information, records, and approved form.","A court-filing document for review.","Review, correct, sign when appropriate, and submit manually."),
("Proposed deadline calculations","The attorney provides the trigger, dates, rule or order, court, and known exceptions.","Merit prepares a proposed calculation that identifies the inputs used.","Calculate the deadline independently. Check the rules, orders, holidays, service, and exceptions."),])+"</div>"),
("What these tests do and do not show", "dark", "<p class='statement'>The public test evidence applies only to the components and paths described on the testing page. Attorneys must still calculate and verify proposed deadlines independently. Merit makes no broad deadline-accuracy claim.</p>"),
("Outside the current scope", "split", "<p>The five workflows do not include discovery or billable-time records. Merit does not give legal advice, exercise professional judgment, file or serve documents, make final legal decisions, or replace firm personnel.</p><p>Merit may fit a firm that has time to supervise the work. It is not suitable where the attorney cannot independently review facts, law, citations, calculations, and the final document.</p>"),
("Evaluate one workflow", "gold", "<p>Bring one workflow. The demonstration will show the preparation and review steps for that task.</p><a class='button' href='https://tidycal.com/drdiaz/discovery-call'>Book a personalized demonstration</a>"),] },
"commands.html": {
"title":"Attorney commands | Merit AI Solutions","desc":"See representative plain-English commands attorneys could use for matter preparation, with review and action boundaries stated clearly.","kicker":"Attorney commands","h1":"Ask for the work in plain English","lead":"Commands describe a task in ordinary language and prepare requested work for attorney review. Every external action remains manual.","mark":"ASK",
"sections":[
("Four representative requests", "favorites", "<ol class='favorite-list'><li>“Prepare the filing materials and identify what remains for attorney review.”</li><li>“Draft the communication for attorney review.”</li><li>“Calculate the deadline and show the complete rule-and-date analysis.”</li><li>“Identify what additional current-law research is required.”</li></ol>"),
("How commands work", "process", "<ol><li><b>Choose the matter</b><span>Work stays tied to the matter the attorney intentionally opens.</span></li><li><b>State one task</b><span>Use a plain-English request. Provide the available facts, records, dates, and instructions.</span></li><li><b>Review the draft</b><span>Check every fact, authority, citation, date, calculation, and document before use.</span></li><li><b>Take any external action manually</b><span>The attorney sends, files, signs, serves, mails, or submits. The command does not.</span></li></ol>"),
("Representative commands", "commands", "<p>This page shows representative requests. Availability is confirmed for the selected workflow, and every result remains subject to attorney review.</p><div class='command-grid'>"+"".join(f"<article><h3>{escape(category)}</h3><ul>{''.join(f'<li>{escape(command)}</li>' for command in commands)}</ul></article>" for category,commands in [
("Matter summary",["Summarize the current matter record and list open questions.","Prepare a concise status summary for attorney review."]),
("Research",["Research the stated issue and identify sources for attorney review.","Identify what additional current-law research is required."]),
("Statutes and rules",["Locate the governing statute or rule and quote the relevant text.","Compare the supplied rule text with the matter facts."]),
("Citation checking",["Check whether each citation exists and supports the stated proposition.","List citations that still require attorney review for currency or treatment."]),
("Facts and chronology",["Build a chronology from the supplied matter records.","Separate supported facts, disputed facts, and missing facts."]),
("Document review",["Summarize this document and identify provisions requiring attorney attention.","Compare these documents and list material differences."]),
("Drafting",["Draft the communication for attorney review.","Prepare a draft from the supplied records and instructions."]),

("Preparation",["Prepare an attorney review checklist for the upcoming event.","Organize the supplied materials into a preparation outline."]),
("Matter maintenance",["List incomplete matter information and records that require attention.","Prepare a matter-status update from the current record."]),
("Deadlines and tasks",["Calculate the deadline and show the complete rule-and-date analysis.","Prepare an internal task list and identify which dates require verification."]),
("Filing and forms",["Prepare the filing materials and identify what remains for attorney review.","Populate the supplied form with known matter information and leave unknowns blank."]),
])+"</div>"),
("Command boundaries", "dark", "<ul class='checklist boundary-list'><li>No emailing, mailing, or sending.</li><li>No filing, signing, serving, or submitting.</li><li>Every deadline requires independent attorney verification.</li><li>Citation retrieval or checking is not a complete citator, current-validity, or subsequent-history result.</li><li>Missing facts remain missing; the system must not invent them.</li><li>Internal tasks or calendars do not prove an entry exists in an external calendar.</li><li>Every output remains a draft until attorney review.</li></ul>"),
("Review one command", "gold", "<p>Bring one task and the records needed to understand it. The demonstration can show the preparation and attorney-review boundary while keeping every external action manual.</p><a class='button' href='https://tidycal.com/drdiaz/discovery-call'>Book a personalized demonstration</a>"),] },
"pilot-demo.html": {
"title":"Demonstration workflow | Merit AI Solutions","desc":"See how a Merit demonstration moves from fictional inputs to attorney review.","kicker":"Demonstration workflow","h1":"Preparation to attorney review","lead":"This page explains the demonstration process. It does not present a completed sample matter or downloadable artifacts. Any public demonstration must use fictional information.","mark":"DEMO",
"sections":[
("Choose one workflow", "choice", "<div class='choice-grid'>"+"".join(f"<button type='button' data-choice='{escape(x)}'>{escape(x)}</button>" for x in ["Research preparation","Draft from supplied records","Intake organization","Filing-document preparation","Proposed deadline calculation"])+"</div><p id='choice-output' class='choice-output' aria-live='polite'>Select a workflow to see the review sequence emphasized.</p>"),
("Review the fictional inputs", "split", "<p>The demonstration identifies the records and instructions Merit would receive. The attorney sees which facts are supplied, which remain open, and which task Merit has been asked to prepare.</p><div class='boundary-note'>Demonstrations use fictional information. Do not submit client material for a demonstration.</div>"),
("Examine the prepared material", "offset", "<p>Research includes sources. Drafts identify supplied records. Proposed dates show the stated trigger and rule. Filing documents stop before any external submission.</p>"),
("Apply the attorney checks", "dark", "<p class='statement'>Compare facts with the record. Open and evaluate sources. Recalculate proposed deadlines. Revise drafts. Decide whether anything is suitable for use.</p><p>Citation checking remains separate from drafting unless the demonstration expressly states that the separate check ran.</p><a class='button button-light' href='testing.html'>Read the dated testing record</a>"),
("Choose a workflow for the call", "gold", "<p>The personalized demonstration covers one workflow selected during booking and shows its preparation and attorney-review steps.</p><a class='button' href='https://tidycal.com/drdiaz/discovery-call'>Book a 30-minute discovery call</a>"),] },
"testing.html": {
"title":"How we test | Merit AI Solutions","desc":"Read dated Merit test results, sample sizes, tested scope, and attorney-review limits.","kicker":"How we test","h1":"Dated results, with the tested scope visible","lead":"The September 29 and October 17, 2026 checkpoints tested specific citation-gate components and paths. The results below preserve their sample sizes and do not become a general accuracy promise.","mark":"TEST",
"sections":[
("Evidence at a glance", "table", "<div class='records compact triad'><article><h3>Standalone gate on the VM</h3><p><b>September 29, 2026.</b> A fabricated citation was blocked, an unsupported real citation was semantically blocked, and a supported real citation passed. Five seat tests passed.</p></article><article><h3>Fresh-seat test sets</h3><p><b>September 29, 2026.</b> A fresh-seat run passed 79 gate and citation tests. The local test set passed 188 tests.</p></article><article><h3>Targeted citation probes</h3><p><b>October 17, 2026.</b> The semantic reviewer blocked five of five planted citation errors in targeted probes.</p></article></div>"+TESTING_VISUAL),
("What the results support", "table", "<div class='records compact triad'><article><h3>Three-way gate behavior</h3><p>The standalone gate distinguished a fabricated citation, an unsupported real citation, and a supported real citation in the tested VM path.</p></article><article><h3>Reproducibility in the tested seat</h3><p>The fresh-seat and local suites support the tested gate and seat configuration for the September 29 checkpoint.</p></article><article><h3>Detection in targeted probes</h3><p>The five planted errors were blocked in the October 17 probes. The sample is reported as a targeted result, not a universal rate.</p></article></div>"),
("Scope limits", "table", "<div class='records compact triad'><article><h3>Component and path specific</h3><p>These results apply to the named gate, seat, and targeted probes. They do not establish broad legal accuracy, deadline accuracy, or client outcomes.</p></article><article><h3>Separate from drafting</h3><p>Citation checking is a separate step. Merit does not claim that every drafting or other workflow automatically runs the citation gate.</p></article><article><h3>Attorney verification remains required</h3><p>The attorney opens and evaluates sources, checks proposition support and application, independently verifies every proposed deadline, and decides what to use.</p></article></div>"),
("What each test report includes", "process", "<p>Each Merit test report identifies the details readers need to understand the result:</p><ul class='checklist'><li>Test date</li><li>Software revision or release</li><li>Number of test items and runs</li><li>Inputs and expected outcomes</li><li>Observed result for the stated test</li><li>Whether attorney-review time is included</li><li>Whether the test covers a component or a complete workflow</li><li>Current disposition only when a dated retest supports it</li></ul><p>A timing result appears with its corresponding correctness result. Merit is compared with manual work only when both conditions use a defined, comparable method.</p>"),
("What these tests do and do not show", "gold", "<p>The public results support only the components and paths named above. No claim is made here about monthly savings, every document type, complete source coverage, automatic citation checking in every workflow, broad legal or deadline accuracy, or client outcomes.</p><a class='button' href='https://tidycal.com/drdiaz/discovery-call'>Book a personalized demonstration</a>"),] },
"security.html": {
"title":"Security and data handling | Merit AI Solutions","desc":"See where original matter files stay, what text may be sent for model processing, and how access works.","kicker":"Security and data handling","h1":"Know where matter information goes","lead":"Merit separates the original client document from the text used for a task. This page explains that path and the current access controls.","mark":"DATA",
"sections":[
("Follow the data", "security-flow", SECURITY_VISUAL),
("What stays on the assigned environment", "table", "<div class='records compact security-records'><article><h3>Original client documents</h3><p>Original client documents are stored on infrastructure dedicated to the firm. Merit does not upload the original file to a model provider.</p></article><article><h3>Local document processing</h3><p>Text extraction and OCR run locally on the assigned machine. Optional embeddings also run locally. Embeddings are not persisted, and the feature is off by default.</p></article></div>"),
("What may be sent for model processing", "offset", "<p class='statement'>A configured cloud model may receive text selected for the task. Today, that text may also include document titles and document-type labels.</p><p>The provider receives text, not the original file. A title can contain identifying information, so firms should treat titles as part of the information that may leave the assigned environment.</p>"),
("Restricted runtime controls", "split", "<p>The configured Lodestar environment narrows what the approved cloud-model lane can do. Model calls run in a read-only execution sandbox with web search turned off. Only a limited set of environment fields is inherited, prompts are text-only, and local matter memory is blocked from remote calls.</p><p>These configured controls reduce exposure, but they do not establish provider no-training or zero retention, at-rest encryption, logged support access, deletion that includes backups, or absolute isolation.</p>"),
("Access and matter scope", "table", "<div class='records compact security-records'><article><h3>Access to the desk</h3><p>Access uses the firm’s Microsoft Entra tenant sign-in and a seat second factor. Connections use TLS through a single Cloudflare hostname.</p></article><article><h3>Matter storage</h3><p>Matter data is stored in per-seat, per-matter scopes. This describes the current storage structure and is not an absolute isolation guarantee.</p></article></div>"),
("Attorney-controlled actions", "dark", "<p class='statement'>Consequential external actions remain manual and require attorney review.</p><p>Merit returns work for review. The attorney decides whether to send, file, serve, or submit it and completes that action outside the preparation step.</p>"),
] },
"responsibility.html": {
"title":"Attorney control and review | Merit AI Solutions","desc":"Review the attorney’s role, workflow limits, certifications, and support terms.","kicker":"Attorney control and review","h1":"Attorney responsibility","lead":"Merit prepares material for review. The attorney evaluates the facts, sources, analysis, calculations, and final document. The attorney decides whether to use it.","mark":"CONTROL",
"sections":[
("Professional-duty considerations", "split", "<p>Minnesota attorneys evaluating AI-assisted preparation may need to consider duties involving competence, confidentiality, candor, and supervision.</p><p>Merit does not provide a compliance opinion or claim that use of the product satisfies those duties. Each attorney must evaluate the tool, matter, firm policies, and applicable requirements.</p>"),
("Legal sources and boundaries", "split", "<p>Research is prepared with identified sources for attorney review. The authorities that matter depend on the question, jurisdiction, facts, procedure, and current law. Attorneys must open, confirm, update, and evaluate every authority before relying on it.</p><p>When a Minnesota statute or rule is referenced, check the current official text through the <a class='text-link' href='https://www.revisor.mn.gov/'>Minnesota Revisor of Statutes</a>. No source list is represented as complete. Merit does not claim that using the AI Legal Associate automatically satisfies professional duties.</p>"),
("Review before use", "process", "<ul class='checklist'><li>Compare factual statements with the matter record</li><li>Read and update cited law</li><li>Confirm source support and application</li><li>Calculate deadlines independently</li><li>Revise every document as needed</li><li>Complete filing, service, delivery, and communication manually</li></ul>"),
("Workflow limits", "dark", "<p>Citation checking is separate from drafting and is not claimed on every workflow. A source check does not replace review of existence, currency, treatment, proposition support, or application.</p><p>Every proposed deadline requires independent attorney verification. Filing documents remain drafts until the attorney reviews and manually submits them.</p>"),
("Certifications and support", "split", "<div><h3>Certifications</h3><p>Merit does not hold SOC 2 or ISO 27001 certification. It may not fit firms that require either.</p></div><div><h3>Support</h3><p>Support requests are monitored. We agree on response expectations during onboarding. The website makes no 24/7 or response-time commitment.</p></div>"),
("Bring your review requirements", "gold", "<p>Bring the security, supervision, and workflow questions your firm needs answered before a pilot.</p><a class='button' href='https://tidycal.com/drdiaz/discovery-call'>Discuss your review requirements</a>"),] },
"pilot.html": {
"title":"Pilot Merit AI Solutions | Discovery call and personalized demonstration","desc":"Discuss a defined Merit pilot beginning with a 30-minute discovery call.","kicker":"Pilot","h1":"Test one defined workflow","lead":"The pilot begins with a 30-minute discovery call and personalized demonstration. Together, we identify the task, records, output, and attorney checks.","mark":"PILOT",
"sections":[
("Pilot offer", "evidence", "<div class='fact'><strong>First three</strong><span>The first three eligible attorneys may receive one pilot month at no charge.</span></div><div class='fact'><strong>One workflow</strong><span>Each pilot covers one defined workflow and its attorney review steps.</span></div><div class='fact'><strong>Schedule after review</strong><span>We set the schedule after reviewing the workflow.</span></div><p>Confirm availability and eligibility during the discovery call. This site does not state pricing after the pilot.</p>"),
("What the pilot may cover", "choice", "<ul class='option-list'><li>Legal research with sources</li><li>A draft from attorney-provided records</li><li>Matter intake and organization</li><li>Court-filing document preparation</li><li>A proposed deadline calculation</li></ul>"),
("Before the pilot starts", "split", "<p>The discovery call and workflow review determine whether the task fits the current service. They also identify requirements for confidentiality, access, records, review, and support.</p><p>Use only fictional information in demonstrations. Any later use of client information requires separately documented approval and review.</p>"),
("During the pilot", "dark", "<p class='statement'>Merit prepares the agreed material. The attorney checks it and decides whether it can be used.</p><p>Citation checking is separate from drafting. Proposed deadlines require independent verification. The attorney manually files, sends, serves, or submits final work.</p>"),
("Measure the defined review work", "questions", "<ul class='question-list'><li>Did the output reflect the supplied records?</li><li>Were open or uncertain facts easy to identify?</li><li>Could the attorney trace research statements to sources?</li><li>How much attorney review and revision did the task require?</li><li>Did the workflow fit the firm’s supervision process?</li></ul>"),
("Book the discovery call", "gold", "<p>Select one workflow. The call focuses on that task, its review boundary, and the information needed to decide whether a pilot fits.</p><a class='button' href='https://tidycal.com/drdiaz/discovery-call'>Book a 30-minute discovery call</a>"),] },
"about.html": {
"title":"About Merit AI Solutions","desc":"Learn about Merit AI Solutions, its AI-assisted matter-preparation work, and founder Dr. Raymond Diaz.","kicker":"About","h1":"About Merit AI Solutions","lead":"Merit develops AI-assisted matter preparation for Minnesota solo attorneys and firms with 2–6 attorneys. Its AI Legal Associate is not a lawyer, employee, or substitute for attorney judgment.","mark":"MERIT",
"sections":[
("What Merit prepares", "split", "<p>Merit prepares research with sources and drafts from attorney-provided records. It also organizes matter intake, prepares court-filing documents, and proposes deadline calculations.</p><p>The attorney reviews every output. Filing, service, submission, and final legal decisions remain with the attorney.</p>"),
("Dr. Raymond Diaz, Founder", "founder", "<p class='founder-statement'>Dr. Raymond Diaz is a Minnesota resident with a background in education, curriculum development, and building carefully reviewed professional systems.</p><p>As founder, Dr. Raymond Diaz is responsible for Merit’s direction and review standards.</p>"),
("Evidence with visible scope", "dark", "<p class='statement'>Merit publishes dated positive test observations with sample sizes and limits. The results stay tied to the component or path that was tested.</p><p>The current public record includes the September 29 VM and fresh-seat citation-gate results and the October 17 five-item targeted probe result.</p><a class='button button-light' href='testing.html'>Read how we test</a>"),
("Discuss one workflow", "gold", "<p>The discovery call lasts 30 minutes and includes a personalized demonstration of one selected workflow.</p><a class='button' href='https://tidycal.com/drdiaz/discovery-call'>Book a 30-minute discovery call</a>"),] },
}

def nav_html(current):
    links=[]
    for label,href in NAV:
        active = " aria-current='page'" if href == current else ""
        links.append(f"<a href='{href}'{active}>{label}</a>")
    return ''.join(links)

def section_html(i, title, kind, body):
    return f"<section class='section section-{kind}' data-reveal><div class='section-inner'><div class='section-heading'><h2>{escape(title)}</h2></div><div class='section-body'>{body}</div></div></section>"

def render(filename, p):
    sections = ''.join(section_html(i,*s) for i,s in enumerate(p['sections']))
    review_strip = """<section class='review-strip' aria-label='Merit review boundary'>
      <figure><img src='assets/review/attorney-input.png' alt='Attorney input: records and instructions' width='1200' height='900'><figcaption>Attorney input</figcaption></figure>
      <figure><img src='assets/review/merit-prepares.png' alt='Merit prepares material for review' width='1200' height='900'><figcaption>Merit prepares</figcaption></figure>
      <figure><img src='assets/review/attorney-reviews.png' alt='Attorney reviews facts, law, and dates' width='1200' height='900'><figcaption>Attorney reviews</figcaption></figure>
      <figure><img src='assets/review/attorney-acts.png' alt='Attorney completes any manual submission' width='1200' height='900'><figcaption>Attorney acts</figcaption></figure>
    </section>"""
    page_class = f"page-{Path(filename).stem}"
    canonical = "https://meritailegalsolutions.com/" if filename == "index.html" else f"https://meritailegalsolutions.com/{filename}"
    return f"""<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>{escape(p['title'])}</title><meta name='description' content='{escape(p['desc'], quote=True)}'><link rel='canonical' href='{canonical}'><link rel='stylesheet' href='assets/site.css'><script>document.documentElement.classList.add('js')</script></head><body id='top' class='{page_class}'>
<a class='skip-link' href='#main'>Skip to content</a>
<header class='site-header'><a class='brand' href='index.html' aria-label='Merit AI Solutions home'><span>Merit</span><small>AI Solutions</small></a><button class='menu-toggle' type='button' aria-expanded='false' aria-controls='site-nav'>Menu</button><nav id='site-nav' class='site-nav' aria-label='Primary'>{nav_html(filename)}<a class='nav-cta' href='https://tidycal.com/drdiaz/discovery-call'>Book a call</a></nav></header>
<main id='main'><header class='hero'><div class='hero-copy'><h1>{escape(p['h1'])}</h1><p class='hero-lead'>{escape(p['lead'])}</p><div class='hero-actions'><a class='button button-gold' href='https://tidycal.com/drdiaz/discovery-call'>Book a 30-minute discovery call</a><a class='text-link' href='capabilities.html'>See the work and limits</a></div></div><div class='hero-mark' aria-hidden='true'><span>{escape(p['mark'])}</span><b>Attorney review required</b></div></header>{review_strip}{sections}</main>
<footer class='site-footer'><div class='footer-name'>Merit</div><div class='footer-grid'><div><h2>Merit AI Solutions</h2><p>AI-assisted matter preparation for Minnesota solo attorneys and firms with 2–6 attorneys.</p></div><nav aria-label='Footer'>{nav_html(filename)}</nav><div><p>Merit is not a law firm and does not provide legal advice. Attorneys review every output and manually file, send, serve, or submit final work.</p><p>Use of this website does not create an attorney-client relationship.</p></div></div><p class='copyright'>© Merit AI Solutions.</p></footer><script src='assets/site.js' defer></script></body></html>"""

(ROOT/'assets').mkdir(parents=True, exist_ok=True)
for filename, data in pages.items():
    (ROOT/filename).write_text(render(filename,data), encoding='utf-8')

REDIRECTS = {
    "ai-legal-associate-minnesota.html": "index.html",
    "hire-a-paralegal-minnesota.html": "capabilities.html",
    "virtual-paralegal-minnesota.html": "capabilities.html",
    "compliance.html": "responsibility.html",
    "orchestration.html": "commands.html",
    "proof.html": "testing.html",
    "systems.html": "security.html",
    "vs-general-ai.html": "capabilities.html",
    "vs-legal-ai.html": "capabilities.html",
    "work-time.html": "capabilities.html",
}

def render_redirect(source, target):
    target_url = "https://meritailegalsolutions.com/" if target == "index.html" else f"https://meritailegalsolutions.com/{target}"
    return f"""<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>Page moved | Merit AI Solutions</title><meta name='robots' content='noindex,follow'><link rel='canonical' href='{target_url}'><meta http-equiv='refresh' content='0; url={target}'></head><body><main><h1>This page has moved</h1><p><a href='{target}'>Continue to the current page</a>.</p></main></body></html>"""

for source, target in REDIRECTS.items():
    (ROOT/source).write_text(render_redirect(source, target), encoding='utf-8')

canonical_routes = ["index.html", "capabilities.html", "commands.html", "pilot-demo.html", "testing.html", "security.html", "responsibility.html", "pilot.html", "about.html"]
sitemap_urls = ["https://meritailegalsolutions.com/" if name == "index.html" else f"https://meritailegalsolutions.com/{name}" for name in canonical_routes]
(ROOT / "sitemap.xml").write_text("<?xml version='1.0' encoding='UTF-8'?>\n<urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>\n" + "".join(f"  <url><loc>{url}</loc></url>\n" for url in sitemap_urls) + "</urlset>\n", encoding="utf-8")
(ROOT / "robots.txt").write_text("User-agent: *\nAllow: /\n\nSitemap: https://meritailegalsolutions.com/sitemap.xml\n", encoding="utf-8")
print(f"Built {len(pages)} canonical pages and {len(REDIRECTS)} compatibility redirects")
