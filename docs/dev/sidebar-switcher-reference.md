# Implementation Summary

## 1. What was built
A sidebar dropdown ("NIU Tools") was added to the site navigation that links out to the Neuroinformatics Unit's other project sites. This is visually similar to the project switcher found on panel.holoviz.org, but it was implemented as our own lightweight, vendored version rather than directly importing and depending on HoloViz's `nbsite` package.

## 2. Why we didn't just import nbsite
We tested importing `nbsite.shared_conf` directly in a local build. We found that `nbsite` overrides Sphinx's `html_theme`, forces HoloViz's CSS, heavily modifies the `html_theme_options`, and hardcodes source code links to resolve to `github.com/holoviz`. More importantly, because Python executes top-down, NIU's own `conf.py` naturally overwrites the variables `nbsite` sets up, erasing the sidebar switcher entirely unless heavily hacked. Vendoring the template proved to be much safer and avoids breaking the existing site.

## 3. How it's implemented
The implementation has three core components:
- **The Template:** `docs/source/_templates/niu-sidebar-dropdown.html`. This Jinja template renders the dropdown HTML. It iterates over a configuration dictionary to build the project list using the exact same Jinja pattern as the original HoloViz template.
- **The Context Hook:** In `docs/source/conf.py`, a setup hook (`add_niu_sidebar_dropdown_context`) is registered via `app.connect("html-page-context", ...)`. This hook injects the project list into the Jinja template context on every build.
- **The Configuration Dictionary:** The actual project list lives in `docs/source/conf.py` under the variable `niu_sidebar_dropdown`. It looks like this:
  ```python
  niu_sidebar_dropdown = {
      'dropdown_value': { 'href': 'https://neuroinformatics.dev/', 'text': 'NIU Tools' },
      'projects': {
          'brainglobe': {
              'text': 'BrainGlobe',          # The text shown in the dropdown
              'url': 'https://brainglobe.info/', # The destination URL
              'title': 'BrainGlobe...'       # Tooltip text shown on hover
          },
          # ...
      },
      'others': {}
  }
  ```
- **The Sidebar Registration:** In `docs/source/conf.py`, the template is explicitly prepended to the `html_sidebars` dictionary for `"**"`, `"blog/index"`, and `"blog/**"`. This ensures the dropdown merges with NIU's existing sidebar structure rather than replacing it.

## 4. How to update the project list
To add, remove, or edit a project link in the sidebar:
1. Open `docs/source/conf.py`.
2. Locate the `niu_sidebar_dropdown` dictionary.
3. Under the `projects` key, add or edit a dictionary block. Provide a simple key name (e.g., `'datashuttle'`), and specify the `text` (display name), `url` (link destination), and `title` (hover tooltip).
4. No HTML or template changes are required! Sphinx will automatically read the updated dictionary on the next build.

## 5. What's still placeholder / needs input
The current `niu_sidebar_dropdown` dictionary in `conf.py` contains **placeholder entries** (BrainGlobe, DataShuttle, and Movement). The exact, finalized list of NIU projects and URLs needs to be provided by the maintainer and updated in `conf.py` before this pull request can be merged.

## 6. How to test it locally
To test the implementation on your own machine:
1. Activate your virtual environment and install dependencies: `pip install -r docs/requirements.txt`.
2. Build the Sphinx docs: `make html` (on Mac/Linux) or `.\make.bat html` (on Windows) inside the `docs` directory.
3. Start a local server: `python -m http.server 8000 -d docs/build/html`.
4. Open your browser to `http://localhost:8000`. Verify that the "NIU Tools" dropdown appears in the left sidebar, the links work, hover tooltips appear, and the existing site theme remains unaffected.

---


```html
{% if hv_sidebar_dropdown %}
<div class="hv-sb-dd">
  <div class="btn-group">
    {% if 'href' in hv_sidebar_dropdown['dropdown_value'] %}
    <a href="{{ hv_sidebar_dropdown['dropdown_value']['href'] }}" class="btn hv-sb-dd-value" target="_blank">{{ hv_sidebar_dropdown['dropdown_value']['text'] }}<i class="fa fa-external-link hv-icon" aria-hidden="true"></i></a>
    {% else %}
    <span class="btn hv-sb-dd-value">{{ hv_sidebar_dropdown['dropdown_value']['text'] }}</span>
    {% endif %}
    <button type="button" class="btn dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false">
      <span class="visually-hidden"></span>
    </button>
    <ul class="dropdown-menu">
      {% for project_name, project_opts in hv_sidebar_dropdown['libraries'].items() %}
      {% if project_name | lower not in project | lower %}
        <li><a class="dropdown-item" href="{{ project_opts['url'] }}" target="_blank" title="{{ project_opts['title'] }}">{{ project_opts['text'] }}<i class="fa fa-external-link hv-icon" aria-hidden="true"></i></a></li>
      {% endif %}
      {% endfor %}
      {% if hv_sidebar_dropdown['others'] %}
      <li><hr class="dropdown-divider"></li>
      {% for project_name, project_opts in hv_sidebar_dropdown['others'].items() %}
      {% if project_name | lower not in project | lower %}
      <li><a class="dropdown-item" href="{{ project_opts['url'] }}" target="_blank" title="{{ project_opts['title'] }}">{{ project_opts['text'] }}<i class="fa fa-external-link hv-icon" aria-hidden="true"></i></a></li>
      {% endif %}
      {% endfor %}
      {% endif %}
    </ul>
  </div>
</div>
{% endif %}
```
