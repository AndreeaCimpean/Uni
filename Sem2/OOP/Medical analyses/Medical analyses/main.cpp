#include <iostream>
#include "UI.h"
#include "Service.h"
#include "Repository.h"
#include "BMI.h"
#include "BP.h"

using namespace std;

int main()
{
	shared_ptr<MedicalAnalysis> bp = make_shared<BP>("2020.05.02", 60, 10);
	shared_ptr<MedicalAnalysis> bmi = make_shared<BMI>("2020.05.02", 19.4);
	Repository repository{};
	Service service{ repository, "Ana" };	
	service.addAnalysis(bp);
	service.addAnalysis(bmi);
	UI ui{ service };
	ui.run();
	return 0;
}