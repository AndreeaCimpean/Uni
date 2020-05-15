#pragma once
#include "MedicalAnalysis.h"

class BMI : public MedicalAnalysis
{
private:
	double value;
public:
	BMI(const std::string& date, const double value) : MedicalAnalysis{ date }, value{ value }{};
	bool isResultOk() const override;
	std::string toString() const override;
};

