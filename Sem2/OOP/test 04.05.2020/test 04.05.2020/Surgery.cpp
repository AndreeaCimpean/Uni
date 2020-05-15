#include "Surgery.h"

using namespace std;

bool Surgery::isEfficent() const
{
	return ((double)(this->numberOfDoctors) / (double)(this->numberOfPatients) >= 2);
}

std::string Surgery::toString() const
{
	string department = HospitalDepartment::toString();
	department += ",Surgery,";
	department += to_string(this->numberOfDoctors);
	department += ",";
	department += to_string(this->numberOfPatients);
	return department;
}
