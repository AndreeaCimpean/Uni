#include "Service.h"

using namespace std;

std::vector<std::shared_ptr<HospitalDepartment>> Service::get_all_departments() const
{
	return this->repository.get_all_departments();
}

void Service::add_department(std::shared_ptr<HospitalDepartment> department)
{
	this->repository.add_department(department);
}

std::vector<std::shared_ptr<HospitalDepartment>> Service::get_all_efficent() const
{
	auto departments = this->get_all_departments();
	std::vector<std::shared_ptr<HospitalDepartment>> filtered;
	for (auto department : departments)
	{
		if (department->isEfficent())
			filtered.push_back(department);
	}
	return filtered;
}

void Service::set_file(const std::string& file)
{
	this->repository.set_file(file);
}

bool Service::is_file()
{
	if (this->repository.get_file() != "")
		return true;
	return false;
}

void Service::write_to_file()
{
	this->repository.write_to_file();
}
