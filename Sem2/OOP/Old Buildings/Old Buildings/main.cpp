#include "Repository.h"
#include "UI.h"
#include "Controller.h"
#include "tests.h"

using namespace std;

int main()
{
	test_all();
	Repository repository{};
	Controller controller{ repository };
	UI ui{ controller };
	ui.run();
	return 0;
}