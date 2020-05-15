#pragma once
#include "HospitalDepartment.h"
class NeonatalUnit : public HospitalDepartment
{
	int numberOfMothers;
	int numberOfNewborns;
	double averageGrade;
public:
	NeonatalUnit(const std::string& hospitalName, const int numberOfDoctors, const int numberOfMothers, const int numberOfNewborns, const double averageGrade) : HospitalDepartment{ hospitalName, numberOfDoctors }, numberOfMothers{ numberOfMothers }, numberOfNewborns{ numberOfNewborns }, averageGrade{ averageGrade }{};
	bool isEfficent() const override;
	std::string toString() const override;
};

