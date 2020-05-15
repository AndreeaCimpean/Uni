#include "Repository.h"
#include <fstream>

using namespace std;

std::vector<std::shared_ptr<HospitalDepartment>> Repository::get_all_departments() const
{
	return this->departments;
}

void Repository::add_department(std::shared_ptr<HospitalDepartment> department)
{
	this->departments.push_back(department);
}

void Repository::set_file(const std::string& file)
{
	this->file = file;
}

std::string Repository::get_file()
{
	return this->file;
}

void Repository::write_to_file()
{
	ofstream outpu_file(this->file);
	for (auto department : departments)
	{
		outpu_file << department->toString() <<endl;
	}
	outpu_file.close();
}
