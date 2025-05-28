# Introduction to Software Testing, Debugging, and Logging

## Introduction to Software Testing

Two main flavors:
1. Functional testing - used to ensure software behaves as expected.
2. Non-functional testing - used to ensure that software is usable, secure, performant, and so on.

Developer-centric testing:
1. Unit testing - validate the code inside an individual unit of code.
2. Integration testing - ensures that disparate units of code work well together.

Unit testing:
Most common form of testing by developers. The purpose of unit testing is to validate the code logic inside an individual unit of code. Can help to identify bugs, edge cases.

What is a unit?
1. A class or method could be a unit when using an object-oriented programming language.
2. A function could be a unit when using a functional programming language.
3. Some languages may use all of these concepts to represent a unit.
4. A unit could be something else entirely. 
5. It should represent the smallest practical piece of code.

Resource stand-in:
1. Stand-ins may be known as fakes, mocks, spies, etc., depending on the programming language and testing tools.
2. Using stand-ins keeps the focus on the unit being tested. No need for external resources or interactions.
3. Tests can be run more quickly as units do not need to wait on external resources.

Integration testing:
Attempt to verify that holistic application behaves as expected. This adds application overhead b/c of external connections. More focused on implementation details. Should use non-production systems.

Resource copy:
1. Some external resources may not be practical to use outside a production environment - e.g., a cloud-based service such as a managed database.
2. In these cases, the types of stand-in used for unit testing may also be used for integration testing.
3. A stand-in for integration testing may also be a separate application, an API, a service, etc.

Code coverage:
The percentage of lines that are executed from a collection of tests. May not need 100%, exact value depends on the application. 

**For software to be tested, it needs to include more modular code.**

### Takeaways
1. Unit testing validates code logic inside an individual unit of code.
2. Integration testing ensures disparate units of code work well together toward their shared purpose.
3. Code coverage describes the percentage of code executed when running a collection of tests.
4. Code coverage is a useful contextual metric to determine the overall value of the tests.

---

## Introduction to Software Debugging and Logging
Software bugs occur from a code defect such as unexpected behaviors and unwanted results.

Debugging:
1. Caveman debugging includes using print() to output to screen.
    - Error location
        - Helps find the last line of code that ran successfully before the error.
        - Useful because, in some cases, the line numbers may not be accurate.
    - Incorrect assumptions
        - Useful for quickly showing an entire data structure.
    - Note
        - Caveman debugging can clutter your code - best practice is to remove it before production.

2. Most languages include a debugger. Python includes [pdb](https://docs.python.org/3/library/pdb.html).
    - Debugging tools
        - Enable stepping through code line by line to inspect variables.
        - Exist as both terminal-based and GUI applications.
        - Have a learning curve, but if you spend your day writing code, the investment is worth it.

Logging:
- A common way to understand what's happening inside an application.
- Usually includes a timestamp, message, and log level.
- Private and PII should not be included in log entries.

### Takeaways
1. The purpose of debugging is to remove defects from software.
2. There are different debugging techniques including caveman debugging, which displays basic information on the command line.
3. The purpose of logging is to capture application messages to gain insights into how an application behaves.
4. The content of a log entry depends on the application and use cases.
5. Sensitive data should be kept out of logs.