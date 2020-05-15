#pragma once
#include "Repository.h"

class Service
{
private:
	Repository& repository;
public:
	Service(Repository& repository) : repository{ repository } {};
	std::vector<std::shared_ptr<HospitalDepartment>> get_all_departments() const;
	void add_department(std::shared_ptr<HospitalDepartment> department);
	std::vector<std::shared_ptr<HospitalDepartment>> get_all_efficent() const;
	void set_file(const std::string& file);
	bool is_file();
	void write_to_file();
};

