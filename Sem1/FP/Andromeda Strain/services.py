class Service:
    def __init__(self, repo):
        self._repository = repo

    def get_people(self):
        return self._repository.get_people()

    def simulate_day(self):
        people = self.get_people()
        for i in range(len(people)):
            if people[i].Status == "ill":
                if people[i].DaysIll == 3:
                    self._repository.update_person_status(people[i].id, "healthy")
                    self._repository.update_person_ill_days(people[i].id, 0)
                elif people[i].DaysIll > 0:
                    for j in range(0, len(people)):
                        if people[j].Status == "healthy" and people[j].Immunization == "nonvaccinated":
                            self._repository.update_person_status(people[j].id, "ill")
                            break
                    self._repository.update_person_ill_days(people[i].id, people[i].DaysIll + 1)
                elif people[i].DaysIll == 0:
                    self._repository.update_person_ill_days(people[i].id, people[i].DaysIll + 1)

    def vaccinate_person(self, personId):
        pass