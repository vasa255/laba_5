import pytest
from datetime import datetime
from laba_5 import Bug, Backlog  # Update with your actual script filename

def test_bug_str():
    bug = Bug("UI glitch", "Minor", datetime(2023, 12, 1), "RESOLVED", "John")
    assert str(bug) == "Bug: UI glitch, Severity: Minor, Deadline: 2023-12-01 00:00:00, Status: RESOLVED, Assignee: John"

def test_backlog_add_bug():
    backlog = Backlog()
    bug = Bug("UI glitch", "Minor", datetime(2023, 12, 1), "RESOLVED", "John")
    backlog.add_bug(bug)
    assert len(backlog.bugs) == 1

def test_backlog_filter_resolved_by_assignee():
    backlog = Backlog()
    bug1 = Bug("UI glitch", "Minor", datetime(2023, 12, 1), "RESOLVED", "John")
    bug2 = Bug("Performance problem", "Major", datetime(2023, 12, 5), "RESOLVED", "Bob")
    backlog.add_bug(bug1)
    backlog.add_bug(bug2)
    resolved_bugs_bob = backlog.filter_resolved_by_assignee("Bob")
    assert len(resolved_bugs_bob) == 1
    assert resolved_bugs_bob[0].assignee == "Bob"

def test_backlog_sort_by_severity():
    backlog = Backlog()
    bug1 = Bug("UI glitch", "Minor", datetime(2023, 12, 1), "RESOLVED", "John")
    bug2 = Bug("Performance problem", "Major", datetime(2023, 12, 5), "RESOLVED", "Bob")
    backlog.add_bug(bug1)
    backlog.add_bug(bug2)
    sorted_bugs = backlog.sort_by_severity()
    assert sorted_bugs[0].severity == "Major"
    assert sorted_bugs[1].severity == "Minor"

