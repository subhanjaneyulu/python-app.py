Major Issues Identified
**Lack of Proper Folder Structure
All code was inside a single file (app.py), making it harder to manage and scale.

**Hardcoded Data & No Modularity
User data was directly stored and handled in one place, with no separation of concerns.

**No Error Handling or Input Validation
The app did not gracefully handle bad inputs or failed operations.

**No Use of Environment Variables
The port was hardcoded, which is not a best practice.



Changes Made and Why
**Separated Concerns
Separated routing, database logic, and main app logic into different files to make the project cleaner and maintainable.

**Added Error Handling
Included try-except blocks and validation to avoid app crashes and unexpected behavior.

**Dynamic Port Binding
Used os.environ.get("PORT", 5000) to make the app production-friendly.

**Improved Readability
Reformatted the code for better readability and maintainability.



Assumptions or Trade-offs

*Assumed SQLite as the default database for simplicity.

*Kept the database schema minimal and flat for demonstration purposes.

*Did not add user authentication tokens to keep the app simple.


What I Would Do With More Time
**Add unit tests for all routes and functions.

**Improve UI with a frontend framework (React or basic HTML templates).

**Implement authentication using JWT.

**Add pagination, search filters, and sorting for user data.

**Use SQLAlchemy ORM for more flexibility with databases. 



AI Assistant Usage
Tools Used: ChatGPT (OpenAI), GitHub Copilot (for suggestions only)

What I Used Them For:

Guidance on how to structure and refactor Flask app code.

Suggestions for improving readability and best practices.

Help writing clear documentation for the CHANGES.md file.

AI-Generated Code:

Some code snippets were suggested by ChatGPT but were carefully reviewed and modified to fit the context and requirements.

I rejected or rewrote parts that didn't match the logic or were too generic.





