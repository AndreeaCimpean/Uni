#include <iostream>
#include "UI.h"
#include "Service.h"
#include "Repository.h"
#include "MedicalAnalysis.h"
#include "BP.h"
#include "BMI.h"
#include <memory>

using namespace std;

int main()
{
	shared_ptr<MedicalAnalysis> bp = make_shared<BP>("2020.05.01", 12, 45);
	shared_ptr<MedicalAnalysis> bmi = make_shared<BMI>("2020.05.02", 19.1);
	Repository repository{};
	repository.add_analysis(bp);
	repository.add_analysis(bmi);
	Service service{ repository };
	UI ui{ service };
	ui.run();
	return 0;
}