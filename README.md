# AUEB Exams API

## Domain model

### Model entities

| Model entity | Description |
| :----------- | :---------- |
| Exams (AUEB) | |
| Exams (API) | |
| Lectures | |
| Rooms | |
| Schedules | |
| Courses | |
| Professors | |
| ProfessorCourses | |
| Departments | |
| DepartmentCourses | |

### Diagram

![Domain model diagram](docs/diagrams/domain_model.png)

### API endpoints

Exam model endpoints

* /api/exams/
* /api/exams/?date=\<date\> : *date* is a "DDMMYYYY" string
* /api/exams/?department=\<department\> : *department* is a string
* /api/exams/?professor=\<professor\> : *professor* is a string
* /api/exams/?course=\<course\> : *course* is a string
* Plus all possible combinations of the above query parameters.

JWT token endpoints

## Issues & weaknesses
