from pathlib import Path

import pytest
from bulmaio_jinja2.tutorial.steps.models import (
    StepsSidebarPanel
)
from bulmaio_jinja2.utils import load_yaml

sample = Path(__file__).parents[3] / 'bulmaio_jinja2' / 'sample'


@pytest.fixture
def context_no_steps_sidebar_panel():
    steps_sidebar_panel = StepsSidebarPanel()
    return dict(steps_sidebar_panel=steps_sidebar_panel)


@pytest.fixture
def context_steps_sidebar_panel():
    pages = load_yaml('pages', base_dir=sample)
    page = pages[6]
    entries = [
        dict(
            title=entry['title'],
            subtitle=entry['subtitle'],
            href=entry['href']
        )
        for entry in page['steps']['entries']
    ]
    steps_sidebar_panel = StepsSidebarPanel(entries=entries)
    return dict(steps_sidebar_panel=steps_sidebar_panel)


@pytest.mark.parametrize(
    'page',
    [['test_tutorial_steps_sidebar_panel.html',
      context_no_steps_sidebar_panel], ],
    indirect=True
)
def test_no_steps_sidebar_panel(page):
    sp = page.find_all('div', class_='bio-tutorial-steps-sidebar')
    assert 0 == len(sp)


@pytest.mark.parametrize(
    'page',
    [['test_tutorial_steps_sidebar_panel.html',
      context_steps_sidebar_panel], ],
    indirect=True
)
def test_steps_sidebar_panel(page):
    sp = page.find('div', class_='bio-tutorial-steps-sidebar')
    entries = sp.find_all('li', class_='steps-segment')
    assert 1 == len(entries)

    # Entry
    li = entries[0]
    assert 'is-active' not in li.attrs['class']
    a = li.find('a')
    assert '/tutorial_project_setup.html' == a.attrs['href']

