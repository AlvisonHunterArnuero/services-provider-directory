from main import app, db, Provider, Review

def seed_data():
    with app.app_context():
        # Clear existing data just in case
        db.drop_all()
        db.create_all()

        # Add dummy providers
        providers_data = [
    {
        "name": "Alvison Hunter",
        "trade": "Senior Web Developer",
        "phone": "+505 8863 8751",
        "email": "alvison@gmail.com",
        "photo_url": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?q=80&w=500&auto=format&fit=crop",  # generic dev portrait
        "location": "Jinotepe, Carazo, Nicaragua",
        "experience_years": 6,
        "is_verified": True,
        "starting_rate": 70.0,
        "bio": "Senior Frontend Engineer specializing in React, Next.js, TypeScript, and Python. Experienced in headless CMS, API integrations, and building scalable web applications for global brands."
    },
    {
        "name": "Guillermo Ernesto D. Medina",
        "trade": "Electronics Engineer",
        "phone": "",  # not public; could leave empty or omit
        "email": "",  # not public; could leave empty or omit
        "photo_url": "https://images.unsplash.com/photo-1677938438599-a55528c41b2c?q=80&w=500&auto=format&fit=crop",  # generic engineer
        "location": "Córdoba, Argentina",
        "experience_years": 5,
        "is_verified": True,
        "starting_rate": 80.0,
        "bio": "Electronics engineer with experience in industrial electronics, maintenance, and electrical installations. Works with complex systems and third‑party service coordination."
    },
    {
        "name": "Ernesto Gutierrez",
        "trade": "CTU Manager",
        "phone": "",
        "email": "",
        "photo_url": "https://images.unsplash.com/photo-1552664730-d307ca884978?q=80&w=500&auto=format&fit=crop",  # generic manager
        "location": "Bogotá, Colombia",
        "experience_years": 12,
        "is_verified": True,
        "starting_rate": 100.0,
        "bio": "CTU Manager focused on organizational transformation and infrastructure projects. Experienced in leading teams and partnerships that build large‑scale infrastructure with long‑term social impact."
    },
    {
        "name": "Gabriela Mercedes Arnuero Suazo",
        "trade": "Attorney & Legal Assistant",
        "phone": "",
        "email": "",
        "photo_url": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=500&auto=format&fit=crop",  # generic lawyer
        "location": "León, Nicaragua",
        "experience_years": 6,
        "is_verified": True,
        "starting_rate": 85.0,
        "bio": "Attorney and legal assistant working across Nicaragua and U.S. cases. Experienced in case coordination, documentation, and supporting clients through complex legal processes."
    },
    {
        "name": "Sharom A. M.",
        "trade": "Education Consultant",
        "phone": "",
        "email": "",
        "photo_url": "https://images.unsplash.com/photo-1600880292089-90a7e086ee0c?q=80&w=500&auto=format&fit=crop",  # generic education consultant
        "location": "Singapore",
        "experience_years": 7,
        "is_verified": True,
        "starting_rate": 95.0,
        "bio": "Education consultant helping institutions and students navigate academic pathways, curriculum development, and learning strategies through personalized consulting."
    },
    {
        "name": "Francisco Briceño Sánchez",
        "trade": "Software Engineer",
        "phone": "",
        "email": "",
        "photo_url": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=500&auto=format&fit=crop",  # generic dev
        "location": "Nicaragua",
        "experience_years": 4,
        "is_verified": True,
        "starting_rate": 65.0,
        "bio": "Software Engineer specializing in backend development with Java and related technologies. Passionate about building reliable and maintainable applications."
    },
    {
        "name": "Walter Marroquin",
        "trade": "Software Developer",
        "phone": "",
        "email": "",
        "photo_url": "https://images.unsplash.com/photo-1566492031773-4f4e44671857?q=80&w=500&auto=format&fit=crop",  # generic dev
        "location": "El Salvador",
        "experience_years": 5,
        "is_verified": True,
        "starting_rate": 75.0,
        "bio": "Software developer experienced with Angular, .NET, React, and Spring Boot. Builds scalable, user‑focused web and backend systems for diverse industries."
    },
    {
        "name": "Roberto Teixeira",
        "trade": "Full‑Stack Developer",
        "phone": "",
        "email": "",
        "photo_url": "https://images.unsplash.com/photo-1621905252507-b35492cc74b4?q=80&w=500&auto=format&fit=crop",  # generic coder
        "location": "Brazil",
        "experience_years": 8,
        "is_verified": True,
        "starting_rate": 90.0,
        "bio": "Full‑stack developer with strong experience in PHP, Laravel, MySQL, React, TypeScript, and Node.js. Builds end‑to‑end applications and modern web platforms."
    },
    {
        "name": "L. G. Díaz",
        "trade": "Engineering & Sourcing Leader",
        "phone": "",
        "email": "",
        "photo_url": "https://images.unsplash.com/photo-1542744173-05336fcc7ad4?q=80&w=500&auto=format&fit=crop",  # generic engineer leader
        "location": "Mexico",
        "experience_years": 22,
        "is_verified": True,
        "starting_rate": 120.0,
        "bio": "Executive engineering and strategic sourcing leader with over 20+ years in the household appliances industry. Focuses on P&L leadership and cost‑impact initiatives."
    },
    {
        "name": "João LFR",
        "trade": "Software Engineer",
        "phone": "",
        "email": "",
        "photo_url": "https://images.unsplash.com/photo-1621905252507-b35492cc74b4?q=80&w=500&auto=format&fit=crop",  # generic coder
        "location": "Brazil",
        "experience_years": 4,
        "is_verified": True,
        "starting_rate": 70.0,
        "bio": "Software engineer and mobile‑focused developer building web and mobile platforms that connect users with local service providers and home‑solutions marketplaces."
    }
]

        pro_objects = []
        for data in providers_data:
            pro = Provider(**data)
            db.session.add(pro)
            pro_objects.append(pro)

        db.session.commit()

        # Add some reviews
        reviews_data = [
            {"pro_id": pro_objects[0].id, "rating": 5, "comment": "Alvison was amazing! Very fast.", "ip_address": "127.0.0.1"},
            {"pro_id": pro_objects[0].id, "rating": 4, "comment": "Very professional, though a bit pricey.", "ip_address": "127.0.0.2"},
            {"pro_id": pro_objects[1].id, "rating": 5, "comment": "Excellent work by Guillermo.", "ip_address": "127.0.0.3"}
        ]

        for r_data in reviews_data:
            review = Review(**r_data)
            db.session.add(review)

        db.session.commit()
        print("Successfully seeded the database with providers and reviews!")

if __name__ == "__main__":
    seed_data()
