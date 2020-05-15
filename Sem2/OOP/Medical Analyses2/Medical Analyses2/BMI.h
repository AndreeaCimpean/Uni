#pragma once
#include "MedicalAnalysis.h"
class BMI:public MedicalAnalysis
{
private:
	double value;
public:
	BMI(const std::string& date, const double value) : MedicalAnalysis{ date }, value{ value }{};
	std::string toString() const override;
	bool isResultOk() const override;
};

