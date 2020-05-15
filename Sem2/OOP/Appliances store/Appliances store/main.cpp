#include "UI.h"
#include "Controller.h"
#include "Service.h"
#include "Refrigerator.h"
#include "DishWasher.h"
#include <iostream>

using namespace std;

int main()
{
	Controller controller;
	shared_ptr<Appliance> someRefrigerator = make_shared<Refrigerator>("123", 12, "A", true);
	shared_ptr<Appliance> someDishWasher = make_shared<DishWasher>("124", 10, 11, 2);
	controller.add_appliance(someRefrigerator);
	controller.add_appliance(someDishWasher);
	Service service{ controller };
	UI ui{ service };
	ui.run();
	return 0;
}