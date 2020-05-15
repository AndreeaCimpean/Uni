#pragma once
#include <memory>
#include <vector>
#include "HospitalDepartment.h"

class Repository
{
private:
	std::string file;
	std::vector<std::shared_ptr<HospitalDepartment>> departments;
public:
	Repository() { this->file = ""; };
	std::vector<std::shared_ptr<HospitalDepartment>> get_all_departments() const;
	void add_department(std::shared_ptr<HospitalDepartment> department);
	void set_file(const std::string& file);
	std::string get_file();
	void write_to_file();
};

