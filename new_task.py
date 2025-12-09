import time


class Timer:
    def __enter__(self):
        self._enter_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._exit_time = time.time()


class Student:

    def __init__(self, name="Robert", age=18, semester=2, health="Good", grades={}):
        self.__name = name
        self.__age = age
        self.__semester = semester
        self.__health = health
        self.__grades = dict(grades)

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_semester(self):
        return self.__semester

    def get_health(self):
        return self.__health

    def get_grades(self):
        return dict(self.__grades)

    def aver_grade(self):
        if not self.__grades:
            return 0
        return sum(self.__grades.values()) / len(self.__grades)

    def __str__(self):
        print("<<< STUDENT INFO >>>\n")

        average = self.aver_grade()

        return (
            f"| Name: {self.__name} | "
            f"Age: {self.__age} | "
            f"Semester: {self.__semester} | "
            f"Health: {self.__health} |\n"
            f"| Grades: {self.__grades} |\n"
            f"| Average Grade: {average:.2f} |"
        )


class Group:

    def __init__(self, students={}):
        self.__students = dict(students)

    def get_students(self):
        return dict(self.__students)

    def display_ranking(self):
        if self.__students:
            # print("Група порожня. Рейтинг неможливий.")
            # return

            print("\n<<< Group Ranking >>>")

            sorted_items = sorted(
                self.__students.items(),
                key=lambda item: item[1],
                reverse=True,
            )

            for rank, item in enumerate(sorted_items, 1):
                name = item[0]
                score = item[1]
                print(f"  {rank}. {name:<15} - rating score: {score}")

    def add_student(self, name, score):
        if isinstance(score, (int, float)) and score >= 0:
            self.__students[name] = score
            print(
                f"Student '{name}' (Rating: {score}) has been added.")
        else:
            print("Error")

    def remove_student(self, name):
        if name in self.__students:
            del self.__students[name]
            print(f"Student '{name}' has been removed.")
        else:
            print(f"Student '{name}' not found in the group.")


def main():
    with Timer() as timer:

        student_grade = {
            "Calculus": 4,
            "Python": 5,
            "English": 3,
            "History": 5,
            "Economics": 4,
            "Web Development": 2,
            "Linear Algebra": 3
        }
    sudent1 = Student(grades=student_grade)
    print(sudent1)

    full_group = {
        "Mark": 92,
        "Bob": 85,
        "Matt": 78,
        "Tom": 92,
        "Ross": 99,
        "Carter": 65,
    }

    group1 = Group(students=full_group)
    group1.display_ranking()

    print("\n--- Applyed Changes ---")

    group1.add_student("John", 53)
    group1.remove_student("Carter")

    group1.display_ranking()

    # print("Starting timed operation...")
    # time.sleep(5.23)  # Simulate a task
    # print("Timed operation finished.")

    print(f"{timer._exit_time - timer._enter_time:.2f} seconds elapsed")


if __name__ == "__main__":
    main()
