#pragma once
#include "HospitalDepartment.h"

class Surgery : public HospitalDepartment
{
private:
	int numberOfPatients;
public:
	Surgery(const std::string& hospitalName, const int numberOfDoctors, const int numberOfPatients) : HospitalDepartment{ hospitalName, numberOfDoctors }, numberOfPatients{ numberOfPatients }{};
	bool isEfficent() const override;
	std::string toString() const override;
};

