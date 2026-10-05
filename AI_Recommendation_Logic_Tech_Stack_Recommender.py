import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

career_data = [
    {
        "role": "Data Scientist",
        "skills": [
            "Python",
            "SQL",
            "Machine Learning",
            "Statistics",
            "Pandas",
            "NumPy",
            "Data Analysis",
            "Data Visualization"
        ]
    },
    {
        "role": "Machine Learning Engineer",
        "skills": [
            "Python",
            "Machine Learning",
            "Deep Learning",
            "TensorFlow",
            "Scikit-learn",
            "NumPy",
            "Pandas",
            "Model Deployment"
        ]
    },
    {
        "role": "Data Analyst",
        "skills": [
            "Python",
            "SQL",
            "Excel",
            "Power BI",
            "Statistics",
            "Data Analysis",
            "Pandas",
            "Data Visualization"
        ]
    },
    {
        "role": "Backend Developer",
        "skills": [
            "Java",
            "Python",
            "SQL",
            "Spring Boot",
            "REST API",
            "Git",
            "Database",
            "Backend Development"
        ]
    },
    {
        "role": "Frontend Developer",
        "skills": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Git",
            "UI Design",
            "Web Development",
            "Frontend Development"
        ]
    },
    {
        "role": "Full Stack Developer",
        "skills": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Node.js",
            "SQL",
            "REST API",
            "Git"
        ]
    },
    {
        "role": "DevOps Engineer",
        "skills": [
            "AWS",
            "Docker",
            "Kubernetes",
            "Linux",
            "Git",
            "CI/CD",
            "Cloud Computing",
            "Automation"
        ]
    },
    {
        "role": "Cloud Architect",
        "skills": [
            "AWS",
            "Azure",
            "Cloud Computing",
            "Docker",
            "Kubernetes",
            "Networking",
            "Infrastructure",
            "Security"
        ]
    },
    {
        "role": "Cybersecurity Analyst",
        "skills": [
            "Cybersecurity",
            "Linux",
            "Networking",
            "Python",
            "Ethical Hacking",
            "Security",
            "Cryptography",
            "Network Security"
        ]
    },
    {
        "role": "Software Engineer",
        "skills": [
            "Java",
            "Python",
            "C++",
            "Git",
            "Data Structures",
            "Algorithms",
            "SQL",
            "Software Development"
        ]
    },
    {
        "role": "AI Engineer",
        "skills": [
            "Python",
            "Artificial Intelligence",
            "Machine Learning",
            "Deep Learning",
            "NLP",
            "Computer Vision",
            "TensorFlow",
            "PyTorch"
        ]
    },
    {
        "role": "NLP Engineer",
        "skills": [
            "Python",
            "NLP",
            "Natural Language Processing",
            "Machine Learning",
            "Deep Learning",
            "Transformers",
            "PyTorch"
        ]
    },
    {
        "role": "Computer Vision Engineer",
        "skills": [
            "Python",
            "Computer Vision",
            "OpenCV",
            "Deep Learning",
            "Machine Learning",
            "TensorFlow",
            "PyTorch"
        ]
    }
]
df = pd.DataFrame(career_data)

df["skill_text"] = df["skills"].apply(
    lambda skills: " ".join(skills)
)
skill_aliases = {
    "ml": "machine learning",
    "ai": "artificial intelligence",
    "dl": "deep learning",
    "nlp": "natural language processing",
    "cv": "computer vision",
    "js": "javascript",
    "reactjs": "react",
    "nodejs": "node.js",
    "sklearn": "scikit-learn",
    "scikit learn": "scikit-learn",
    "powerbi": "power bi",
    "k8s": "kubernetes",
    "cicd": "ci cd",
    "frontend": "frontend development",
    "backend": "backend development"
}
def normalize_skill(skill):

    skill = skill.strip().lower()

   
    skill = " ".join(skill.split())

   
    if skill in skill_aliases:
        return skill_aliases[skill]

    compact_skill = skill.replace(" ", "")

    if compact_skill in skill_aliases:
        return skill_aliases[compact_skill]

    return skill

def display_header():

    print("\n" + "=" * 64)

    print("              AI RECOMMENDATION LOGIC")

    print("               TECH STACK RECOMMENDER")

    print("=" * 64)

    print("              DecodeLabs - Project 3")

    print("=" * 64)

def display_career_paths():

    print("\nAvailable Career Paths:")

    print("-" * 64)

    for number, role in enumerate(
        df["role"],
        start=1
    ):
        print(f"{number:2}. {role}")

