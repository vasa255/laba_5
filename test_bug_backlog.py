"""
This module contains the Bug and Backlog classes for bug tracking.
"""
from datetime import datetime
from laba_5 import Bug, Backlog  # Update with your actual script filename


def test_backlog_add_bug():
    """Test the 'add_bug' method of the Backlog class.
    """
    backlog = Backlog()
    bug = Bug("UI glitch", "Minor", datetime(2023, 12, 1), "RESOLVED", "John")
    backlog.add_bug(bug)
    assert len(backlog.bugs) == 1


def test_backlog_filter_resolved_by_assignee():
    """Test the 'filter_resolved_by_assignee' method of the Backlog class.
    """
    backlog = Backlog()
    bug1 = Bug("UI glitch", "Minor", datetime(2023, 12, 1), "RESOLVED", "John")
    bug2 = Bug("Performance problem", "Major", datetime(2023, 12, 5), "RESOLVED", "Bob")
    backlog.add_bug(bug1)
    backlog.add_bug(bug2)
    resolved_bugs_bob = backlog.filter_resolved_by_assignee("Bob")
    assert len(resolved_bugs_bob) == 1
    assert resolved_bugs_bob[0].assignee == "Bob"


def test_backlog_sort_by_severity():
    """Test the 'sort_by_severity' method of the Backlog class.
    """
    backlog = Backlog()
    bug1 = Bug("UI glitch", "Minor", datetime(2023, 12, 1), "RESOLVED", "John")
    bug2 = Bug("Performance problem", "Major", datetime(2023, 12, 5), "RESOLVED", "Bob")
    backlog.add_bug(bug1)
    backlog.add_bug(bug2)
    sorted_bugs = backlog.sort_by_severity()
    assert sorted_bugs[0].severity == "Minor"
    assert sorted_bugs[1].severity == "Major"
