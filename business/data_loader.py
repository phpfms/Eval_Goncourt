# -*- coding: utf-8 -*-

"""
Chargement d'un jeu de données initial en base de données.
"""

from bdd.initial_data import get_initial_data

from daos.address_dao import AddressDao
from daos.person_dao import PersonDao
from daos.student_dao import StudentDao
from daos.teacher_dao import TeacherDao
from daos.course_dao import CourseDao


class DataLoader:

    def __init__(self):
        self.address_dao = AddressDao()


    def load(self):
        """Charge les données initiales dans la BDD."""

        data = get_initial_data()

        # =========================
        # 1. ADRESSES
        # =========================

        for address in data["addresses"]:
            self.address_dao.create(address)

        # =========================
        # 2. PERSONNES + ÉTUDIANTS
        # =========================

        for student in data["students"]:
            self.person_dao.create(student)
            self.student_dao.create(student)

        # =========================
        # 3. PERSONNES + ENSEIGNANTS
        # =========================

        for teacher in data["teachers"]:
            self.person_dao.create(teacher)
            self.teacher_dao.create(teacher)

        # =========================
        # 4. COURS
        # =========================

        for course in data["courses"]:
            self.course_dao.create(course)

        # =========================
        # 5. INSCRIPTIONS
        # =========================

        # Les objets possèdent maintenant leurs identifiants BDD.
        # On peut donc enregistrer les relations étudiant/cours.

        for student in data["students"]:
            for course in student.courses_taken:
                # À remplacer par ton DAO de relation
                # student_course_dao.create(student, course)
                pass

        print("Données initiales chargées avec succès.")