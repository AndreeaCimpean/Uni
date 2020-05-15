#include <iostream>
#include "UI.h"
#include "Repository.h"
#include "Service.h"

using namespace std;

int main()
{
	Repository repository{};
	Service service{ repository };
	UI ui{ service };
	ui.run();
	return 0;
}