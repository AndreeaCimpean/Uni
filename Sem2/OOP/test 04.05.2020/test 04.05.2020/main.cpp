#include <iostream>
#include "Repository.h"
#include "Service.h"
#include "UI.h"

using namespace std;

int main()
{
	Repository repository{};
	Service service{ repository };
	UI ui{ service };
	ui.run();
	return 0;
}