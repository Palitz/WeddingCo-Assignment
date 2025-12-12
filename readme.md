Organization Management Service

A scalable, multi-tenant backend service designed to manage organizations and their dedicated data collections. Built with FastAPI (Python) and MongoDB (Async Motor driver).

Features

Multi-Tenancy: Implements a "Collection-per-Tenant" strategy. Creating an organization dynamically creates a dedicated MongoDB collection (`org_<name>`).
Authentication: Admin login with JWT (JSON Web Tokens) issuance.
Security: Passwords are hashed using `bcrypt`. Environment variables manage secrets.
Async Performance: Fully asynchronous database operations using `Motor`.
Modular Design: Clean separation of concerns (Routers, Services, Models, Core).

Tech Stack

Framework: FastAPI
Database: MongoDB (via Motor & Pydantic)
Auth: JWT (Python-Jose) + Passlib (Bcrypt)
Containerization: Docker & Docker Compose

Architecture

The system uses a Modular Monolith approach.
1. Master DB: Stores global metadata (Organization Name, Admin Email, Collection Reference).
2. Dynamic Collections: Each organization gets its own collection (e.g., `org_spacex`, `org_tesla`) to ensure data isolation.

Setup & Installation

Prerequisites
Docker & Docker Compose OR Local MongoDB
Python 3.10+
Everything mentioned in the requirements.txt file

Clone & Configure (run these commands on terminal)
git clone https://github.com/Palitz/WeddingCo-Assignment
cd backend-assignment
cp .env.example .env

Elaboration:
1. Executive Summary
This project successfully implements a Multi-Tenant Backend Service designed to manage organizations and their isolated data. The system handles dynamic database provisioning, secure authentication, and organization metadata management using a modular, asynchronous architecture.
2. Technical Stack
Framework: FastAPI (Python 3.10+) - Chosen for high performance and native async support.
Database: MongoDB - Chosen for flexible schema and rapid collection provisioning.
Driver: Motor (AsyncIOMotorClient) - Ensures non-blocking database operations.
Authentication: JWT (JSON Web Tokens) with passlib (Bcrypt) hashing.
Validation: Pydantic - Enforces strict data schemas for inputs and outputs.
Containerization: Docker & Docker Compose.
3. System Architecture
The system utilizes a Collection-per-Tenant strategy within a shared MongoDB cluster.
Master Data: Stored in a master_metadata collection. Holds organization names, admin credentials (hashed), and pointers to tenant collections.
Tenant Data: Upon organization creation, the system dynamically provisions a dedicated collection (e.g., org_spacex, org_tesla).
Benefit: This approach ensures logical data isolation and simplifies per-tenant backup/restore operations without the operational overhead of managing separate database instances for every client.
The application follows a Service-Repository pattern to separate concerns, satisfying the "Class-based design" requirement:
routers/: Handles HTTP requests and response codes.
services/: Contains business logic (e.g., uniqueness checks, collection creation).
core/: Manages configuration, database connections, and security utilities.
models/: Defines data structures (Pydantic schemas).
<img width="1862" height="887" alt="image" src="https://github.com/user-attachments/assets/56acbc5b-c9d9-4941-a69b-11f930a8652e" />
<img width="1853" height="883" alt="image" src="https://github.com/user-attachments/assets/8bd6342a-c1a5-46d1-a6eb-f41d96d7846a" />
<img width="1844" height="894" alt="image" src="https://github.com/user-attachments/assets/3c4bb784-d343-4eb0-b9ec-9a7d9f8307ca" />
<img width="1864" height="890" alt="image" src="https://github.com/user-attachments/assets/cb8d5672-eaea-4412-9386-df7673284c68" />



