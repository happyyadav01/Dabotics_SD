class Bug:
    def __init__(self, bug_id, description, assigned_to):
        self.bug_id = bug_id
        self.description = description
        self.assigned_to = assigned_to
        self.priority = None
        self.tested = False
        self.fixed = False

class BugTracker:
    def __init__(self):
        self.bugs = {}
        self.counter = 1
    
    
    def log_bug(self, description, assigned_to):
        bug = Bug(self.counter, description, assigned_to)
        self.bugs[self.counter] = bug
        print(f"Bug #{self.counter} logged and assigned to {assigned_to}.")
        self.counter += 1

    
    def prioritize_bug(self, bug_id, priority):
        if bug_id in self.bugs:
            self.bugs[bug_id].priority = priority
            print(f"Bug #{bug_id} priority set to {priority}.")
        else:
            print(f"Bug #{bug_id} not found.")
    
    def test_bug(self, bug_id):
        if bug_id in self.bugs:
            self.bugs[bug_id].tested = True
            print(f"Bug #{bug_id} tested.")
        else:
            print(f"Bug #{bug_id} not found.")

    
    def deploy_fix(self, bug_id):
        if bug_id in self.bugs and self.bugs[bug_id].tested:
            self.bugs[bug_id].fixed = True
            print(f"Bug #{bug_id} fixed and deployed.")
        elif bug_id not in self.bugs:
            print(f"Bug #{bug_id} not found.")
        else:
            print(f"Bug #{bug_id} must be tested before deploying.")


tracker = BugTracker()
tracker.log_bug("Fix login issue", "Alice")
tracker.log_bug("Resolve crash on start", "Bob")

tracker.prioritize_bug(1, "High")
tracker.prioritize_bug(2, "Medium")

tracker.test_bug(1)
tracker.deploy_fix(1)

tracker.test_bug(2)
tracker.deploy_fix(2)
