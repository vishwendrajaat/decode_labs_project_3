# AI Recommendation Logic — Tech Stack Recommender

## Decode Labs — Artificial Intelligence Internship | Project 3

An AI-powered **Tech Stack Recommender** built using Python and Machine Learning concepts. The system takes a user's technical skills as input and recommends the **Top 3 career paths** based on similarity between the user's skill profile and predefined career profiles.

---

## 📌 Project Overview

This project implements a simple **content-based recommendation system**.

The user provides their technical skills, and the system:

1. Accepts user skills as input
2. Normalizes common skill names and aliases
3. Converts skill profiles into numerical vectors using **TF-IDF**
4. Calculates similarity using **Cosine Similarity**
5. Scores available career paths
6. Sorts the career paths based on similarity
7. Displays the **Top 3 recommended career paths**

The project demonstrates the basic logic behind recommendation systems and personalization.

---

## 🎯 Objective

The main objective of this project is to build a recommendation system that can match a user's technical skills with suitable career paths using text similarity techniques.

---

## 🧠 Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity
- Content-Based Recommendation
- Command Line Interface (CLI)

---

## ⚙️ How It Works

The recommendation pipeline follows these steps:

```text
User Skills
     ↓
Skill Normalization
     ↓
User Skill Profile
     ↓
TF-IDF Vectorization
     ↓
Cosine Similarity
     ↓
Career Profile Scoring
     ↓
Sorting
     ↓
Top 3 Recommendations