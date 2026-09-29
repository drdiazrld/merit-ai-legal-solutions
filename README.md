# Merit AI Legal Solutions — marketing site

Published at https://meritailegalsolutions.com/ (GitHub Pages, main / root).

Root `*.html` is the **published output**. `pages/` + `partials/` + `build.py` are the generator.

**Hazard:** the generator is behind the published output (last full build 2026-09-16; the published
pages carry the 2026-09-27 receipted claims and the 2026-09-28 copy rulings). Re-sync `pages/`
from the root HTML before running `build.py`, or the build will silently revert live claims.
