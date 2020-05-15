#include "NeonatalUnit.h"

using namespace std;

bool NeonatalUnit::isEfficent() const
{
	return (this->averageGrade >= 8.5 && this->numberOfNewborns >= this->numberOfMothers);
}

std::string NeonatalUnit::toString() const
{
	string department = HospitalDepartment::toString();
	department += ",Neonatal Unit,";
	department += to_string(this->numberOfDoctors);
	department += ",";
	department += to_string(this->numberOfMothers);
	department += ",";
	department += to_string(this->numberOfNewborns);
	department += ",";
	department += to_string(this->averageGrade);
	return department;
}