def get_user_skills():

    print("\n" + "-" * 64)

    print("ENTER YOUR SKILLS")

    print("-" * 64)

    print("Enter at least 3 skills separated by commas.")

    print("\nExample:")

    print("Python, Machine Learning, TensorFlow")

    print("\nType 'q' to exit.")

    user_input = input("\nEnter your skills: ").strip()

    if user_input.lower() == "q":
        return None

    if not user_input:

        print("\nERROR: No skills were entered.")

        return []

    raw_skills = user_input.split(",")
    user_skills = []

    for skill in raw_skills:

        normalized = normalize_skill(skill)

        if normalized and normalized not in user_skills:

            user_skills.append(normalized)

    if len(user_skills) < 3:

        print("\nERROR: Please enter at least 3 different skills.")

        return []

    return user_skills

def display_user_profile(user_skills):

    print("\n" + "=" * 64)

    print("YOUR USER PROFILE")

    print("=" * 64)

    for skill in user_skills:

        print(f"✓ {skill.title()}")

def generate_recommendations(user_skills):

    user_profile = " ".join(user_skills)

    documents = [
        user_profile
    ] + df["skill_text"].tolist()

    vectorizer = TfidfVectorizer(
        lowercase=True,
        ngram_range=(1, 2)
    )

    tfidf_matrix = vectorizer.fit_transform(
        documents
    )
    user_vector = tfidf_matrix[0]

    career_vectors = tfidf_matrix[1:]

    similarity_scores = cosine_similarity(
        user_vector,
        career_vectors
    )[0]

    results = df.copy()

    results["similarity_score"] = similarity_scores

    results["match_percentage"] = (
        results["similarity_score"] * 100
    )

    results = results.sort_values(
        by="similarity_score",
        ascending=False
    ).reset_index(drop=True)

    return results

def find_matched_skills(
    user_skills,
    career_skills
):
    matched_skills = []

    for user_skill in user_skills:

        user_words = set(
            user_skill.lower().split()
        )


        for career_skill in career_skills:

            career_words = set(
                career_skill.lower().split()
            )

            if user_skill.lower() == career_skill.lower():

                matched_skills.append(
                    career_skill
                )

                break

            if user_words.intersection(
                career_words
            ):

                matched_skills.append(
                    career_skill
                )

                break


    return matched_skills

def display_top_recommendations(
    results,
    user_skills
):

    top_3 = results.head(3)


    print("\n" + "=" * 64)

    print("             TOP 3 CAREER RECOMMENDATIONS")

    print("=" * 64)


    for rank, (_, row) in enumerate(
        top_3.iterrows(),
        start=1
    ):

        print(f"\n{rank}. {row['role']}")


        print(
            f"   Similarity Score: "
            f"{row['match_percentage']:.2f}%"
        )


        matched = find_matched_skills(
            user_skills,
            row["skills"]
        )

        if matched:

            print(
                "   Matched Skills: "
                + ", ".join(
                    skill.title()
                    for skill in matched
                )
            )

        print(
            "   Tech Stack: "
            + ", ".join(row["skills"])
        )

        print("-" * 64)

def display_complete_ranking(results):

    print("\n" + "=" * 64)

    print("                  COMPLETE RANKING")

    print("=" * 64)


    for rank, (_, row) in enumerate(
        results.iterrows(),
        start=1
    ):

        print(
            f"{rank:2}. "
            f"{row['role']:<30}"
            f"{row['match_percentage']:>7.2f}%"
        )

def main():

    display_header()

    display_career_paths()

    while True:

        user_skills = get_user_skills()

        if user_skills is None:

            print("\n" + "=" * 64)

            print(
                "Thank you for using "
                "the AI Recommendation Logic System!"
            )

            print("=" * 64)

            break

        if len(user_skills) < 3:

            continue

        display_user_profile(
            user_skills
        )

        print("\n" + "-" * 64)

        print("PROCESSING RECOMMENDATIONS...")

        print("-" * 64)

        print("1. Ingesting user skill profile...")

        print("2. Creating TF-IDF vectors...")

        print("3. Calculating Cosine Similarity...")

        print("4. Scoring career profiles...")

        print("5. Sorting recommendations...")

        print("6. Filtering Top 3 results...")

        results = generate_recommendations(
            user_skills
        )

        display_top_recommendations(
            results,
            user_skills
        )

        show_ranking = input(
            "\nWould you like to see the complete ranking? (Y/N): "
        ).strip().lower()

        if show_ranking == "y":

            display_complete_ranking(
                results
            )

        print("\n" + "-" * 64)

        again = input(
            "Would you like to try another skill profile? (Y/N): "
        ).strip().lower()


        if again != "y":

            print("\n" + "=" * 64)

            print(
                "       RECOMMENDATION PROCESS COMPLETED"
            )

            print("=" * 64)

            print(
                "\nThank you for using "
                "the AI Tech Stack Recommender!"
            )

            break

if __name__ == "__main__":

    main()