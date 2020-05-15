#pragma once
#include <string>
class HospitalDepartment
{
protected:
	std::string hospitalName;
	int numberOfDoctors;
public:
	HospitalDepartment(const std::string& hospitalName, const int numberOfDoctors) : hospitalName{ hospitalName }, numberOfDoctors{ numberOfDoctors }{};
	virtual bool isEfficent() const = 0;
	virtual std::string toString() const;
	std::string get_hospital_name() const;
	int get_numer_of_doctors() const;

};

