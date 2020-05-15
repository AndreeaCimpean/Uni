#include "HospitalDepartment.h"

using namespace std;

std::string HospitalDepartment::toString() const
{
	string department = "";
	department = this->hospitalName;
	return department;
}

std::string HospitalDepartment::get_hospital_name() const
{
	return this->hospitalName;
}

int HospitalDepartment::get_numer_of_doctors() const
{
	return this->numberOfDoctors;
}
