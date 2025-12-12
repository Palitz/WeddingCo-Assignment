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