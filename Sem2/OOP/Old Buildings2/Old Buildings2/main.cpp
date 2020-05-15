#include <iostream>
#include "Repository.h"
#include "Block.h"
#include "House.h"
#include "Controller.h"
#include "UI.h"
#include <memory>
#include <crtdbg.h>

using namespace std;

int main()
{
	{
		shared_ptr<Building> block = make_shared<Block>("Str. 1 Mai nr. 4", 1998, 30, 0);
		shared_ptr<Building> house = make_shared<House>("Str. Ana nr. 4", 1000, "duplex", false);
		Repository repository{};
		repository.addBuilding(block);
		repository.addBuilding(house);
		Controller controller{ repository };
		UI ui{ controller };
		ui.run();
		return 0;
	}
	_CrtDumpMemoryLeaks();
}