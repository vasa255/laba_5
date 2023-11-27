from datetime import datetime 
 
class Bug: 
    def __init__(self, description, severity, deadline, status="OPEN", assignee=None): 
        self.description = description 
        self.severity = severity 
        self.deadline = deadline 
        self.status = status 
        self.assignee = assignee 
    def __str__(self): 
        return f"Bug: {self.description}, Severity: {self.severity}, Deadline: {self.deadline}, Status: {self.status}, Assignee: {self.assignee}" 
 
class Backlog: 
    def __init__(self): 
        self.bugs = [] 
 
    def add_bug(self, bug): 
        self.bugs.append(bug) 
    def filter_resolved_by_assignee(self, assignee): 
        resolved_bugs = [bug for bug in self.bugs if bug.status == "RESOLVED" and bug.assignee == assignee] 
        return resolved_bugs 
 
    def sort_by_severity(self): 
        sorted_bugs = sorted(self.bugs, key=lambda bug: bug.severity, reverse=True) 
        return sorted_bugs 

bug1 = Bug("UI glitch", "Minor", datetime(2023, 12, 1), "RESOLVED", "John") 
bug2 = Bug("Database connection issue", "Critical", datetime(2023, 11, 15), "OPEN", "Alice") 
bug3 = Bug("Performance problem", "Major", datetime(2023, 12, 5), "RESOLVED", "Bob") 
bug4 = Bug("UI glitch", "Minor", datetime(2023, 12, 1), "RESOLVED", "John")
bug5 = Bug("Database connection issue", "Critical", datetime(2023, 11, 15), "OPEN", "Alice")
bug6 = Bug("Performance problem", "Major", datetime(2023, 12, 5), "RESOLVED", "Bob")
bug7 = Bug("Security vulnerability", "Critical", datetime(2023, 12, 10), "OPEN", "Charlie")
bug8 = Bug("Feature not working", "Major", datetime(2023, 11, 20), "RESOLVED", "David")
bug9 = Bug("Compatibility issue", "Minor", datetime(2023, 11, 25), "OPEN", "Eva")

backlog = Backlog() 
backlog.add_bug(bug1) 
backlog.add_bug(bug2) 
backlog.add_bug(bug3) 
backlog.add_bug(bug4) 
backlog.add_bug(bug5) 
backlog.add_bug(bug6) 
backlog.add_bug(bug7) 
backlog.add_bug(bug8) 
backlog.add_bug(bug9) 
 
resolved_bugs_bob = backlog.filter_resolved_by_assignee("Bob") 
for bug in resolved_bugs_bob: 
    print(bug) 
print("+++++++========")
sorted_bugs = backlog.sort_by_severity() 
for bug in sorted_bugs: 
    print(bug)